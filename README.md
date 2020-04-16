# Snippets
Userful snippets

# Rstudio
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
Set cases via python---current amplitude
```python
# -*- coding: utf-8 -*-
app = designer.GetApplication()
app.SetCurrentStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated")
app.View().SetCurrentCase(1)

DW_AMP = 77.3295312916975
BW_AMP = 3.96561698931782

for ind in range(20):
	app.GetModel(u"ind88888").GetStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated").GetDesignTable().AddCase()
	app.GetModel(u"ind88888").GetStudy(u"ind88888Tran2TSS-ForceCapabilityTest-Rated").GetDesignTable().SetValue(ind+1, 3, DW_AMP - BW_AMP*0.5*(ind+1))
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

# LaTeXmk
my favorite:
```
latexmk -pdflatex="pdflatex -file-line-error -synctex=1 -halt-on-error -sleep=1 -interaction=nonstopmode" -pdf -pvc -view=none <Tex-file>
```
pdfLaTeX with synctex
```
latexmk -pdflatex="pdflatex -file-line-error -synctex=1" -pdf <tex-file-name>
```
XeLaTeX 
```
latexmk -pdf -e "$pdflatex=q/xelatex %O %S/" document.tex
:: https://stackoverflow.com/questions/3124273/compile-xelatex-tex-file-with-latexmk
```

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
- BracketHighlighter
- Dayle Rees Color Schemes
- DocBlockr
- Emmt
- FileBrowser
- GitGutter
- JsPrettier
- Materialize
- *Package Control*
- PackageResourceViewer
- Predawn
- Predawn Monokai
- *SideBarEnhancements*
- SideBarTools
- SublimeLinter
- Theme - Soda
- *Outline* (Ctrl+Shfit+P type in Browse Mode, Dark mode: {"color_scheme": "Packages/Outline/outline-Dark.hidden-tmTheme"}, see https://packagecontrol.io/packages/Outline

