#%%
from time import time as clock
from pylab import np, plt
import femm, os
MyModel = 'my_SPM_motor_AGB.fem'

# base frequency in Hz
wbase=4000/60 #(4000 rev/minute)*(minute/(60*seconds))

# range of speeds over which to evaluate losses
SpeedMin = 100 # in RPM
SpeedMax = 8000 # in RPM
SpeedStep = 100 # in RPM

# Winding properties
MyIdCurrent = 0 # direct current in phase current amplitude scaling
MyIqCurrent = 2 # quadrature current phase current amplitude scaling
MyLowestHarmonic = 2 # lowest numbered harmonic present in the stator winding
AWG=25 # Magnet wire gauge used in winding
WindingFill=0.3882
PhaseResistance = 0.223*2.333 # phase resistance including end turns at 20 degC
TemperatureRise = 100 # temperature increase, degrees C

# Magnet properties
RotorMagnets = 16
omag = 0.556*10**6                  # conductivity of sintered NdFeB in S/m

# Core properties
ce = 0.530 # Eddy current coefficient in (Watt/(meter**3 * T**2 * Hz**2)
ch = 143. # Hysteresis coefficient in (Watts/(meter**3 * T**2 * Hz)
cs = 0.95  # Lamination stacking factor (nondimensional)

####################################
## End User-Defined Parameters
####################################

# helpful unit definitions
deg=np.pi/180.

# angle through which to spin the rotor in degrees
n = 360/MyLowestHarmonic

# angle increment in degrees
dk = 1

ns = int(np.round(n/dk)) # 180 deg / 1 deg # number of steps

# A similar loss/volume expression can be derived to compute proximity
# effect losses in the windings.  Use the low frequency approximiation
# from the paper, since in this case, wire size is a lot smaller than skin
# depth at the frequencies of interest.

# Get parameters for proximity effect loss computation for phase windings
dwire=0.324861*0.0254*np.exp(-0.115942*AWG) # wire diameter in meters as a function of AWG
owire = (58*10**6)/(1+TemperatureRise*0.004) # conductivity of the wire in S/m at prescribed deltaT
cePhase = (np.pi**2/8)*dwire**2*WindingFill*owire

## Perform a series of finite element analyses

femm.openfemm(1)
femm.opendocument(MyModel)
femm.mi_smartmesh(0)  # use relatively coarse mesh to save time
femm.mi_saveas('temp.fem')

# Run an analysis through an entire spin of the rotor and record
# element centroid flux density and vector potential (using the mesh from the first iteration)
# at every step.  This information will then be used to estimate
# core losses
for kk in range(ns):
    starttime = clock()
    k = kk*dk # rotor angle in degrees

    # Set the rotor angle to the correct angle for this iteration
    # Since the model uses an "air gap element", the rotor position is set by
    # modifying a parameter indicated rotor position in the air gap element 
    # boundary definition
    femm.mi_modifyboundprop('AGE',10,k)

    # make sure that the current is set to the appropriate value for this iteration.  
    tta = (RotorMagnets/2) * k*deg
    Id = np.array([ np.cos(tta),  np.cos(tta-2*np.pi/3),  np.cos(tta+2*np.pi/3)])
    Iq = np.array([-np.sin(tta), -np.sin(tta-2*np.pi/3), -np.sin(tta+2*np.pi/3)])
    Itot =  MyIdCurrent*Id + MyIqCurrent*Iq
    femm.mi_setcurrent('A', Itot[0])
    femm.mi_setcurrent('B', Itot[1])
    femm.mi_setcurrent('C', Itot[2])
    
    femm.mi_analyze(1)
    femm.mi_loadsolution()
    femm.mo_smooth('off')  # flux smoothing algorithm is off
    if k == 0:
        # Record the initial mesh elements if the first time through the loop
        nn = int(femm.mo_numelements())
        b  = np.zeros([ns,nn], dtype=np.complex64) # matrix that will hold the flux density info
        A  = np.zeros([ns,nn]) # matrix that will hold the vector potential info
        z  = np.zeros([nn,1], dtype=np.complex64) # Location of the centroid of each element
        a  = np.zeros([nn,1]) # Area of each element
        g  = np.zeros([nn,1]) # Block label of each element
        tq = np.zeros([ns,1])
        for m in range(nn): # start from 0 for indexing but from 1 for counting 
            counting_element = m+1
            elm = femm.mo_getelement(counting_element)
            # z is a vector of complex numbers that represents the location of the centroid of each element.
            z[m] = elm[4-1] + 1j*elm[5-1]
            # element area in the length units used to draw the geometry
            a[m] = elm[6-1]
            # group number associated with the element
            g[m] = elm[7-1]

    # Store element flux densities *)
    u = np.exp(1j*k*np.pi/180.)
    for m in range(nn):
        if g[m]>10:
            # Element is in a rotor magnet, marked with group numbers 11 and higher
            # Store vector potential at the element centroid for elements that are in PMs
            A[kk,m] = femm.mo_geta( float(np.real(z[m])), 
                                    float(np.imag(z[m])) )
        elif g[m] > 0:
            # Element is on the stator or rotor iron.
            # Store flux density at the element centroid for these elements
                # b[kk,m] = np.dot( np.matrix(
                #                   femm.mo_getb(float(np.real(z[m])), 
                #                                float(np.imag(z[m])))), 
                #                   np.matrix([[1], [1j]]) )
            b_temp = femm.mo_getb(float(np.real(z[m])), 
                                  float(np.imag(z[m])))
            b[kk,m] = b_temp[0] + 1j*b_temp[1]

    # mo_getprobleminfo returns, among other things, the depth of the
    # machine in the into-the-page direction and the length units used to
    # draw the geometry. Both of these pieces of information will be needed
    # to integrate the losses over the volume of the machine.
    probinfo = femm.mo_getprobleminfo()

    # compute torque    
    tq[kk] = femm.mo_gapintegral('AGE',0)  
    femm.mo_close()
    
    print(f'{k} of {n} :: {clock()-starttime} seconds ::  {tq[kk]} N*m \n')

# clean up after finite element runs are finished
femm.closefemm()
os.remove('temp.fem')
os.remove('temp.ans')

#%% Add Up Core Losses

def matlab_fft(matrix_input):
    return np.fft.fft(matrix_input.T).T

# Compute the square of the amplitude of each harmonic at the centroid of
# each element in the mesh. Matlab's built-in FFT function makes this easy.
ns    = n/dk # 180 deg / 1 deg # number of steps
bxfft = np.abs(matlab_fft(np.real(b))) * (2/ns)
byfft = np.abs(matlab_fft(np.imag(b))) * (2/ns)
bsq  = (bxfft*bxfft) + (byfft*byfft)

# Compute the volume of each element in units of meter**3
stack_length = probinfo[3-1]            # Length of the machine in the into-the-page direction
lengthunits  = probinfo[4-1]  # Length of drawing unit in meters
v            = a*stack_length*lengthunits**2

# compute fft of A at the center of each element
from copy import deepcopy
Afft = matlab_fft(A)*(2/ns)
Jm   = deepcopy(Afft)
for k in range(1, RotorMagnets+1):
    g3 = g==(10+k)
    # total volume of the magnet under consideration
    vmag = np.dot(v.T, g3) # [inner product]
    # average current in the magnet for each harmonic
    Jo = np.dot(Jm, v * g3) /vmag # Jo's shape is (180, 1)
    # subtract averages off of each element in the magnet
    Jm = Jm - np.dot(Jo, g3.T)

Iphase  = np.sqrt(MyIdCurrent**2+MyIqCurrent**2)/np.sqrt(2)
PhaseOhmic = 3*(PhaseResistance*(1+TemperatureRise*0.004))*Iphase**2

#%%
results=[]

for thisSpeed in np.arange(SpeedMin, SpeedMax+0.1, SpeedStep):

    thisFrequency = thisSpeed/60 # mechanical speed in Hz

    # Make a vector representing the frequency associated with each harmonic
    # The last half of the entries are zeroed out so that we don't count each
    # harmonic twice--the upper half of the FFT a mirror of the lower half
    w=np.arange(ns)
    w=MyLowestHarmonic*thisFrequency*w*(w<(ns/2))

    # Now, total core loss can be computed in one fell swoop...
    # Dividing the result by cs corrects for the lamination stacking factor
    g1=(g==10)
    rotor_loss = np.dot(np.dot((ch*w+ce*w*w), bsq), (v*g1)) / cs

    g2=(g==1)
    stator_loss = np.dot(np.dot((ch*w+ce*w*w), bsq), (v*g2)) / cs

    # and prox losses can be totalled up in a similar way
    g4=(g==2)
    prox_loss = np.dot(np.dot((cePhase*w*w), bsq), (v*g4))

    # Add up eddy current losses in the magnets
    magnet_loss = 0.5 * np.dot((omag*(2*np.pi*w)**2), np.dot((np.abs(Jm)**2), v)) # g3 is already taken into account in variable Jm
                # 0.5 = (1/sqrt(2)) ** 2, the peak value Jm should be converted to RMS value for calculating loss power

    total_loss = rotor_loss + stator_loss + prox_loss + PhaseOhmic + magnet_loss

    results.append([thisSpeed, rotor_loss, stator_loss, magnet_loss, PhaseOhmic, prox_loss, total_loss])

print(len(results), len(results[0]))

# save('c:\\temp\\myLossData.m','results','-ASCII')

#%% Loss plot
list_speed       = [el[0] for el in results]
list_rotor_loss  = [el[1] for el in results]
list_stator_loss = [el[2] for el in results]
list_magnet_loss = [el[3] for el in results]
list_PhaseOhmic  = [el[4] for el in results]
list_prox_loss   = [el[5] for el in results]
list_total_loss  = [el[6] for el in results]
plt.figure(dpi=150)
plt.plot(list_speed, list_rotor_loss )
plt.plot(list_speed, list_stator_loss)
plt.plot(list_speed, list_magnet_loss)
plt.plot(list_speed, list_PhaseOhmic )
plt.plot(list_speed, list_prox_loss  )
plt.plot(list_speed, list_total_loss )
plt.xlabel('Speed, RPM')
plt.ylabel('Total Losses, Watts')
plt.title('Loss versus Speed')
plt.legend(['Rotor Core','Stator Core','Magnets','Coil Ohmic','Coil Proximity','Total Loss','Location','northwest'])
# plt.ylim([0, 0.3])

#%% Torque plot
plt.figure()
plt.plot(np.arange(0, n, dk), tq)
plt.xlabel('Rotor Angle, Degrees')
plt.ylabel('Torque, N*m')
plt.title('Torque on Rotor vs. Angle')

## Plot of heating

wbase=4000/60 #(4000 rev/minute)*(minute/(60*seconds))
w = np.arange(ns)
w = MyLowestHarmonic*wbase*w*(w<(ns/2)) 

# Rotor loss
g1=(g==10)
ptloss = np.transpose(np.dot(ch*w+ce*w*w, bsq)*g1) / cs

# Stator loss
g2=(g==1)
ptloss = ptloss + np.transpose(np.dot(ch*w+ce*w*w, bsq)*g2) / cs

# Prox loss
g4=(g==2)
ptloss = ptloss + np.transpose (np.dot(cePhase*w*w, bsq)*g4)

# PM contribution
ptloss = ptloss + 0.5*np.dot((omag*(2*np.pi*w)**2), (abs(Jm)**2)).T

## point location in z
heating = [np.real(z),np.imag(z),ptloss]
# save('c:\\temp\\mySPMLossData.txt','heating','-ASCII')


#%%
from pylab import np, plt
from re import X
import pandas as pd
df = pd.read_csv(r"D:\horyc\Downloads\femm-info\mySPMLossData.txt", header=None, delimiter=r"\s+")
df.columns = 'X', 'Y', 'Z'
X, Y, Z = np.array(df['X']), np.array(df['Y']), np.array(df['Z'])

# 散点图代替
plt.figure()
scaled_Z = (Z - Z.min()) / Z.ptp()
# plt.scatter( X, Y, edgecolors=plt.cm.Spectral(scaled_Z), color='white', marker='.')
plt.scatter( X, Y, edgecolors=plt.cm.Spectral(scaled_Z), color=plt.cm.Spectral(scaled_Z), marker='.')
plt.gca().set_aspect('equal')
# plt.gca().set_facecolor('xkcd:salmon')
# plt.gca().set_facecolor((1.0, 0.47, 0.42))
plt.gca().set_facecolor((57/255, 11/255, 26/255))

# 和david meeker一样！
plt.figure()
plt.tricontourf(X, Y, Z, cmap=plt.cm.CMRmap) # https://stackoverflow.com/questions/36579763/matplotlib-contour-plot-from-xyz-data-with-scale
plt.gca().set_aspect('equal')
plt.show()


# 画出来是空白的图
# [XX, YY] = np.meshgrid(X,Y)
# ZZ = np.zeros(XX.shape)
# for i in range(XX.shape[0]):
#     for j in range(XX.shape[1]):
#         if i==j:
#             ZZ[i,j] = Z[i]
# plt.figure()
# plt.contourf(X, Y, Z)
# plt.show()
