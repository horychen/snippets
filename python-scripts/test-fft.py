from pylab import plt, np

frequency = 1 # lowest frequency in signal s
period = 1 / frequency
# nc: number of cycles
# ns: number of steps

nc = 1; ns = 16 # 偶数
# nc = 1; ns = 17 # 奇数
# nc = 1; ns = 120 # 好
# nc = 10; ns = 120 # 采样频率不够，但是信号中有比采样频率高的分量，混叠发生了（0.1Hz处出现了不该有的波峰，此时分辨率高反而导致了问题）
# nc = 10; ns = 1200 # 双高，爽

# step_size_sec = nc * period / (ns-1) # 泄露示意（需要加窗） Leakage happens because the implict periodicity is broken and also the the DFT resolution is not exact
step_size_sec = nc * period / ns

t = np.arange(ns) * step_size_sec  # Run one more step to have full DFT resolution
# RESOLUTION = 1/t.ptp(); print(f'{RESOLUTION=}')
RESOLUTION = step_size_sec*ns

print('Signal duration time:', step_size_sec*ns)
print('SAMPLING_FREQUENCY:', 1/step_size_sec, 'Hz')
print(f'RESOLUTION = step_size_sec*ns =', step_size_sec*ns)
print(t)

s = 3 + 1 *np.sin(frequency*1  *2*np.pi*t) \
      + 2 *np.sin(frequency*5  *2*np.pi*t) \
      + 3 *np.sin(frequency*7  *2*np.pi*t) \
      + 0*4 *np.sin(frequency*7.5*2*np.pi*t) \
      + 0*4 *np.sin(frequency*8  *2*np.pi*t) \
      + 0*4 *np.sin(frequency*8.5*2*np.pi*t) \
      + 5 *np.sin(frequency*50 *2*np.pi*t) # 混叠示意（需要先抗混叠滤波）

fig, axes = plt.subplots(2, dpi=150)
axes[0].plot(t, s, '-o')

if True:
    sfft = np.fft.fft(s.T).T
    w_ = np.arange(ns)
    w = RESOLUTION * w_ * (w_<=(ns/2))
    spectrum = abs(sfft)*2/ns 

    axes[1].plot(w, spectrum, '.')
    for index,(a,b) in enumerate(zip(w, spectrum)):
        print(f'{index} | {a} Hz | ' + f'{b:g} V' if b>1e-14 else f'{index} | {a} Hz | ')


    print(''' 关于公式 spectrum = abs(sfft)*2/ns，注意以下几点：
    要点1：直流分量错误得乘了个2。
    要点2：ns如果是奇数，可以测量得到采样频率的1/2处的信号，此时你的分辨率可能不支持分辨它；但是反过来你甚至可以分出比1/2采样频率更高的频率。
    要点3：ns如果是偶数，无法获得采样频率的1/2处的信号。
    ''')
    # 要点4：【误差来源】基于DFT计算损耗，如果发生频谱泄露，要主要到本身DFT计算的结果就是偏小的这个事实！你看5Hz的幅值才0.886 V，实际上是1.0 V才对。
    # 要点5：【误差来源】如果泄露发生，基频的倍数越高处的波峰，频谱泄露越严重，所以铁耗计算不要搞到很高倍谐波了。

if True:

    def DFT(x):
        ns = len(x)
        Matrix = np.dot(np.arange(ns).reshape(ns,1), np.arange(ns).reshape(1,ns))
        print(Matrix)
        W = np.exp(-2j * np.pi / ns)
        e = np.exp(-2j * np.pi / ns * Matrix )
        X = np.dot(e, x)
        return X

    sDFT = DFT(s)
    spectrumDFT = abs(sDFT)*2/ns
    axes[1].plot(w, spectrumDFT, 'x')


plt.show()
