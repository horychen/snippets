
WSL不支持自动检测文件变化，不论你用entr还是inotifywait。至少，entr至少支持新加文件（-d）时执行指令。
while sleep 1 ; do ls *.tex | entr -cdp cmd.exe /C z ; done
while inotifywait -e close_write BLIM_Review.tex; do cmd.exe /C z; done
while true; do ls *.tex | entr -d echo Changed; done
# Ptyhon:
when-changed BLIM_Review.tex z

gimp

# free up some space in linux
wajig large # see large installed package
sudo apt-get clean # to clears out the local repository of retrieved package files

# check directory size via shell command
ncdu
du -h --max-depth=1 | sort -hr
du -sh -- * # -s total -h human readable
du -sh -- * .* # https://unix.stackexchange.com/questions/185764/how-do-i-get-the-size-of-a-directory-on-the-command-line

fortune | cowsay | lolcat

gnome-terminal # x-server needed
    sudo apt-get install gnome-terminal (if you are running ubuntu)
    install an xserver such as xming or vcxsrv (https://sourceforge.net/projects/vcxsrv/files/latest/download)
    if gnome-terminal does not work you made need to do these steps:
    sudo apt-get install dbus-x11


tmux kill-server
ctrl+b x
ctrl+:  then type resize-pane -U/D/L/R 2
ctrl+[arrow key]
ctrl+b ""
ctrl+b %
ctrl+b d # detach
tmux new -s s_name
tmux a # attach-session
tmux attach-session -t 0
tmux ls
tmux # <=> ctrl+b
https://hackernoon.com/a-gentle-introduction-to-tmux-8d784c404340

lsb_release -a

export A=B # set environment variable from command line

ctrl+z === exit python interpreter
ctrl+d === exit
ctrl+c === interrupt 

killall firefox
watch free -h # watch repeat the command every 2 sec 

chmod 755 ./ # typucal perm for directory
chmod 644 .bashrc # typical perm for file
chmod 700 .bashrc # only me can do stuff with this file

usr grp everyone
rwx rwx rwx # rea write executable
421 421 421
 7   7   7


ls -lah

id

exit
su - molly

ls -al / > lsout.txt

less # 
more # use space bar to change page, press q to quit

cat >> temp.sh # >> is append, > is overwritten
history |
grep "git commit"
Ctrl+D
cat
bash temp.sh

rmdir
rm -r ./path/* # -recursive
man man # manual
apropos time
whatis cal
cal
which cal
sudo updatedb # update locate database
locate .bashrc
file .bashrc

You can add permission to .sh file so you do not need to type bash before .sh file any more # https://askubuntu.com/questions/38661/how-do-i-run-sh-files
sudo chmod +x /opt/scandoc.sh # change mode +x make this executable for everyone


hory@HORY-Y730:/mnt/d/973课题四$ scandoc.sh "MUSIC"
-bash: /opt/scandoc.sh: Permission denied
hory@HORY-Y730:/mnt/d/973课题四$ bash scandoc.sh "MUSIC"
Welcome to scandocs. This will search .doc AND .docx files in this directory for a given string.
Type in the text string you want to find...

source /etc/environment # build it 
nano /opt/environment --- add ":/opt" to PATH
to see ENV variables use: printenv 
use tab to fill 

# to live with bash 
alias cmd.exe dos-cmd
in cmd try type: bash -c "ls -af"
in cmd try type: wsl ls -lah
you can also type in wsl: powershell.exe subl .

sudo apt-get update && sudo apt-get install package-name
sudo apt-get upgrade # To actually upgrade your software (not "update" the lists), you execute the command



sudo apt list --installed
sudo apt remove --purge tilix # use tmux instead of tilix!

touch filename
nano ~/.bashrc
source ~/.bashrc
tree
tilix

tar -vxzf file.tar.gz
tar -vxjf 'Sublime Text 2.0.2 x64.tar.bz2'

# symbolic link
sudo ln -s Sublime\ Text\ 2/sublime_text /usr/bin/subl
sudo ln -s ./sublime_text /usr/bin/subl

There are stopped jobs
https://askubuntu.com/questions/431606/what-should-i-do-when-i-get-there-are-stopped-jobs-error


man ls # manual

man find # manual
find . -type f -iname "*.py" # insensitive to case (captical)
find . -type f -mmin +1 -mmin -100 # <1 min and >5 min
https://www.youtube.com/watch?v=KCVaNb_zOuw




Linux/Mac Tutorial: Cron Jobs - How to Schedule Commands with crontab
https://www.youtube.com/watch?v=QZJ1drMQz1A



ls -la ./codes | grep femm
-rwxrwxrwx 1 hory hory   9490 Dec 31 14:50 pyfemm_script.py

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# From https to ssh: no more password when push # https://stackoverflow.com/questions/6565357/git-push-requires-username-and-password
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
git remote set-url origin https://github.com/horychen/horychen.github.io.git # need pswd
# you can 密码被存在本地文件
git config credential.helper store
git push origin
git config --global credential.helper 'cache --timeout 7200'
# it is better to use SSH: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
ssh-keygen -t rsa -b 4096 -C "jiahao.chen@wisc.edu"
    git remote set-url origin git+ssh://github.com/horychen.github.io.git # this is wrong!
git remote set-url origin git@github.com:horychen//horychen.github.io.git # this is working! see https://help.github.com/articles/changing-a-remote-s-url/
git remote set-url origin git@github.com:horychen/blimdesign.git
# trouble-shooting: https://help.github.com/articles/error-permission-denied-publickey/

git reflog
git log
git commit --amend
git merge 

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# dpkg: yet another apt-get install
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
sudo dpkg -i diffmerge_4.2.0.*.deb

#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# d directory
# f file
# iname case in-sensitive
# mmin modified minute
# mtime modified days
# perm permission
# chown change owner
# {} placeholder for the results
# + or \; will be ok
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
find . -type d 
find . -type f
find . -type f -iname "*.bat"
find . -mmin -10
find . -mmin +10
find . -mmin +1 -mmin -5
find . -size +5M
find . -empty
find . -perm 777
find . -exec chown username:group {} +
use ls -la to check this 
find . -exec chown 775 {} +
find . -exec chown 664 {} +
find . -perm 664
find . -type f -iname "*.bat" -maxdepth 1 <- use this as a dry run before you rm files
find . -type f -name "*.jpg" -maxdepth 1 -exec rm {} +
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# Global RE Print -C 2 means Context 2 lines -A after -B before
# -w: whole word
# -i: case insensitive
# -n: line number
# -r: recursive
# -l: list match (contain the string) file
# -c: count of match
#~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
grep -inc -C 2 "savetxt" ./*/*

grep -incr -C 2 "operator*" ./

ls | grep -in -P "sub"

history | grep "git commit"

history | grep "git commit" | grep "back"

hory@HORY-Y730:/mnt/d/OneDrive - UW-Madison/b$ grep -P "\D{3}=" ./_layouts/default.html # Perl-compatable RE

history | grep -P "apt[\d\D]*install"

grep -in "Arnon*" ./matlab/modular_code/FEALib/*

grep -inr "Loss_BPMSM" ./*


use && run two commands in one line

##################################################
理解 ls -la 可以去看youtube上7个小时的Ubuntu入门到精通

BEA and Perlx.x in these folders are symbolic links. The symbolic link is another name that "points to" the real file.

The option '-l' tells the command to use a long list format. It gives back several columns wich correspond to:

1. Permissions
2. Number of hardlinks
3. File owner
4. File group
5. File size
6. Modification time
7. Filename

The first letter in the permissions(**lrwxrwxrwx**) column show the file's type. **`l` here means a link**, A 'd' means a directory and a '-' means a normal file (there are other characters, but those are the basic ones). The next nine characters are divided into 3 groups, each one a permission. Each letter in a group correspond to the read, write and execute permission, and each group correspond to the owner of the file, the group of the file and then for everyone else.

[ File type ][ Owner permissions ][ Group permissions ][ Everyone permissions ]
The characters can be one of four options:

r = read permission
w = write permission
x = execute permission
- = no permission
Finally, the "+" at the end means some extended permissions.



From the output above we can deduct a following information:
-rw-rw-r- permissions
1 : number of linked hard-links
lilo: owner of the file
lilo: to which group this file belongs to
0: size
Feb 26 07:08 modification/creation date and time
file1: file/directory name