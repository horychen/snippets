# 姜峰：svpwm母线电压是线电压峰值，spwm母线电压是相电压峰值的两倍。【真理】
# 按【真理】，svpwm输出的线电压峰值是Vdc。
# 按【真理】，svpwm输出的相电压峰值是Vdc/sqrt(3)。
# 按恒幅值Clarke变换，三相PWM输出的六个非零电压矢量的幅值为Vdc*2/3。
# 咱们希望代码与母线电压Vdc无关，所以要把非零电压矢量的幅值标幺化一下，变成 Vdc*2/3 除以 Vdc/sqrt(3) 等于 2/sqrt(3)。

class Plot_Register:
    def __init__(self):
        self.data = []

    def add(self, row):
        self.data.append(row)

class SVgen_Object:
    def __init__(self):
        self.Ualfa = 0.0
        self.Ubeta = 0.0
        self.Unot = 0.0
        self.Ta = 0.5
        self.Tb = 0.5
        self.Tc = 0.5
        self.SYSTEM_MAX_PWM_DUTY_LIMATATION = 0.96
        self.SYSTEM_MIN_PWM_DUTY_LIMATATION = 0.04

        # Those variables are only needed in simulation
        self.bool_interupt_event = False
        self.bool_counting_down = False
        self.bool_RisingEdgeDelay_is_active = [False, False, False]
        self.bool_FallingEdgeDelay_is_active = [False, False, False]
        self.carrier_counter = 0
        self.deadtime_counter = [0, 0, 0]
        self.S1, self.S2, self.S3, self.S4, self.S5, self.S6 = 0,0,0,0,0,0
        self.EPwm1Regs_CMPA_bit_CMPA = 2500
        self.EPwm2Regs_CMPA_bit_CMPA = 2500
        self.EPwm3Regs_CMPA_bit_CMPA = 2500
def SVGEN_DQ(v, one_over_Vdc, Unot=0.0):

    # Note an additional factor of 1.7320508 is introduced to be equivalent to normalizing Ualfa and Ubeta to a base value of Vdc/sqrt(3)
    one_over_maximum_phase_voltage = one_over_Vdc * 1.7320508

    # Normalization (which converts [Volt] into [s])
    Talpha = v.Ualfa * one_over_maximum_phase_voltage # v.Ualfa is in sense of amplitude invariant Clarke transformation
    Tbeta  = v.Ubeta * one_over_maximum_phase_voltage # v.Ubeta is in sense of amplitude invariant Clarke transformation
    Tz     = v.Unot  * one_over_maximum_phase_voltage # duration of the added zero sequence voltage

    # Inverse clarke transformation??
    A =                     Tbeta # 0 degree line pointing at 0 degree
    C =  1.7320508*Talpha - Tbeta # C =  sin( 60/180*np.pi)*Talpha - sin(30/180*np.pi)*Tbeta
    B = -1.7320508*Talpha - Tbeta # B = -sin( 60/180*np.pi)*Talpha - sin(30/180*np.pi)*Tbeta

    # 60 degree Sector determination
    Sector = 0 
    if (A > 0): Sector = 1
    if (C > 0): Sector = Sector+2
    if (B > 0): Sector = Sector+4

    # X,Y,Z calculations ()
    XXX =                            Tbeta # This is also the A line
    YYY =  0.86602540378444*Talpha + Tbeta*0.5 # This is also the B line
    ZZZ = -0.86602540378444*Talpha + Tbeta*0.5 # This is also the C line

    if Sector == 0: # Sector 0: this is special case for (Ualfa,Ubeta) = (0,0)*/
        v.Ta = 0.5
        v.Tb = 0.5
        v.Tc = 0.5
    if Sector == 1: #Sector 1: t1=Z and t2=Y (abc ---> Tb,Ta,Tc)*/
        t1 = ZZZ
        t2 = YYY
        v.Tb=(1-t1-t2)*0.5 + Tz*0.5
        v.Ta = v.Tb+t1              # taon = tbon+t1        */
        v.Tc = v.Ta+t2              # tcon = taon+t2        */
    elif Sector == 2:     # Sector 2: t1=Y and t2=-X (abc ---> Ta,Tc,Tb)*/
        t1 = YYY
        t2 = -XXX
        v.Ta=(1-t1-t2)*0.5 + Tz*0.5
        v.Tc = v.Ta+t1              #  tcon = taon+t1       */
        v.Tb = v.Tc+t2              #  tbon = tcon+t2       */
    elif Sector == 3:     # Sector 3: t1=-Z and t2=X (abc ---> Ta,Tb,Tc)*/
        t1 = -ZZZ
        t2 = XXX
        v.Ta=(1-t1-t2)*0.5 + Tz*0.5
        v.Tb = v.Ta+t1              #   tbon = taon+t1      */
        v.Tc = v.Tb+t2              #   tcon = tbon+t2      */
    elif Sector == 4:     # Sector 4: t1=-X and t2=Z (abc ---> Tc,Tb,Ta)*/
        t1 = -XXX
        t2 = ZZZ
        v.Tc=(1-t1-t2)*0.5 + Tz*0.5
        v.Tb = v.Tc+t1              #   tbon = tcon+t1      */
        v.Ta = v.Tb+t2              #   taon = tbon+t2      */
    elif Sector ==  5:    # Sector 5: t1=X and t2=-Y (abc ---> Tb,Tc,Ta)*/
        t1 = XXX
        t2 = -YYY                   #   tbon = (1-t1-t2)*0.5    */
        v.Tb=(1-t1-t2)*0.5 + Tz*0.5
        v.Tc = v.Tb+t1              #   taon = tcon+t2      */
        v.Ta = v.Tc+t2
    elif Sector == 6:     # Sector 6: t1=-Y and t2=-Z (abc ---> Tc,Ta,Tb)*/
        t1 = -YYY
        t2 = -ZZZ
        v.Tc=(1-t1-t2)*0.5 + Tz*0.5
        v.Ta = v.Tc+t1              #   taon = tcon+t1      */
        v.Tb = v.Ta+t2              #   tbon = taon+t2      */

    # 高低有效逻辑翻转
    v.Ta = 1-v.Ta
    v.Tb = 1-v.Tb
    v.Tc = 1-v.Tc

    # 考虑到输出功率时母线电压会跌落，不要用满占空比。
    if (v.Ta>v.SYSTEM_MAX_PWM_DUTY_LIMATATION): v.Ta=v.SYSTEM_MAX_PWM_DUTY_LIMATATION
    if (v.Tb>v.SYSTEM_MAX_PWM_DUTY_LIMATATION): v.Tb=v.SYSTEM_MAX_PWM_DUTY_LIMATATION
    if (v.Tc>v.SYSTEM_MAX_PWM_DUTY_LIMATATION): v.Tc=v.SYSTEM_MAX_PWM_DUTY_LIMATATION
    if (v.Ta<v.SYSTEM_MIN_PWM_DUTY_LIMATATION): v.Ta=v.SYSTEM_MIN_PWM_DUTY_LIMATATION
    if (v.Tb<v.SYSTEM_MIN_PWM_DUTY_LIMATATION): v.Tb=v.SYSTEM_MIN_PWM_DUTY_LIMATATION
    if (v.Tc<v.SYSTEM_MIN_PWM_DUTY_LIMATATION): v.Tc=v.SYSTEM_MIN_PWM_DUTY_LIMATATION

    return v
def gate_signal_generator(ii, v,
    CPU_TICK_PER_SAMPLING_PERIOD = 10000,
    DEAD_TIME_AS_COUNT = 200):
    if ii % CPU_TICK_PER_SAMPLING_PERIOD == 0:
        v.bool_interupt_event = True
        v.deadtime_counter[0] = 0
        v.deadtime_counter[1] = 0
        v.deadtime_counter[2] = 0
        v.bool_RisingEdgeDelay_is_active[0] = False
        v.bool_RisingEdgeDelay_is_active[1] = False
        v.bool_RisingEdgeDelay_is_active[2] = False
        v.bool_FallingEdgeDelay_is_active[0] = False
        v.bool_FallingEdgeDelay_is_active[1] = False
        v.bool_FallingEdgeDelay_is_active[2] = False

    if ii % CPU_TICK_PER_SAMPLING_PERIOD == CPU_TICK_PER_SAMPLING_PERIOD * 0.5:
        v.bool_counting_down = True
        v.deadtime_counter[0] = 0
        v.deadtime_counter[1] = 0
        v.deadtime_counter[2] = 0
        v.bool_RisingEdgeDelay_is_active[0] = False
        v.bool_RisingEdgeDelay_is_active[1] = False
        v.bool_RisingEdgeDelay_is_active[2] = False
        v.bool_FallingEdgeDelay_is_active[0] = False
        v.bool_FallingEdgeDelay_is_active[1] = False
        v.bool_FallingEdgeDelay_is_active[2] = False

    if v.bool_interupt_event:
        v.bool_interupt_event = False
        v.bool_counting_down = False
        v.carrier_counter = 0

    if v.bool_counting_down:
        v.carrier_counter -= 1
    else:
        v.carrier_counter += 1

    v.phase_U_gate_signal = True if v.carrier_counter >= v.EPwm1Regs_CMPA_bit_CMPA else False
    v.phase_V_gate_signal = True if v.carrier_counter >= v.EPwm2Regs_CMPA_bit_CMPA else False
    v.phase_W_gate_signal = True if v.carrier_counter >= v.EPwm3Regs_CMPA_bit_CMPA else False

    # Insert dead time based on Active Hgih Complementary (AHC)
    if v.bool_counting_down == False:

        if v.carrier_counter >= v.EPwm1Regs_CMPA_bit_CMPA:
            v.deadtime_counter[0] += 1
            v.bool_RisingEdgeDelay_is_active[0] = True if v.deadtime_counter[0] <= DEAD_TIME_AS_COUNT else False

        if v.carrier_counter >= v.EPwm2Regs_CMPA_bit_CMPA:
            v.deadtime_counter[1] += 1
            v.bool_RisingEdgeDelay_is_active[1] = True if v.deadtime_counter[1] <= DEAD_TIME_AS_COUNT else False

        if v.carrier_counter >= v.EPwm3Regs_CMPA_bit_CMPA:
            v.deadtime_counter[2] += 1
            v.bool_RisingEdgeDelay_is_active[2] = True if v.deadtime_counter[2] <= DEAD_TIME_AS_COUNT else False

    elif v.bool_counting_down == True:

        if v.carrier_counter < v.EPwm1Regs_CMPA_bit_CMPA:
            v.deadtime_counter[0] += 1
            v.bool_FallingEdgeDelay_is_active[0] = True if v.deadtime_counter[0] <= DEAD_TIME_AS_COUNT else False

        if v.carrier_counter < v.EPwm2Regs_CMPA_bit_CMPA:
            v.deadtime_counter[1] += 1
            v.bool_FallingEdgeDelay_is_active[1] = True if v.deadtime_counter[1] <= DEAD_TIME_AS_COUNT else False

        if v.carrier_counter < v.EPwm3Regs_CMPA_bit_CMPA:
            v.deadtime_counter[2] += 1
            v.bool_FallingEdgeDelay_is_active[2] = True if v.deadtime_counter[2] <= DEAD_TIME_AS_COUNT else False

    v.S1, v.S2, v.S3 = v.phase_U_gate_signal, v.phase_V_gate_signal, v.phase_W_gate_signal
    v.S4, v.S5, v.S6 = not v.S1, not v.S2, not v.S3
    if v.bool_RisingEdgeDelay_is_active[0]:   v.S1 = False
    if v.bool_FallingEdgeDelay_is_active[0]:  v.S4 = False
    if v.bool_RisingEdgeDelay_is_active[1]:   v.S2 = False
    if v.bool_FallingEdgeDelay_is_active[1]:  v.S5 = False
    if v.bool_RisingEdgeDelay_is_active[2]:   v.S3 = False
    if v.bool_FallingEdgeDelay_is_active[2]:  v.S6 = False

def main():

    plot_register = Plot_Register()
    svgen1 = SVgen_Object()

    from pylab import np, plt, mpl
    CL_TS = 1e-4

    Vdc = 50; one_over_Vdc = 1.0/Vdc
    AMPL = 25

    # 测试1
    for ANGLE in range(0, 360, 5):

        svgen1.Ualfa = AMPL * np.cos(ANGLE/180*np.pi)
        svgen1.Ubeta = AMPL * np.sin(ANGLE/180*np.pi)

        SVGEN_DQ(svgen1, one_over_Vdc)

        EPwm1Regs_CMPA_bit_CMPA = (int)(svgen1.Ta*50000000*CL_TS)
        EPwm2Regs_CMPA_bit_CMPA = (int)(svgen1.Tb*50000000*CL_TS)
        EPwm3Regs_CMPA_bit_CMPA = (int)(svgen1.Tc*50000000*CL_TS)

        print( 
            EPwm1Regs_CMPA_bit_CMPA, EPwm2Regs_CMPA_bit_CMPA, EPwm3Regs_CMPA_bit_CMPA, end=' | ')
        print(f'{svgen1.Ta=:.2f}, {svgen1.Tb=:.2f}, {svgen1.Tc=:.2f}')

        # myTbeta = svgen1.Ta
        myTbeta  = (svgen1.Tb + svgen1.Tc)
        myTalpha = (svgen1.Tb - svgen1.Tc) / 1.7320508
        plt.plot(myTalpha, myTbeta, '.')

        myTalpha = (svgen1.Ta - 0.500*svgen1.Tb - 0.500*svgen1.Tc) * 2 / 3
        myTbeta  = (            0.866*svgen1.Tb - 0.866*svgen1.Tc) * 2 / 3
        plt.plot(myTalpha, myTbeta, 'o')
        plt.gca().set_aspect('equal')
    # plt.show()


    # 测试2
    # main loop
    CPU_TICK_PER_SAMPLING_PERIOD = 500
    AMPL = 25 # V
    ANGLE = 90 # deg
    plt.figure()
    plt.gca().set_aspect('equal')
    for ii in range(16*CPU_TICK_PER_SAMPLING_PERIOD):

        if ii%CPU_TICK_PER_SAMPLING_PERIOD == 0:
            # ANGLE += 1e-4 * 20e4
            ANGLE += 1e-4 * 5e4

            svgen1.Ualfa = AMPL * np.cos(ANGLE/180*np.pi)
            svgen1.Ubeta = AMPL * np.sin(ANGLE/180*np.pi)
            SVGEN_DQ(svgen1, one_over_Vdc)
            # svgen1.EPwm1Regs_CMPA_bit_CMPA = 4534
            # svgen1.EPwm2Regs_CMPA_bit_CMPA = 1217
            # svgen1.EPwm3Regs_CMPA_bit_CMPA = 465 
            svgen1.EPwm1Regs_CMPA_bit_CMPA = (int)(svgen1.Ta*CPU_TICK_PER_SAMPLING_PERIOD*0.5) #50000000*CL_TS)
            svgen1.EPwm2Regs_CMPA_bit_CMPA = (int)(svgen1.Tb*CPU_TICK_PER_SAMPLING_PERIOD*0.5) #50000000*CL_TS)
            svgen1.EPwm3Regs_CMPA_bit_CMPA = (int)(svgen1.Tc*CPU_TICK_PER_SAMPLING_PERIOD*0.5) #50000000*CL_TS)

            plt.plot(svgen1.Ualfa, svgen1.Ubeta, 'o')

        gate_signal_generator(ii, svgen1, CPU_TICK_PER_SAMPLING_PERIOD=CPU_TICK_PER_SAMPLING_PERIOD, DEAD_TIME_AS_COUNT=200/10000*CPU_TICK_PER_SAMPLING_PERIOD)

        plot_register.add([
            svgen1.phase_U_gate_signal, 
            svgen1.phase_V_gate_signal, 
            svgen1.phase_W_gate_signal, 
            svgen1.carrier_counter, 
            svgen1.S1, 
            svgen1.S2, 
            svgen1.S3, 
            svgen1.S4, 
            svgen1.S5, 
            svgen1.S6
        ])

    U = waveform__phase_U_gate_signal = np.array(plot_register.data)[:, 0]
    V = waveform__phase_V_gate_signal = np.array(plot_register.data)[:, 1]
    W = waveform__phase_W_gate_signal = np.array(plot_register.data)[:, 2]
    Carrier = np.array(plot_register.data)[:, 3]
    S1 = np.array(plot_register.data)[:, 4]
    S2 = np.array(plot_register.data)[:, 5]
    S3 = np.array(plot_register.data)[:, 6]
    S4 = np.array(plot_register.data)[:, 7]
    S5 = np.array(plot_register.data)[:, 8]
    S6 = np.array(plot_register.data)[:, 9]

    plt.subplots(sharex=True)
    plt.subplot(611 ); plt.ylabel(u'Carrier')
    plt.plot(Carrier)

    plt.subplot(612); plt.ylabel(u'Terminal Voltage [V]')
    plt.plot(U * Vdc)
    plt.plot(V * Vdc)
    plt.plot(W * Vdc)

    plt.subplot(613); plt.ylabel(u'Line Voltage [V]')
    plt.plot((U-V) * Vdc)
    plt.plot((V-W) * Vdc)
    plt.plot((W-U) * Vdc)

    plt.subplot(614); plt.ylabel('S1, S4')
    plt.plot(S1, '--')
    plt.plot(S4, '--')
    plt.subplot(615); plt.ylabel('S2, S5')
    plt.plot(S2, '--')
    plt.plot(S5, '--')
    plt.subplot(616); plt.ylabel('S3, S6')
    plt.plot(S3, '--')
    plt.plot(S6, '--')



    fig, axes = plt.subplots(5, 1, sharex=True)
    axes[0].set_ylabel(u'Carrier')
    axes[0].plot(Carrier)

    axes[1].set_ylabel('S1')
    axes[1].plot(S1, '--')

    axes[2].set_ylabel('S2')
    axes[2].plot(S2, '--')

    axes[3].set_ylabel('S3')
    axes[3].plot(S3, '--')

    axes[4].set_ylabel('Zero')
    # axes[4].plot(S1+S2+S3, '--')
    axes[4].plot((U+V+W) * Vdc)

    plt.show()

if __name__ == '__main__':
    main()

