# Snippets

_Userful snippets (keeps updating)._

# Use CMake and MinGW on Windows
hello.cpp
```cpp
#include <iostream>

int main(){
    std::cout << "Hello world\n";
    return 1;
}
```

CMakeLists.txt
```
cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(hello VERSION 1.0)
add_executable(hello hello.cpp)
```

camke-on-windows.bat
```
mkdir build
cd build
cmake .. -G "MinGW Makefiles"
mingw32-make
```

> Assuming CMake and MinGW (not mingw-64) are installed 

# Font Setup for Matplotlib that I Ever Wanted
```python
from pylab import mpl, plt, np
plt.style.use('classic')
plt.rcParams['mathtext.fontset'] = 'stix'
mpl.rc('font', family='Times New Roman', size=14.0)
mpl.rc('legend', fontsize=8)

font = {'family':'Times New Roman', 'weight':'normal', 'size':14} # now we can delete this

fig, axes = plt.subplots(nrows=6, ncols=1, dpi=150, facecolor='w', figsize=(8,6), sharex=True)

ax = axes[0]
ax.plot(t, y1, label=r'$\omega_r^*$')
ax.plot(t, y2, label=r'$\omega_r$')
ax.set_ylabel(r'Speed [r/min]', multialignment='center') #) #, fontdict=font)
ax.legend(loc=2, fontsize=6) # one can change fontsize locally if needed

for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks(): # now we can delete this
    tick.label.set_font(font)
```

# Adobe Acrobat Reader Shortcuts
- Ctrl+H, reading mode
- Alt+-, jump back
- F4 and Shift+F4, open side bar menu

# Matplotlib tips:

https://stackoverflow.com/questions/31357611/format-y-axis-as-percent

# Altium Designer
Green X error markers appear when design is updated. 
Shortcut is `T-M`. 
See this [post](https://electronics.stackexchange.com/questions/341075/altium-designer-how-to-remove-green-xs-error-markers)

Ctrl+M：测距

如果要更新封装（Footprint），可以直接在PCBDoc上右键替换某个元件的封装为新的。然后按T-M清除绿色的Error Makers。

# Circuitikz 
There are two use cases of symbol "-|":
1. Specifying a perpendicular coordinates
3. `|-` ("first vertical, then horizontal" path modifier
>https://tex.stackexchange.com/questions/228486/lining-amplifiers-up-in-circuitikz
>https://tex.stackexchange.com/questions/286194/working-with-perpendicular-coordinates-in-circuitikz

How to add two coordinates to get a new one?
```latex
($ (a) + (0,1) $)
```
>https://tex.stackexchange.com/questions/48756/tikz-relative-coordinates

# Git: Line-ending 
This is an issue I met when I use the git in WSL between local windows system and remote overleaf server. The line-ending is LF in windows system, but when I git in WSL, sometimes the whole file is changed as the line-ending is all somehow conveted by either my system or the overleaf server.

See this [post](https://stackoverflow.com/questions/10418975/how-to-change-line-ending-settings)

My expected hehavior is to do nothing:
```shell
git config --global core.autocrlf false
```

# Remove a pdf file from git
See [this](https://stackoverflow.com/questions/40879523/how-to-remove-all-pdf-files-from-a-git-push).
```
git rm -r ismb2021.pdf
```
or
```
git rm -rf ismb2021.pdf
```

# Python cProfiling, async and await
See [this](https://www.youtube.com/watch?v=m_a0fN48Alw).
Maybe also [this](https://www.youtube.com/watch?v=8qEnExGLZfY)

# Sublime Text 4 Python Version
See [this](https://medium.com/swlh/setting-your-python-version-in-sublime-text-8e8a305e6701). In short, Ctrl+Shift+P install `PackageResourceViewer` and 
```
Tools > Command Pallete > type 'PackageResourceViewer' > PackageResourceViewer: Open Resource > python > python.sublime build
```
change (py is python 3.9 in my system)
```
    "windows": {
        "cmd": ["py", "-u", "$file"],
    },
```
to (python is python 3.7 from anaconda in my system)
```
    "windows": {
        "cmd": ["python", "-u", "$file"],
    },

```

# Windows shortcut to folder
Hit `Win+R` and type:
```
shell:startup
%WindowsEnvVariables%
```

# mpl, plt
```
plt.show(block=False)
```

pip install --upgrade pip setuptools wheel

# Manifest.in (Python Packaging)
> https://packaging.python.org/guides/using-manifest-in/


# 2to3
```shell
2to3 --output-dir=python3-version -W -n python2-version
```

# PYPI project
Unknown location error. E.g., you need to manually create a `__init__` file in `acmsimpyv1` folder.
```ImportError: cannot import name 'acmsimpy' from 'emachinery.acmsimpyv1' (unknown location)```

# Vitual Env
```
C:\Users\horyc\AppData\Local\Programs\Python\Python39\Scripts\virtualenv .venv
cd .venv/Scripts && activate
pip install -r requirements.txt
```

# SWIFT Code
>中国银行微银行（微信）可以查询开户行
>
>https://intl.alipay.com/ihome/help/swiftcode.htm
>
>https://www2.swift.com/bsl/?bicSearch_bic=BKCHCNBJ&bicSearch_city=hangzhou&bicSearch_country=CN
>
>https://www.bankofchina.com/aboutboc/ab6/200810/t20081016_7363.html
>
> 0018657187967385 （在新加坡拨打中国银行浙大支行）
> "注意：中行的swift code只要找到省或市一级的就可以了，不用详细到各区的分支行。" quote from http://www.xineurope.com/thread-778744-1-1.html

# Anaconda 3 pkgs folder is huge
```conda clean --force-pkgs-dirs```
![[Pasted image 20210530084527.png]]

# VS Code
-Ctrl+P, open settings.json (The one in `AppData\Roaming\Code\User`), and add the following (see [this post](https://stackoverflow.com/questions/42307949/color-theme-for-vs-code-integrated-terminal#:~:text=VSCode%20comes%20with%20in%2Dbuilt,on%20mac%20and%20type%20color%20.)): 
```json
"workbench.colorCustomizations" : {
	 "editor.lineHighlightBackground": "#000000",
	 "terminal.foreground" : "#00FD61",
	 "terminal.background" : "#383737",
	 "terminalCursor.background":"#D0D0D0",
	 "terminalCursor.foreground":"#D0D0D0",
 },
 
 "editor.tokenColorCustomizations": {
	"textMateRules": [
		{
			"scope": "punctuation.definition.comment",
			"settings": {
				// "foreground": "#FFFFFF"
			}
		},
		{
			"scope": "comment.block",
			"settings": {
			 	"foreground": "#7DF9FF" //"#00DBFF" //"#EA7CB5"
			}
		},
		{
			"scope": "comment.block.documentation",
			"settings": {
				"foreground": "#FFA87C"
			}
		},
	],
},
 ```
- Shift+Alt+F, auto format your codes
- Ctrl+Alt+arrows, up and down for multi-line edit,** left and right for window split.**
- F2, Ctrl+F2, Ctrl+D, rename symbol, select all that are same, select the same one by one
- Right click on variable and click on peek can give your call hierachy which is seen in CCS.
- User Setting: search for `autoGuessEncoding` and set it to true.
- Extension: **Predawm** Theme
- Extension: **Ayu** File Icon Theme
- ~~Extension: Remote-WSL~~
- Extension: GitLens (Settings: uncheck add actions to tab bar)
- Extension: Better Comments
- Extension: Bookmark, ctrl+alt+J/K/L (might need to resolve )
![[Pasted image 20210526143452.png]]

# C2000 中断优先级和中断嵌套
In 2837xD Technical Reference Manual @Section2.4.2.2 PIE Stage, it writes:
> When the CPU receives an interrupt, it fetches the address of the ISR from the PIE. The PIE returns the vector for the lowest-numbered channel in the group that is both flagged and enabled. This gives lower-numbered interrupts a higher priority when multiple interrupts are pending.

from which we know, for example, in the following code snippet, EPWM1 will have higher priority than ECAP and EQEP interrupts.
```C
    IER |= M_INT3;  // EPWM1_INT
    IER |= M_INT4;  // ECAP1_INT
    IER |= M_INT5;  // EQEP1_INT
```
But, this does not mean the higher priority interrupt (EPWM) can interrupt the CPU when CPU is executing the ISR (Interrupt Service Routine) of the lower priority interrupt (ECAP or EQEP). It only means that the CPU will execute the EPWM ISR first if the 3 enabled interrupt flags are all set in PIE. 

See `F2837xD_defaultisr.h` for a complete list of interrupt priorities.
```c
interrupt void TIMER1_ISR(void);        // CPU Timer 1 Interrupt
interrupt void TIMER2_ISR(void);        // CPU Timer 2 Interrupt
interrupt void DATALOG_ISR(void);       // Datalogging Interrupt
interrupt void RTOS_ISR(void);          // RTOS Interrupt
interrupt void EMU_ISR(void);           // Emulation Interrupt
interrupt void NMI_ISR(void);           // Non-Maskable Interrupt
interrupt void ILLEGAL_ISR(void);       // Illegal Operation Trap
interrupt void USER1_ISR(void);         // User Defined Trap 1
interrupt void USER2_ISR(void);         // User Defined Trap 2
interrupt void USER3_ISR(void);         // User Defined Trap 3
interrupt void USER4_ISR(void);         // User Defined Trap 4
interrupt void USER5_ISR(void);         // User Defined Trap 5
interrupt void USER6_ISR(void);         // User Defined Trap 6
interrupt void USER7_ISR(void);         // User Defined Trap 7
interrupt void USER8_ISR(void);         // User Defined Trap 8
interrupt void USER9_ISR(void);         // User Defined Trap 9
interrupt void USER10_ISR(void);        // User Defined Trap 10
interrupt void USER11_ISR(void);        // User Defined Trap 11
interrupt void USER12_ISR(void);        // User Defined Trap 12
interrupt void ADCA1_ISR(void);         // 1.1 - ADCA Interrupt 1
interrupt void ADCB1_ISR(void);         // 1.2 - ADCB Interrupt 1
interrupt void ADCC1_ISR(void);         // 1.3 - ADCC Interrupt 1
interrupt void XINT1_ISR(void);         // 1.4 - XINT1 Interrupt
interrupt void XINT2_ISR(void);         // 1.5 - XINT2 Interrupt
interrupt void ADCD1_ISR(void);         // 1.6 - ADCD Interrupt 1
interrupt void TIMER0_ISR(void);        // 1.7 - Timer 0 Interrupt
interrupt void WAKE_ISR(void);          // 1.8 - Standby and Halt Wakeup Interrupt
interrupt void EPWM1_TZ_ISR(void);      // 2.1 - ePWM1 Trip Zone Interrupt
interrupt void EPWM2_TZ_ISR(void);      // 2.2 - ePWM2 Trip Zone Interrupt
interrupt void EPWM3_TZ_ISR(void);      // 2.3 - ePWM3 Trip Zone Interrupt
interrupt void EPWM4_TZ_ISR(void);      // 2.4 - ePWM4 Trip Zone Interrupt
interrupt void EPWM5_TZ_ISR(void);      // 2.5 - ePWM5 Trip Zone Interrupt
interrupt void EPWM6_TZ_ISR(void);      // 2.6 - ePWM6 Trip Zone Interrupt
interrupt void EPWM7_TZ_ISR(void);      // 2.7 - ePWM7 Trip Zone Interrupt
interrupt void EPWM8_TZ_ISR(void);      // 2.8 - ePWM8 Trip Zone Interrupt
interrupt void EPWM1_ISR(void);         // 3.1 - ePWM1 Interrupt
interrupt void EPWM2_ISR(void);         // 3.2 - ePWM2 Interrupt
interrupt void EPWM3_ISR(void);         // 3.3 - ePWM3 Interrupt
interrupt void EPWM4_ISR(void);         // 3.4 - ePWM4 Interrupt
interrupt void EPWM5_ISR(void);         // 3.5 - ePWM5 Interrupt
interrupt void EPWM6_ISR(void);         // 3.6 - ePWM6 Interrupt
interrupt void EPWM7_ISR(void);         // 3.7 - ePWM7 Interrupt
interrupt void EPWM8_ISR(void);         // 3.8 - ePWM8 Interrupt
interrupt void ECAP1_ISR(void);         // 4.1 - eCAP1 Interrupt
interrupt void ECAP2_ISR(void);         // 4.2 - eCAP2 Interrupt
interrupt void ECAP3_ISR(void);         // 4.3 - eCAP3 Interrupt
interrupt void ECAP4_ISR(void);         // 4.4 - eCAP4 Interrupt
interrupt void ECAP5_ISR(void);         // 4.5 - eCAP5 Interrupt
interrupt void ECAP6_ISR(void);         // 4.6 - eCAP6 Interrupt
interrupt void EQEP1_ISR(void);         // 5.1 - eQEP1 Interrupt
interrupt void EQEP2_ISR(void);         // 5.2 - eQEP2 Interrupt
interrupt void EQEP3_ISR(void);         // 5.3 - eQEP3 Interrupt
interrupt void SPIA_RX_ISR(void);       // 6.1 - SPIA Receive Interrupt
interrupt void SPIA_TX_ISR(void);       // 6.2 - SPIA Transmit Interrupt
interrupt void SPIB_RX_ISR(void);       // 6.3 - SPIB Receive Interrupt
interrupt void SPIB_TX_ISR(void);       // 6.4 - SPIB Transmit Interrupt
interrupt void MCBSPA_RX_ISR(void);     // 6.5 - McBSPA Receive Interrupt
interrupt void MCBSPA_TX_ISR(void);     // 6.6 - McBSPA Transmit Interrupt
interrupt void MCBSPB_RX_ISR(void);     // 6.7 - McBSPB Receive Interrupt
interrupt void MCBSPB_TX_ISR(void);     // 6.8 - McBSPB Transmit Interrupt
interrupt void DMA_CH1_ISR(void);       // 7.1 - DMA Channel 1 Interrupt
interrupt void DMA_CH2_ISR(void);       // 7.2 - DMA Channel 2 Interrupt
interrupt void DMA_CH3_ISR(void);       // 7.3 - DMA Channel 3 Interrupt
interrupt void DMA_CH4_ISR(void);       // 7.4 - DMA Channel 4 Interrupt
interrupt void DMA_CH5_ISR(void);       // 7.5 - DMA Channel 5 Interrupt
interrupt void DMA_CH6_ISR(void);       // 7.6 - DMA Channel 6 Interrupt
interrupt void I2CA_ISR(void);          // 8.1 - I2CA Interrupt 1
interrupt void I2CA_FIFO_ISR(void);     // 8.2 - I2CA Interrupt 2
interrupt void I2CB_ISR(void);          // 8.3 - I2CB Interrupt 1
interrupt void I2CB_FIFO_ISR(void);     // 8.4 - I2CB Interrupt 2
interrupt void SCIC_RX_ISR(void);       // 8.5 - SCIC Receive Interrupt
interrupt void SCIC_TX_ISR(void);       // 8.6 - SCIC Transmit Interrupt
interrupt void SCID_RX_ISR(void);       // 8.7 - SCID Receive Interrupt
interrupt void SCID_TX_ISR(void);       // 8.8 - SCID Transmit Interrupt
interrupt void SCIA_RX_ISR(void);       // 9.1 - SCIA Receive Interrupt
interrupt void SCIA_TX_ISR(void);       // 9.2 - SCIA Transmit Interrupt
interrupt void SCIB_RX_ISR(void);       // 9.3 - SCIB Receive Interrupt
interrupt void SCIB_TX_ISR(void);       // 9.4 - SCIB Transmit Interrupt
interrupt void CANA0_ISR(void);         // 9.5 - CANA Interrupt 0
interrupt void CANA1_ISR(void);         // 9.6 - CANA Interrupt 1
interrupt void CANB0_ISR(void);         // 9.7 - CANB Interrupt 0
interrupt void CANB1_ISR(void);         // 9.8 - CANB Interrupt 1
interrupt void ADCA_EVT_ISR(void);      // 10.1 - ADCA Event Interrupt
interrupt void ADCA2_ISR(void);         // 10.2 - ADCA Interrupt 2
interrupt void ADCA3_ISR(void);         // 10.3 - ADCA Interrupt 3
interrupt void ADCA4_ISR(void);         // 10.4 - ADCA Interrupt 4
interrupt void ADCB_EVT_ISR(void);      // 10.5 - ADCB Event Interrupt
interrupt void ADCB2_ISR(void);         // 10.6 - ADCB Interrupt 2
interrupt void ADCB3_ISR(void);         // 10.7 - ADCB Interrupt 3
interrupt void ADCB4_ISR(void);         // 10.8 - ADCB Interrupt 4
interrupt void CLA1_1_ISR(void);        // 11.1 - CLA1 Interrupt 1
interrupt void CLA1_2_ISR(void);        // 11.2 - CLA1 Interrupt 2
interrupt void CLA1_3_ISR(void);        // 11.3 - CLA1 Interrupt 3
interrupt void CLA1_4_ISR(void);        // 11.4 - CLA1 Interrupt 4
interrupt void CLA1_5_ISR(void);        // 11.5 - CLA1 Interrupt 5
interrupt void CLA1_6_ISR(void);        // 11.6 - CLA1 Interrupt 6
interrupt void CLA1_7_ISR(void);        // 11.7 - CLA1 Interrupt 7
interrupt void CLA1_8_ISR(void);        // 11.8 - CLA1 Interrupt 8
interrupt void XINT3_ISR(void);         // 12.1 - XINT3 Interrupt
interrupt void XINT4_ISR(void);         // 12.2 - XINT4 Interrupt
interrupt void XINT5_ISR(void);         // 12.3 - XINT5 Interrupt
interrupt void VCU_ISR(void);           // 12.6 - VCU Interrupt
interrupt void FPU_OVERFLOW_ISR(void);  // 12.7 - FPU Overflow Interrupt
interrupt void FPU_UNDERFLOW_ISR(void); // 12.8 - FPU Underflow Interrupt
interrupt void IPC0_ISR(void);          // 1.13 - IPC Interrupt 0
interrupt void IPC1_ISR(void);          // 1.14 - IPC Interrupt 1
interrupt void IPC2_ISR(void);          // 1.15 - IPC Interrupt 2
interrupt void IPC3_ISR(void);          // 1.16 - IPC Interrupt 3
interrupt void EPWM9_TZ_ISR(void);      // 2.9 - ePWM9 Trip Zone Interrupt
interrupt void EPWM10_TZ_ISR(void);     // 2.10 - ePWM10 Trip Zone Interrupt
interrupt void EPWM11_TZ_ISR(void);     // 2.11 - ePWM11 Trip Zone Interrupt
interrupt void EPWM12_TZ_ISR(void);     // 2.12 - ePWM12 Trip Zone Interrupt
interrupt void EPWM9_ISR(void);         // 3.9 - ePWM9 Interrupt
interrupt void EPWM10_ISR(void);        // 3.10 - ePWM10 Interrupt
interrupt void EPWM11_ISR(void);        // 3.11 - ePWM11 Interrupt
interrupt void EPWM12_ISR(void);        // 3.12 - ePWM12 Interrupt
interrupt void SD1_ISR(void);           // 5.9 - SD1 Interrupt
interrupt void SD2_ISR(void);           // 5.10 - SD2 Interrupt
interrupt void SPIC_RX_ISR(void);       // 6.9 - SPIC Receive Interrupt
interrupt void SPIC_TX_ISR(void);       // 6.10 - SPIC Transmit Interrupt
interrupt void UPPA_ISR(void);          // 8.15 - uPPA Interrupt
interrupt void USBA_ISR(void);          // 9.15 - USBA Interrupt
interrupt void ADCC_EVT_ISR(void);      // 10.9 - ADCC Event Interrupt
interrupt void ADCC2_ISR(void);         // 10.10 - ADCC Interrupt 2
interrupt void ADCC3_ISR(void);         // 10.11 - ADCC Interrupt 3
interrupt void ADCC4_ISR(void);         // 10.12 - ADCC Interrupt 4
interrupt void ADCD_EVT_ISR(void);      // 10.13 - ADCD Event Interrupt
interrupt void ADCD2_ISR(void);         // 10.14 - ADCD Interrupt 2
interrupt void ADCD3_ISR(void);         // 10.15 - ADCD Interrupt 3
interrupt void ADCD4_ISR(void);         // 10.16 - ADCD Interrupt 4
interrupt void EMIF_ERROR_ISR(void);    // 12.9 - EMIF Error Interrupt
interrupt void RAM_CORRECTABLE_ERROR_ISR(void);     // 12.10 - RAM Correctable
                                                    //         Error Interrupt
interrupt void FLASH_CORRECTABLE_ERROR_ISR(void);   // 12.11 - Flash Correctable
                                                    //         Error Interrupt
interrupt void RAM_ACCESS_VIOLATION_ISR(void);      // 12.12 - RAM Access
                                                    //         Violation Interrupt
interrupt void SYS_PLL_SLIP_ISR(void);              // 12.13 - System PLL Slip
                                                    //         Interrupt
interrupt void AUX_PLL_SLIP_ISR(void);              // 12.14 - Auxiliary PLL
                                                    //         Slip Interrupt
interrupt void CLA_OVERFLOW_ISR(void);              // 12.15 - CLA Overflow
                                                    //         Interrupt
interrupt void CLA_UNDERFLOW_ISR(void);             // 12.16 - CLA Underflow
                                                    //         Interrupt
```

When CPU is executing the ISR, it will stop receiving any interrupt flag. If you want the ECAP to interrupt the ISR of EPWM ISR, you need to explictly allow it in the EPWM ISR. This is called [interrupt nesting](https://software-dl.ti.com/C2000/docs/c28x_interrupt_nesting/html/index.html).
> 2.4.4.4 Nesting Interrupts
> 
> By default, interrupts do not nest. It is possible to nest and prioritize interrupts via software control of the IER and PIEIERx registers. Documentation and example code can be found in controlSUITE and on the TI Processors wiki:
http://processors.wiki.ti.com/index.php/Interrupt_Nesting_on_C28x

Here is an example of mine:
```C
__interrupt void EPWM1ISR(void){

    EPWM1IntCount += 1;

    /* Step 1. Set the global priority */
    // Set global priority by adjusting IER, so as to allow PIE group 4 to send interrupt flag to CPU stage.
    IER |= M_INT4; // Modify IER to allow CPU interrupts from PIE group 4 to be serviced. Part 1
    IER &= M_INT4; // Modify IER to allow CPU interrupts from PIE group 4 to be serviced. Part 2

    /* Step 2. Set the group priority */
    uint16_t TempPIEIER4;
    TempPIEIER4 = PieCtrlRegs.PIEIER4.all; // Save PIEIER register for later
    PieCtrlRegs.PIEIER4.all &= 0x7;        // Set group priority by adjusting PIEIER4 to allow INT4.1, 4.2, 4.3 to interrupt current ISR

    /* Step 3. Enable interrupts */
    PieCtrlRegs.PIEACK.all = 0xFFFF;      // Enable PIE interrupts by writing all 1’s to the PIEACK register
    asm("       NOP");                    // Wait at least one cycle
    EINT;                                 // Enable global interrupts by clearing INTM

    /* Step 4. Execute EPWM ISR */
    CJHMainISR();

    /* Step 5. Disable interrupts */
    DINT;

    /* Step 6. Restore the PIEIERx register */
    PieCtrlRegs.PIEIER4.all = TempPIEIER4;

    /* Step 7. Exit EPWM1 ISR */
    EPwm1Regs.ETCLR.bit.INT = 1;
    PieCtrlRegs.PIEACK.all |= PIEACK_GROUP3;
}
```

# Zotero
You can add a useful column called "extra" for typing notes.

Use +/- to expand/collapse all entries.

You can collpase abstract in info menu.

Use ctrl+shitf+A/C to get info from an entry.

# Zotero search in pdf  
[Re-index](https://forums.zotero.org/discussion/comment/43349/#Comment_43349) 


# Git: Stop tracking a file
See [stackoverflow](https://stackoverflow.com/questions/936249/how-to-stop-tracking-and-ignore-changes-to-a-file-in-git)
```shell
git rm --cached Main.pdf
```
An alternative solution is 
```shell
git update-index --assume-unchanged Main.pdf
```

# Git Warning: Change CL to CRLF
See [this](https://stackoverflow.com/questions/1967370/git-replacing-lf-with-crlf/20653073#20653073)
```
git config --global core.autocrlf false
```

# Fancy Annotation using Matplotlib
```python
ax.annotate('External Resistors Connected (0.5 $\\Omega$)', xy=(35.5, 3.65), xycoords='data',
                    xytext=(40, 3.72), size=14, 
                    arrowprops=dict(arrowstyle="-[,widthB=3.4,lengthB=0.3", connectionstyle="angle,angleA=180,angleB=90,rad=0"))
```

# JabRef Citation Key Pattern
```
Default: [year]-[auth.auth.ea]-[veryshorttitle]
Book: [year]-[auth.auth.ea]-book-[shorttitle]
```

# AxGlyph
alt+c可以增加格式刷，拉一个新的框用alt+ v刷上。

右边侧边栏可以改背景色，我喜欢改成无色，也可以修改线段类型，精确输入框宽和长和椭圆的长短轴。

按住shift拖动图形可以不变形，更多按F1看帮助文档pdf。

嫌文字太大太小，选中流程图框框，回车，找到字体设置，修改大小为16比如，然后应用到新的框框。

此外还有各种对齐的功能等等。

输入文字可以找到流程图所在的菜单的右边第二个，一个T图标，右键它定义快捷键，方便批量输入文字。

在打开的axmath窗口，善用ctrl+1234切换斜体和粗体。

还有比如ctrl+ F可以把视窗对到文件正中间，滚轮调整zoom，右键按住拖动可以平移画布。


# Least Square Snippets

OLS `D:\DrH\Codes\acmsimc_tut\exp.dat\noloadtest_exp_phaseVoltage.py`
```python
import statsmodels.api as sm
# Ordinary least squares regression
print('Start OLS...')
model_Simple = sm.OLS(y, x).fit()
print(model_Simple.summary())
print('Parameters: ', model_Simple.params)

# Add a constant term like so:
print('\n', '-'*40)
print('Start OLS with a constant term (intercept)...')
model = sm.OLS(y, sm.add_constant(x)).fit()
print(model.summary())
print('Parameters: ', model.params)

x = [0] + x.tolist() + [3000]
print(x)

plt.plot(x, np.array(x)*model_Simple.params[0], 'b--')
plt.plot(x, np.array(x)*model.params[1] + model.params[0], 'r--')

plt.xlabel('Voltage Squared [$\\rm V^2$]')
plt.ylabel('Power [W]')
plt.grid()

# plt.figure()
# plt.plot(list_volt, list_realpower, 'ko')
# plt.grid()
plt.show()
```

# Solidworks Add 3D annotation for dimension
(Original Text is missing in Earthquick)
In View-Show/Hide-
![[Pasted image 20210429090633.png]]
![[Pasted image 20210429092508.png]]

# CCS 10: Code Folding
![[Pasted image 20210619130632.png]]

# CCS 10: shortcuts
- Ctrl+O will open mini-outline window for you to navigate.
- Ctrl+G to search text and replace.

# CCS 10: no core is connected bug
(Original Text is missing in Earthquick)
![[Pasted image 20210429134716.png]]
![[Pasted image 20210429134748.png]]

# WinEdt: default PDF viewer
(Original Text is missing in Earthquick)
![[Pasted image 20210507130617.png]]



# CMake tries to compile nonexisting source file
CMake will get into error when you delete a c source file, e.g.:
`cmake mingw32-make.exe[2]: *** No rule to make target commissioning.c`

The simple solution is to modify and save CMakeLists.txt file:
> From my experience the most reliable way to retrigger the CMake configuration is to touch one of the projects `CMakeLists.txt` files.
> from: https://stackoverflow.com/questions/30949452/cmake-ninja-attempting-to-compile-deleted-cpp-file

# CMake cannot relief from a previous error
:: 我遇到了下面的错误，但是这个错误我已经修正了，而且用`gmake.exe`可以编译运行了，但是Cmake不依不饶，继续报错：
```shell
[100%] Linking C executable acmsimcv5.exe
CMakeFiles\acmsimcv5.dir/objects.a(pmsm_observer.c.obj): In function `the_active_flux_estimator':D:/DrH/Codes/emachineryTestPYPI/emachinery/acmsimcv5/c/pmsm_observer.c:820: undefined reference to `general_4states_rk4_solver'  
collect2.exe: error: ld returned 1 exit status
CMakeFiles\acmsimcv5.dir\build.make:309: recipe for target 'acmsimcv5.exe' failed     mingw32-make.exe[2]: *** [acmsimcv5.exe] Error 1
CMakeFiles\Makefile2:74: recipe for target 
'CMakeFiles/acmsimcv5.dir/all' failed      
mingw32-make.exe[1]: *** [CMakeFiles/acmsimcv5.dir/all] Error 2
Makefile:82: recipe for target 'all' failedmingw32-make.exe: *** [all] Error 2
```
比起想办法 clean 现有的 Cmake 输出文件，更有效的方法是 touch 一下 你的 CMakeList.txt 文件（就是打开按个回车保存）。

# Obsidian vs. Typora
They both support markdown and latex. 
> By the way, mubu now also supports markdown + latex.
> Jupyter lab also supports markdown + latex.

The differnce is that Obsidian can have a side-by-side preview window (as in VS Code) if you hold ctrl and left click on the preview button on the right top corner.
> see papaya电脑教室's youtube video on Obsidian.

I personally prefer how Obsidian handles it when I paste a image from the pasteboard into the document.

# Install PyTorch CUDA
I install torch from [Start Locally | PyTorch](https://pytorch.org/get-started/locally/#windows-pip) with following command:
```shell
conda install pytorch torchvision torchaudio cudatoolkit=10.1 -c pytorch
```

I encounter an intersting python package called "easyocr" and by running it, it suggests my GPU driver is too old. So, I downloaded for my GeForce 1050Ti a new driver (Game Ready Driver) from:
> https://www.nvidia.com/Download/driverResults.aspx/170799/en-us

It is extracted to:
> `D:\NVIDIA\DisplayDriver\461.40\Win10-DCH_64\International`

After it is installed, the folder `D:\NVIDIA` is gone, and I tested:
```python
>>> import torch
>>> torch.__version__
'1.7.1'
>>> torch.cuda.is_available()
True
```

Note if you have previously installed torch. After you do `conda install pytorch torchvision torchaudio cudatoolkit=10.1`, you must manually delete all name matching `/torch*` folders as well as `~orch` in python's `site-packages` folder.
Mine is at
```shell
C:\Users\horyc\Anaconda3\Lib\site-packages
```
See the answer of [srodriguez142857](https://discuss.pytorch.org/t/importerror-key-already-registered-with-the-same-priority/86271/2)
> Conclusion: This problem is due to existent library files in the _torch_ folder due to previous installations. One needs to remove them manually before reinstall again the latest version of PyTorch.

I confirm he is right, because after I do  `conda install pytorch torchvision torchaudio cudatoolkit=10.1`, I can still `import torch`. It is said torch is a module, but there is no `torch.__version__` or `torch.cuda`. This means there is a folder named `/torch` in my python import path.

# Clean up pkgs by conda and pip 
See answer by [Dr Manhattan](https://stackoverflow.com/users/3571614/dr-manhattan)
```shell
pip cache dir
pip cache purge
conda clean -a
```
For windows users, there is a more aggressive [option](https://stackoverflow.com/questions/56266229/is-it-safe-to-manually-delete-all-files-in-pkgs-folder-in-anaconda-python):
```shell
conda clean --force-pkgs-dirs
```
# Cannot load plugin fix for PySide2, PyQt5, Qt Creator
- Add a environment variable `QT_QPA_PLATFORM_PLUGIN_PATH` with value `C:\Users\horyc\anaconda3\Lib\site-packages\PyQt5\Qt\plugins\platforms`.
- Copy qwindow.dll from `C:\Users\horyc\anaconda3\Lib\site-packages\PySide2\plugins\platforms` to `C:\Users\horyc\Anaconda3\Library\plugins\platforms` ([ref](https://stackoverflow.com/questions/41994485/how-to-fix-could-not-find-or-load-the-qt-platform-plugin-windows-while-using-m))

# Implementing Donut.c in Windows 10

First you need to install ubuntu from Microsoft Store, enable WSL, restart PC and open the newly installed ubuntu terminal:
```shell
# https://stackoverflow.com/questions/62215963/how-to-install-gcc-and-gdb-for-wslwindows-subsytem-for-linux
sudo apt-get update
sudo apt-get upgrade -y
sudo apt autoremove -y
# If you see "Aborted (core dumped)"", autoremove would be helpful.
sudo apt-get install gcc -y
# -y means --assume-yes
gcc -o donut donut.c -lm
./donut
```

# CLion Setting

There is an important post to ease editing CMakeLists.txt: 

> https://stackoverflow.com/questions/33653113/how-to-add-existing-source-and-headers-file-to-the-clion-project/42043930

![clion-setting](https://github.com/horychen/snippets/blob/master/assets/images/clion-setting.png)

Shortcults
- Ctrl+Alt+S will call out the settings, locate appearance-font to change for the color scheme to monokai. See help from menu-bar for more.
- Ctrl+Shift+N is equivalent to Ctrl+P in Sublime Text--open file in project
- Ctrl+N and Ctrl+Shift+Alt+N are kind of equivalent to Ctrl+G in Sublime Text--go to any symbol
> ref: https://blog.jetbrains.com/clion/2015/03/search-and-navigation-in-clion/


# Sublime Text 3: change color for comment.block in color-syntax scheme

- Package install PackageResourceViewer.
- PackageResourceViewer-Open Resource.
	- Open C improved.tmLanguage, find the scope you want to edit, for example, comment.block for chaging multi-line comment in Clang.
	- Open `Color Scheme (Default)-Monokai..sublime-color-scheme` and add
```json
{
    "name": "CommentBlock",
    "scope": "comment.block.c",
    "foreground": "var(orange3)"
},
```
Of course you need to define what `orange3` means.

# 2837xD Dual Core Debugging
- Build both cpu01 project and cpu02 project and there will be .out file below Binaries in Project Explorer.
- Start debugging cpu01, for example.
- In Debug window (PS: there are, e.g., Expressions, Registers, Console and Debug windows.), right click on <Texas Instruments XDS2xx" USB Debug Probe_0/C28xx_CPU1> and select connect target. Then, in menu, click in order: Run-Load-Load Program-load the .out file to CPU1. Also load .out file to CPU2 this way.
- See also https://e2e.ti.com/support/microcontrollers/c2000/f/171/t/718227?LAUNCHXL-F28379D-Unable-to-download-CPU2-flash and I quote:
> 1. Build both CPU1 and CPU2 projects.
> 2. Using target ccxml, launch the configuraiton.
> 3. For CPU1, connect target. Load the CPU1 binary. CPU1 should halt in main. Do not run.
> 4. For CPU2, connet target. Load the CPU2 binary. CPU2 should halt in main.
> 5. Now run CPU1 then CPU2.


Reference:
https://blog.csdn.net/qq_42151264/article/details/106986787

# CCS 10 Encoding
It's 2021. Let's use UTF-8 for all. However, you need to do this for every project and convert GBK encoded files to UTF-8 files.
So think twice before you do it.

```
Menu-Window-Preferences-General-Workspace-Text file encoding-Other-UTF-8
```

# CCS + Sublime Text 3
ST3 likes UTF-8, but CCS would stick with GBK. Here is one workaround.

After installing [Convert​To​UTF8](https://packagecontrol.io/packages/ConvertToUTF8), ST3 can open GBK file with one extra fresh.
However, CCS with GBK as default coding cannot display UTF-8 encoded file correctly.
As a rescue, we can first open the UTF-8 file in ST3, and then select File-Set File Encoding to Chineses Simplified (GBK).
Finally, CCS can edit this file without encoding error.


# CCS 10 Emulator Firmware Warning
If you see "A firmware update is recommended for XDS200 debug probe" when debugging, try:

```
Help-Check for Updates-Emulator blah blah-Next...
```

This does not make sure that warning will go away, though.

# CCS 10 __cplusplus display bug
Window-Preferences-Show advanced settings-C/C++/Language Mappings/Add/Content type: C Source-Language: GNU C

See also screenshot: ![LanguageMappingInCCS](https://1drv.ms/u/s!AhJy_zY_lX2qgbpQJAPMCOe_kpEA_w)

Reference: https://sir.ext.ti.com/jira/browse/EXT_EP-9603

Bonus: Window-Preferences-Show advanced settings-C/C++/Editor/Folding

# Avoid putting passwords when working with Overleaf + Git
Overleaf supports Git but does not support SSH (to avoid inputing username and password). 

The following command will avoid your inputing password in 3600 sec.

```git config credential.helper "cache --timeout=3600"```

Since this command is a bit long, I use following command to recall it with WSL:

```histroy | grep credential```

# Avoid seeing ^M in Git Diff for Git-handled Files
Use \n for newline.
https://stackoverflow.com/questions/1889559/git-diff-to-ignore-m

# instaloader
A python tool to download instagram pictures.

# Steps to use Pyinstaller to create small .exe file
1. Download python installer from https://www.python.org/downloads/, don't download embeddable version--that won't work with pyinstaller even you get-pip.
2. Custom install python (only check pip) in, e.g., python37/
3. ```cd python37/Scripts```
4. ```pip install pyinstaller```
5. Download vanilla numpy ```numpy-1.18.5+vanilla-cp37-cp37m-win_amd64.whl``` here: https://www.lfd.uci.edu/~gohlke/pythonlibs/
6. In Scripts/, ```pip install numpy-1.18.5+vanilla-cp37-cp37m-win_amd64.whl```
7. In Scripts/, ```pyinstaller -F -w --onefile your-python-file.py```
8. In Scripts/dist, you can find you .exe file.
9. In my case, the .exe file built with Anaconda is over 200 MB, but now my new .exe file is only 10.9 MB.

# virtualenv
See https://www.youtube.com/watch?v=N5vscPTWKOk

In Windows, you need to copy those 4 files at:
>	D:\Users\horyc\Anaconda3\python.exe
>	
>	D:\Users\horyc\Anaconda3\python.pdb
>	
>	D:\Users\horyc\Anaconda3\pythonw.exe
>	
>	D:\Users\horyc\Anaconda3\pythonw.pdb

to:

>	D:\Users\horyc\Anaconda3\Lib\venv\scripts\nt\

Then, follow Corey's video:
```
mkdir Environments
cd Environments
virtualenv project1_env
```

Finally, instead of linux command ```source```, you need to use run the .bat file, for example:
```DOS
cd project1_env/Scripts
activate
```
In project1_env/Scripts/, type ```pip list```, you will have a clean pip list now.

With that said, you can also use WSL (Windows Subsystem for Linux) instead of cmd.exe for trying out virtualenv.
Because, the proper way to do virtual env in Windoes is to use VENV, see https://www.youtube.com/watch?v=APOPm01BVrk

By the way, for using pyinstaller to convert py to exe, don't use Anaconda. See https://stackoverflow.com/questions/48629486/how-can-i-create-the-minimum-size-executable-with-pyinstaller

# Typora: Change Width of Writing Area
> Edit-Preference-Appearance-Themes-Open Theme Folder-xxx.css-find 'max-width'-replace with following:
```css
#write {
	/*max-width: 914px;*/
	color: #333;
}
#typora-source .CodeMirror-lines {
  max-width: 1800px;
}
```
> see https://support.typora.io/Width-of-Writing-Area/

# Compressed folder name: .vscode.7z
由于每台电脑安装 gcc 等编译器的情况不同，在 acmsimc_tut 代码所在目录解压后需要修改的地方与操作步骤：
1. c_cpp_properies.json 中的 compilerPath：修改为你的 gcc.exe 所在地址
2. launch.json 中的 miDebuggerPath：修改为你的 gcc.exe 所在地址
3. tasks.json 中的 command：修改为你的 gcc.exe 所在地址
4. 完事以后，在 acmsimc_tut 代码所在目录右键用 vs code 打开当前文件夹
5. 打开 main.c，
6. 快捷键：按 ctrl+shift+b 是编译但不会运行 main.exe
7. 快捷键：按 F5 是编译 + 运行 debug

# File name: makefile 
```
# Should be equivalent to your list of C files, if you don't build selectively
SRC=$(wildcard *.c)

CFLAGS = -I. -L.

%.o : %.c
	gcc -c $(CFLAGS) $< -o $@

main: $(SRC)
	gcc -o $@ $^ $(CFLAGS)

# https://stackoverflow.com/questions/170467/makefiles-compile-all-c-files-at-once
# https://stackoverflow.com/questions/3932895/makefile-aliases/3933012#3933012
```

# File name: !C_GCC.sublime-build
```json
{
    "working_dir": "$file_path",
    "cmd": "gcc -Wall $file_name -o $file_base_name",
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "selector": "source.c",
    "variants": 
    [
        {   
        "name": "ACMSIMC_TUT",
            "shell_cmd": "gcc $file commissioning.c inverter.c controller.c observer.c -L. -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
        },

        {   
        "name": "ACMSIMC_iSMC",
            "shell_cmd": "gcc $file comm.c inverter.c controller.c observer.c -L. -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
        },

        {   
        "name": "GMAKE",
            "shell_cmd": "gmake $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
        },

        {   
        "name": "ACMSIMC_V3",
            "shell_cmd": "gcc $file dopri45.c controller/controller.c selfCommission/selfCommission.c selfCommission/Goertzel.c observerTAAO/observerTAAO.c -L. -I. -Imodeling -Icontroller -IselfCommission -IobserverTAAO -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
        },

        {   
        "name": "ACMSIMC_V4",
            "shell_cmd": "gcc $file controller/controller.c observer_FirstApproxAnderson86/observerFirstApproxAnderson86.c observer_NaturalOb/observerNatural.c selfCommission/Goertzel.c -L. -I. -Imodeling -Icontroller -Iobserver_FirstApproxAnderson86 -Iobserver_NaturalOb -IselfCommission -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
        }
    ]
}
```

# Font is lost when importing pdf to inkscape
The following batch command will convert DimensionedPMMotor.pdf to DimensionedPMMotorFontAsPath.pdf, converting text/font into path.
```
"D:\Program Files\gs\gs9.52\bin\gswin64.exe" -o DimensionedPMMotorFontAsPath.pdf -dNoOutputFonts -sDEVICE=pdfwrite DimensionedPMMotor.pdf
```
Reference: https://bugs.launchpad.net/inkscape/+bug/295564

# Git checkout a unmaned commit as a new branch
```
git checkout -b <new branch name for this commit>
```

# Revert a Git Commit that has been pushed to Remote
See https://gist.github.com/gunjanpatel/18f9e4d1eb609597c50c2118e416e6a6

If the changes are local, you may want to use ```git reset --hard 2e75f2<some commit hash>``` and ```git clean -df``` instead. See https://www.youtube.com/watch?v=FdZecVxzJbk

# OBS Studio 
Issue 1: For laptop haveing two GPUs (for me, it has one integrated from intel and one from NVDIA something with 1050Ti), if you see a black screen, you may need to 
1. Press winkey
2. Type in graphic settings
3. In Graphic settings, click Browse and locate your OBS Studio executive.
4. Click options, choose between Power saving and High performance.
For me, I use power saving to record on my PC screen and use high performance to record on an external monitor.

Issue 2: If you see "failed to open nvenc codec" and you happen to try to use integrated GPU with OBS Studio, please take a look at (this link)[https://obsproject.com/forum/threads/failed-to-open-nvenc-codec-generic-error-in-an-external-library-i-have-tried-everything.112568/]. NVDIA GPU can do hardware encoding while integrated may not be able to do exactly the same (e.g., NVENC). I fix this after reading the following from the link:
> I also had this problem. On another website, I found this can be caused by trying to use the GPU for encoding when the GPU doesn't support that encoding. Click "Settings" then select "Output". Change "Encoding" to "Software" under "Streaming" and "Recording."

# SolidWorks
1. ctrl+1: normal to plane view
2. hold right click and move for quick tool access
3. ctrl+middle wheel: move
4. alt+middle wheel: rotate
5. shift+middle wheel: zoom

Build Com Object for SolidWorks.
```
python D:\Users\horyc\Anaconda3\Lib\site-packages\win32com\client\makepy.py -v -o PySldWorks.py "D:\Program Files\SOLIDWORKS Corp\SOLIDWORKS (2)\sldworks.tlb"
```
> How to use makepy from win32com package: https://mail.python.org/pipermail/python-win32/2015-March/013426.html
> This last email reply likes refers to Joshua Redstone's Blog.
>
> Joshua Redstone's Blog shows how to look up for ByRef variable for passing to COM object: http://joshuaredstone.blogspot.com/2015/02/solidworks-macros-via-python.html
>
> pythoncom.Nothing for Callout argument in SelectByID2: https://stackoverflow.com/questions/41175007/pass-the-variable-nothing-using-pythons-win32com/61851346#61851346


# pdf2eps with crop (remove white space)
Finally I have found the correct way to crop the white space of a pdf figure produced by Python.
> Refer to:  
> https://tex.stackexchange.com/questions/20883/how-to-convert-pdf-to-eps/133239

In short, create a new batch file named "pdf2eps" for example and paste in the below content:
```
rem pdf2eps <page number> <pdf file without ext>  
echo off  
pdfcrop "%2.pdf" "%2-temp.pdf"  
pdftops -f %1 -l %1 -eps "%2-temp.pdf" "%2.eps"  
del  "%2-temp.pdf"  
```

Now change directory to the directory with the pdf file and open cmd.exe and type in:
```
pdf2eps_crop 1 <pdf-file-name-without-suffix>
```

# pdf2eps (texlive is installed)
```batch
echo off
set arg1=%1
shift
shift
pdftops %arg1%.pdf %arg1%-temp.ps
ps2eps %arg1%-temp.ps
move %arg1%-temp.eps %arg1%.eps

rem ref: https://stackoverflow.com/questions/26551/how-can-i-pass-arguments-to-a-batch-file
rem inkscape TDDA_inner_block_cn.pdf --export-eps=TDDA_inner_block_cn.eps <- font will be lost
```

# latexmk

TL;DR
```shell
latexmk -quiet -pdf -synctex=1 -pvc -view=none <tex-file-name-without-suffix>
@pause
::see https://mg.readthedocs.io/latexmk.html
```

My favorite:
```shell
latexmk -quiet -pdf -synctex=1 -pvc -view=none -jobname=./aux-files/ismb2021 ismb2021
del pdflatex*.fls
```

**If you want to use XeLaTeX, go this way**
```shell
latexmk -pdf -xelatex -synctex=1 -pvc -view=none <tex-file-name-without-suffix>
```

Using Latexmk with Overleaf: 
> https://tex.stackexchange.com/questions/518564/what-are-the-steps-for-compiling-overleaf-projects-offline-and-getting-consisten
```
:: make sure you have "latexmk" file from overleaf in the directory(https://tex.stackexchange.com/questions/518564/what-are-the-steps-for-compiling-overleaf-projects-offline-and-getting-consisten)
:: Do not use -halt-on-error or -file-line-error. No effect.

:: Option 1 (manually compile everytime)
::latexmk -pdf -synctex=1 

:: Option 2 (detect changes and compile so you must be careful now if you want to press ctrl+s)
latexmk -pdf -synctex=1 -pvc -view=none :: <- latexmk will panic if you have error with references.

:: [Important] Sometimes, compiler called with latexmk will remove the already generated .pdf file at the end of compilation and insists that there are errors (e.g., refer to bibtex's log file .blg). Searching online, people put \end{document} before \bibliographystyle command, but this is not your case. In fact, if you put your files back to overleaf, it just compiles well. In this situation, my working solution is to create a new .tex file with a different name and paste your original .tex content to the new .tex file and run ```latexmk -pdf <your-new-tex-file-name>. It works for me.```
```

Here are some examples I found online. I do not recommend to use them.
```shell
:: XeLaTeX
latexmk -pdf -e "$pdflatex=q/xelatex %O %S/" document.tex
:: https://stackoverflow.com/questions/3124273/compile-xelatex-tex-file-with-latexmk

:: preview continuously:
latexmk -pdflatex="pdflatex -synctex=1 -halt-on-error -interaction=nonstopmode" -pdf -pvc -view=none <Tex-file>

:: pdfLaTeX with synctex
latexmk -pdflatex="pdflatex -synctex=1" -pdf <tex-file-name>
```

# Inkscape tips
In order to remove white space around a figure, there are two ways. First is to save your figure as .pdf file and use "pdfcrop" in cmd.exe to crop out the white space. Second is to save it as an .eps file, but before you do "save as", you need go to File->Document Properties->Custome size->Resize page to content->Resize page to drawing or selection, and also check here Border->Show page border if you like.

# RStudio
- Tools-Code-Saving-Default text encoding: set to UTF-8

# JMAG Designer Script
Set cases via python---slip
```python
app = designer.GetApplication()
app.SetCurrentStudy(u"2D_DPNV@60Hz_Ime=13A_Ise=0A_s=Cases")
app.View().SetCurrentCase(1)
which_variable = 0
for index, slip in enumerate([1, 0.8, 0.6, 0.4, 0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.04, 0.01, 0]):
	app.GetModel(u"Motor Performance_Torque vs Speed(Slip)_13Arms").GetStudy(u"2D_DPNV@60Hz_Ime=13A_Ise=0A_s=Cases").GetDesignTable().AddCase()
	app.GetModel(u"Motor Performance_Torque vs Speed(Slip)_13Arms").GetStudy(u"2D_DPNV@60Hz_Ime=13A_Ise=0A_s=Cases").GetDesignTable().SetValue(index+1, which_variable, slip)
```
Set cases via python---current amplitude (DW_AMP is the current per torque winding rather than inverter current.)
```python
app = designer.GetApplication()
app.SetCurrentStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated")
app.View().SetCurrentCase(1)

DW_AMP = 77.3295312916975
BW_AMP = 3.96561698931782

for ind in range(20):
	app.GetModel(u"ind88888").GetStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated").GetDesignTable().AddCase()
	app.GetModel(u"ind88888").GetStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated").GetDesignTable().SetValue(ind+1, 3, DW_AMP - BW_AMP*(ind))
	app.GetModel(u"ind88888").GetStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated").GetDesignTable().SetValue(ind+1, 4, BW_AMP*(ind+1))
```

# Anaconda 3 (after installing it, I tend to do what follows)
1. Revise history.py
	```
	File "D:\Users\horyc\Anaconda3\lib\site-packages\pyreadline\lineeditor\history.py", line 82, in read_history_file
	    for line in open(filename, 'r'):
	UnicodeDecodeError: 'gbk' codec can't decode byte 0x81 in position 2260: illegal multibyte sequence
	```
	Go to line 82 of history.py, and change it to ```for line in open(filename, 'r', encoding='utf-8'):```.

2. Install control. (read: https://python-control.readthedocs.io/en/0.8.3/intro.html#installation)
	```conda install -c conda-forge control ```

3. Install pygmo via conda.
	```
	conda config --add channels conda-forge
	conda install pygmo
	```

4. pip install pyx.

5. pip install pyfemm.

6. pip install you-get.

7. Put the path of open-ssl (D:\Users\horyc\Anaconda3\pkgs\pyopenssl-19.1.0-py37_0\Library\bin) to system enviroment variable path. The path depends on Anaconda version. Mine is Anaconda 2020-03.

8. If you encounter "The procesure entry point not located" error, see https://stackoverflow.com/questions/59645179/update-anaconda-failed-entry-point-not-found 
	
	> Removed pythoncom37.dll and pywintypes37 from C:\Windows\System32.

# Change https remote to ssh remote
See https://stackoverflow.com/questions/55246165/how-to-ssh-a-git-repository-after-already-cloned-with-https

First remove old https origin, then add new ssh origin, and finally set upstream between your local branch and the remote origin branch.

```
git remote remove origin
git remote add origin git@github.com:horychen/snippets.git
git push -u origin master
git push -u origin main
git push -u origin your-other-branches
```

```git remote set-url origin user@example.com:PATH/REPOSITORY```

# My ways to use SSH with Github
> Environment: Windows, WSL
1. ```cd ~/.ssh```, make sure there are no existing files named ```id_rsa*```. If so, rm ```id_rsa*```. This is possible if you have done this before and you forget how you did it, like me.
2. ```cd ~```, ```ssh-keygen -t rsa```, press enter, enter, enter...
3. ```ssh-add -l```, if it says "The agent has no identities.", run ```ssh-add ~/.ssh/id_rsa```, and it says ```Identity added: ~/.ssh/id\_rsa (~/.ssh/id\_rsa)```. If it prompts ```no authetification agent```, you need to manually start ssh agent by ```eval $(ssh-agent -s)```.
4. Add yoru generated public key to "https://github.com/settings/keys". To attain the public key, use ```cat ~/.ssh/id_rsa.pub``` to print and copy from the terminal you are using.
5. Test it with ```ssh -T git@github.com```, it says: "Hi horychen! You've successfully authenticated, but GitHub does not provide shell access."
6. ```git remote set-url origin git@github.com:horychen/snippets.git```
7. If you want to automatically start ssh agent when you open bash, see https://stackoverflow.com/questions/18880024/start-ssh-agent-on-login/38980986
8. After you add those snippets from step 7 to .bashrc (I do not have .bash_profile), you need to restart bash or compile it by ```source ~/.bashrc``` to make it effective.
9. Now you can git pull and git push without entering your user account and password anymore for this repo.


# AutoHotkey (use ".ahk to .exe" tool to convert .ahk file to .exe file)
```
#NoEnv
#Warn
SendMode Input  
SetWorkingDir %A_ScriptDir%  
SetTitleMatchMode 2

#q:: closePythonPlot() 
closePythonPlot()
{
    isExist = 1
    while isExist
    {
        PostMessage, 0x112, 0xF060,,, Figure
        IfWinNotExist, Figure
        {
            isExist = 0
        }
    }
}

#o::  Winset, Alwaysontop, , A
```

# Code Composer Studio 9 Setting
1. Project -> Import CCS Project
2. Window -> Preferences -> General -> Content Types -> C Source File -> Default Encoding, type in UTF-8 and update, and restart CCS9.
3. Window -> Preferences -> General -> Colors and Fonts -> Text Font, select font consolas and font size of 12.
4. to be updated.

# English Windows 10 Language for Non-Unicode Programs
Winkey -> type in "region settings" -> related settings -> Additional data, time & regional settings -> Region -> Administrative tab -> Change system locale... -> Chinese (*)

# WinEdt 10.3 and SumatraPDF
- WinEdt -> Options -> Preferences -> Unicode
	- Enable UTF-8 Formart for Modes: ```*;UTF-8;EDT;INI|UNICODE;UTF-7;ACP;OEM```
	- Enable ANSI Format for Modes: ```ACP|UNICODE;UTF-8;UTF-7;OEM```
- WinEdt -> Execution Modes -> LaTeX or XeLaTeX -> Start Viewer -> Forward Search -> Use shift F8 to forward search
- SumatraPDF (version higher than 3.3.2) -> File -> Setting -> Avanced Option -> Find `EnableTeXEnhancements` -> set to `true`
- SumatraPDF -> File -> Setting -> Options -> Set inverse search command-line
	- "D:\Program Files\WinEdt Team\WinEdt 10\WinEdt.exe" -C="WinEdt 10.3" "[Open(|%f|);SelPar(%l,8);]"
- Options -> Toolbar -> 2 row Small
- Shortcuts:
	- Ctrl+Shift+Alt+right arrow = comment
	- Ctrl+Shift+H = set current directory
	- Ctrl+Shift+C = Hide output window
	- Ctrl+Enter = Auto fill
	- Shift+Enter = Auto spell
	- Ctrl+G to go to line number.
	- Ctrl+L will open .log file.
	- Right click on the editor's left margin area (there is a blue arrow there!), you can set bookmark and jump between book mark.
	- Shift+F8 is forward search (jump to pdf file) which is equivalent to double click on the editor's left margin area.
- My Preferred Font: Georgia, fontsize=14. It gives me an unknown desire to type/write.

# Sublime Text 3
## User settings
```
{
	"color_scheme": "Packages/Color Scheme - Default/Monokai.sublime-color-scheme",
	"file_exclude_patterns":
	[
		"codes/**"
	],
	"font_options":
	[
		"gdi"
	],
	"font_size": 13,
	"ignored_packages":
	[
		"Vintage"
	],
	"line_padding_bottom": -1,
	"line_padding_top": 0,
	"show_encoding": true,
	"show_legacy_color_schemes": true,
	"tabs_small": true,
	"theme": "Material Monokai.sublime-theme",
	"translate_tabs_to_spaces": true,
	"update_check": false
}
```

```
{
	"color_scheme": "Packages/Color Scheme - Default/Monokai.sublime-color-scheme",
	"file_exclude_patterns":
	[
		"dat/**",
		"emachinery/gui/",
		"cmake-build-debug/"
	],
	"font_size": 12,
	"ignored_packages":
	[
		"Vintage"
	],
	"line_padding_bottom": -1,
	"line_padding_top": 0,
	"show_encoding": true,
	"show_legacy_color_schemes": true,
	"tabs_small": true,
	// "theme": "Cyanide - Love.sublime-theme",
	"theme": "Adaptive.sublime-theme",
	"translate_tabs_to_spaces": true,
	"update_check": false,
	"caret_style": "smooth",
	"highlight_line": true,
	"overlay_scroll_bars": "enabled",
}

```

## Key bindings
```
[
    { "keys": ["ctrl+o"], "command": "show_panel", "args": {"panel": "output.exec"} },
    { "keys": ["alt+z"], "command": "unfold" },
    { "keys": ["alt+q"], "command": "unfold" },
    { "keys": ["alt+x"], "command": "fold" },
]
```

```
[
    { "keys": ["ctrl+o"], "command": "show_panel", "args": {"panel": "output.exec"} },
    { "keys": ["alt+z"], "command": "unfold" },
    { "keys": ["alt+q"], "command": "unfold" },
    { "keys": ["alt+x"], "command": "fold" },
    { "keys": ["`"], "command": "toggle_side_bar" },
]
```

Switch to header file:
`Goto > _Switch_ File > _Switch_ Header/Implementation`



## !C_GCC.sublime-build
```
{
    "working_dir": "$file_path",
    "cmd": "gcc -Wall $file_name -o $file_base_name",
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "selector": "source.c",
    "variants": 
    [
        {   
        "name": "ACMSIMC_TUT",
            "shell_cmd": "gcc $file controller.c observer.c -L. -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
            // "shell_cmd": "gcc $file controller.c observer_OmgZhang02.c observerNatural.c -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
            // "shell_cmd": "gcc $file controller.c observer.c observerTAAO.c -L. -lsatlut -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
            // "shell_cmd": "gcc $file inverter.c controller.c observer.c observerTAAO.c -L. -lsatlut -o $file_base_name && start cmd /c \"${file_path}/${file_base_name}\""
        }
    ]
}
```

## Packages
Must have:
- **Dark sidebar**: Preferences-Theme-Adaptive.sublime-theme
- *Package Control*
- *ConvertToUTF8*: This allows you to properly open files with GB2312 encoding.
- *PackageResourceViewer*
- *Outline* (Ctrl+Shfit+P type in Browse Mode, Dark mode: {"color_scheme": "Packages/Outline/outline-Dark.hidden-tmTheme"}, see https://packagecontrol.io/packages/Outline
- *SideBarEnhancements*
- *highlightwords*: Use ctrl+alt+h (Edit-HighlightWords) to temporarily highlight words, and Preferences-Package Settings-HighlightWords-SettingsUser to permanently highlight words as follows
```json
{
    // Keywords to be always highlighted, clear the list to disable it.
    // "keyword" are literally matched, and "color" refers to theme scope names.
    // "flag": 0 - regex, 1 - literal (default), 2 - regex and ignore case, 3 - literal and ignore case
    // Note that json has some special characters like '\' should be escaped.
    "permanent_highlight_keyword_color_mappings": [
        // {"keyword": "TODO", "color": "support.function"},
        {"keyword": "FIXIT .*", "color": "support.function", "flag": 2},
        {"keyword": "Note .*", "color": "support.function", "flag": 2},
    ]

}
```

Shortcuts
- CTRL+Shift+P: access to package control
- CTRL+\`: see ST's python console command
- CTRL+P: open file in project
- CTRL+R: go to symbol in current file
- CTRL+G: go to line number
- **ALT+O: switch c header and c source file**
- CTRL+ALT+Up/Down: multi-edit
- CTRL+LeftClick: multi edit
- CTRL+D: select same text
- CTRL+SHIFT+F: search in project
- CTRL+H, ALT+R: replace, toggle regex
- CTRL+SHIFT+Z: undo undo
- CTRL+K, CTRL+1: Fold by level 1
- CTRL+K, CTRL+J: unfold all
- CTRL+F2: toggle bookmark
- F2, jump to next bookmark
- Alt+-: go to last view
- CTRL+M: jump to marching bracket
- SHIFT+ALT+2: split into two views
- File-New View Into File
- CTRL+B or CTRL+SHIFT+B: Build
- **CTRL+SHIFT+R**: brings up the search panel for all indexed symbols.


Syntax Coloring:
- [PackageResourceViewer](https://stackoverflow.com/questions/32227791/syntax-coloring-in-comments-on-sublime-text-3)
- [PackageDev](http://ilkinulas.github.io/programming/2016/02/05/sublime-text-syntax-highlighting.html)
- [C Improved](https://packagecontrol.io/packages/C%20Improved)
- [Python Improved]
- [C++ (fmt)](https://android.googlesource.com/platform/external/fmtlib/+/refs/heads/master/support/C++.sublime-syntax)
- LSP


Less often used:
- BracketHighlighter
- Dayle Rees Color Schemes
- DocBlockr
- Emmt
- FileBrowser
- GitGutter
- JsPrettier
- Materialize
- Predawn
- Predawn Monokai
- SideBarTools
- SublimeLinter
- Theme - Soda
- See also https://www.youtube.com/watch?v=-6ikAMmu3Nc


HighlightWords.sublime-settings
```json
{
    // Keywords to be always highlighted, clear the list to disable it.
    // "keyword" are literally matched, and "color" refers to theme scope names.
    // "flag": 0 - regex, 1 - literal (default), 2 - regex and ignore case, 3 - literal and ignore case
    // Note that json has some special characters like '\' should be escaped.
    "permanent_highlight_keyword_color_mappings": [
        // {"keyword": "TODO", "color": "support.function"},
        {"keyword": "FIXIT .*", "color": "support.function", "flag": 2},
        // {"keyword": "Note .*", "color": "support.function", "flag": 2},
        {"keyword": "[^#]## .*", "color": "support.comment", "flag": 2},
        {"keyword": "/// .*", "color": "support.comment", "flag": 2},
    ]
}
```


# Sublime Text 3 go to variable declaration
- Download zip file from https://jaist.dl.sourceforge.net/project/ctags/ctags/5.8/
- Extract zip file and add this folder to System Environment Path
- In Sublime Text, install CTags via Package Control
- run `ctags -R --exclude=.\dat -f .tags` to create ctags file `.tags` in your c-project directory.
- In Sublime Text, right click on a variable (for example, a float variable) and "Navigate to Definition". If there are multiple definitions, select the one you want.
- In ST3, add following to Preferences-Packages Settings-CTags-Setting User
```
{

    // Additional options to pass to ctags, i.e.
    // ["--exclude=some/path", "--exclude=some/other/path", ...]
    "opts" : ["--c-kinds=+l"],

    "file_exclude_patterns": [".tags", ".tags_sorted_by_file", ".gemtags"]
}
```
