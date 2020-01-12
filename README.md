# snippets
Userful snippets

# My ways to use SSH with Github
> Environment: Windows, WSL
1. cd ~/.ssh, make sure there are no existing files named id_rsa*. If so, rm id_rsa*. This is possible if you have done this before and you forget how you did it, like me.
2. cd ~, ssh-keygen -t rsa, enter, enter, enter...
3. ssh-add -l, if it says "The agent has no identities.", run ssh-add ~/.ssh/id_rsa, is says "Identity added: ~/.ssh/id_rsa (~/.ssh/id_rsa)". If it prompts "no authetification agent", you need to manually start ssh agent by eval $(ssh-agent -s).
4. Test with ssh -T git@github.com, it says: "Hi horychen! You've successfully authenticated, but GitHub does not provide shell access."
5. Add public key to "https://github.com/settings/keys". To obtain the public key, use cat ~/.ssh/id_rsa.pub to print and copy from the terminal you are using.
6. git remote set-url origin git@github.com:horychen/snippets.git
7. If you do not want to start ssh agent everytime, see https://stackoverflow.com/questions/18880024/start-ssh-agent-on-login/38980986
8. After you add those snippets from step 7 to .bashrc (I do not have .bash_profile), you need to compile it by source ~/.bashrc.
9. Now you can git pull and git push without entering your user account and password anymore for this repo.

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
