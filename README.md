# Snippets
Userful snippets

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

# LaTeX
latexmk -pdflatex="pdflatex -file-line-error -synctex=1" -pdf digest
latexmk -pdf -e "$pdflatex=q/xelatex %O %S/" document.tex
:: https://stackoverflow.com/questions/3124273/compile-xelatex-tex-file-with-latexmk

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
- Package Control
- PackageResourceViewer
- Predawn
- Predawn Monokai
- SideBarEnhancements
- SideBarTools
- SublimeLinter
- Theme - Soda
