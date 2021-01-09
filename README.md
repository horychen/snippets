# Snippets
Userful snippets (keep updating).

# Avoid putting passwords when working with Overleaf + Git
Overleaf supports Git but does not support SSH (to avoid inputing username and password). 

The following command will avoid your inputing password in 3600 sec.

```git config credential.helper "cache --timeout=3600"```

Since this command is a bit long, I use following command to recall it with WSL:

```histroy | grep credential```

# Avoid seeing ^M in Git Diff for Git-handled Files
Use \n for newline.
https://stackoverflow.com/questions/1889559/git-diff-to-ignore-m

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

However, I would first make the newest commit a new branch for backup, and then checkout to the history commit that I want to revert back to such that HEAD would be pointed at this history commit and then delete the current branch, e.g., main, and make the history commit a branch named to the name of the deleted branch, which would be main.

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
Overleaf: 
> https://tex.stackexchange.com/questions/518564/what-are-the-steps-for-compiling-overleaf-projects-offline-and-getting-consisten
```
:: make sure you have "latexmk" file from overleaf in the directory(https://tex.stackexchange.com/questions/518564/what-are-the-steps-for-compiling-overleaf-projects-offline-and-getting-consisten)

:: (Optional) Renmae your .tex file to "output.tex".

:: Do not use -halt-on-error or -file-line-error. No effect.

:: Option 1
::latexmk -pdf -synctex=1 

:: Option 2 (This is my favorite)
latexmk -pdf -synctex=1 -pvc -view=none :: <- latexmk will panic if you error with references.

:: [Important] Sometimes, latexmk will remove the already generated .pdf file at the end of compilation and insists that there are errors (e.g., refer to bibtex's log file .blg). By searching online, people put \end{document} before \bibliographystyle command, but this is not your case. In fact, if you put your files back to overleaf, it just compiles really well. In this situation, my working solution is to create a new .tex file with a different name and paste your original .tex content to the new .tex file and run ```latexmk -pdf <your-new-tex-file-name>. It works for me.```
```
preview continuously:
```
latexmk -pdflatex="pdflatex -synctex=1 -halt-on-error -interaction=nonstopmode" -pdf -pvc -view=none <Tex-file>
```
pdfLaTeX with synctex
```
latexmk -pdflatex="pdflatex -synctex=1" -pdf <tex-file-name>
```
XeLaTeX 
```
latexmk -pdf -e "$pdflatex=q/xelatex %O %S/" document.tex
:: https://stackoverflow.com/questions/3124273/compile-xelatex-tex-file-with-latexmk
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

# Anaconda 3 (after installing it, I tend to do what is follows)
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
- SumatraPDF -> File -> Setting -> Options -> Set inverse search command-line
	- "D:\Program Files\WinEdt Team\WinEdt 10\WinEdt.exe" -C="WinEdt 10.3" "[Open(|%f|);SelPar(%l,8);]"
- Options -> Toolbar -> 2 row Small
- Shortcuts:
	- Ctrl+Shift+Alt+right arrow = comment
	- Ctrl+Shift+H = set current directory
	- Ctrl+Shift+C = Hide output window
	- Ctrl+Enter = Auto fill
	- Shift+Enter = Auto spell
	

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

## Key bindings
```
[
    { "keys": ["ctrl+o"], "command": "show_panel", "args": {"panel": "output.exec"} },
    { "keys": ["alt+z"], "command": "unfold" },
    { "keys": ["alt+q"], "command": "unfold" },
    { "keys": ["alt+x"], "command": "fold" },
]
```

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
- *Package Control*
- *SideBarEnhancements*
- *ConvertToUTF8*: This allows you to properly open files with GB2312 encoding.
- BracketHighlighter
- Dayle Rees Color Schemes
- DocBlockr
- Emmt
- FileBrowser
- GitGutter
- JsPrettier
- Materialize
- PackageResourceViewer
- Predawn
- Predawn Monokai
- SideBarTools
- SublimeLinter
- Theme - Soda
- *Outline* (Ctrl+Shfit+P type in Browse Mode, Dark mode: {"color_scheme": "Packages/Outline/outline-Dark.hidden-tmTheme"}, see https://packagecontrol.io/packages/Outline

