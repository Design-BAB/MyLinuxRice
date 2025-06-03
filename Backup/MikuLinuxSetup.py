#Author: DesignBAB
#Date: 10-20-24

#!/usr/bin/env python3
import subprocess # to run O.S.commands
import os
import sys
import shutil

#defining the funtions
def install_package(package_name):
    try:
        subprocess.run(['sudo', 'apt', 'install', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def install_flatpak(package_name):
    try:
        subprocess.run(['sudo', 'flatpak', 'install', 'flathub', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def strip_replace(file1, file2):
    shutil.copyfile(file1, file2)

def install_lazy():
    try:
        subprocess.run(['sudo', 'git', 'clone', 'https://github.com/LazyVim/starter', '~/.config/nvim'], check=True)    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def pause():
    pause = input("Please press ENTER to continue...")

#right here we are putting the program title.
username = os.getlogin()
username = "/home/" + username + "/"
#this is my test
# Replace file contents with a new string

bashrcString = """# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
        # We have color support; assume it's compliant with Ecma-48
        # (ISO/IEC-6429). (Lack of such support is extremely rare, and such
        # a case would tend to support setf rather than setaf.)
        color_prompt=yes
    else
        color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\\u@\\h:\\w\\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\\[\\e]0;${debian_chroot:+($debian_chroot)}\\u@\\h: \\w\\a\\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e 's/^\\s*[0-9]\\+\\s*//;s/[;&|]\\s*alert$//')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

alias nvim='flatpak run io.neovim.nvim'
neofetch --sixel
. "$HOME/.cargo/env"
"""

print(" |  \/  (_) |        ( )     | |    (_)                   / ____|    | |")
print(" | \  / |_| | ___   _|/ ___  | |     _ _ __  _   ___  __ | (___   ___| |_ _   _ _ __")
print(" | |\/| | | |/ / | | | / __| | |    | | '_ \| | | \ \/ /  \___ \ / _ \ __| | | | '_ *")
print(" | |  | | |   <| |_| | \__ \ | |____| | | | | |_| |>  <   ____) |  __/ |_| |_| | |_) |")
print(" |_|  |_|_|_|\_\*__,_| |___/ |______|_|_| |_|\__,_/_/\_\ |_____/ \___|\__|\__,_| .__/")
print("                                                                                | |")
print("Welcome! This program will set up your POP_os rice!                             |_|")
#now we start installing all the apt related programs
print("The first step: Downloading catimg so we use terminal pixels to diplay cool images 🖼️")
pause()
install_package('catimg')
print("")
print("Next we install neofetch 😎")
pause()
install_package('neofetch')
print("We will do a backup for bashrc just in case in its' same file location")
bashrcLocation = username + ".bashrc"
shutil.copy(bashrcLocation, bashrcLocation + ".bak")
with open(bashrcLocation, "w") as file:
    file.write(bashrcString)
#
#
print("")
print("You should be set up!")
chooice1 = input("Would you like to addtionally install neovim with LazyVim config? ✏️   (Y/n)")
if chooice1 == 'Y':
    print("Note: we are going to install this using Flatpak instead of the APT repository.")
    print("On POP_os, Flatpak has seem to have the more up to date and stable version of the program.")
    pause()
    install_flatpak('io.neovim.nvim')
    print("We are finished with nvim installation!")
chooice2 = input("It makes sence that we need a cool task manager, right? Shall we Install btop?📈 (Y/n)")
if chooice2 == 'Y':
    install_package("btop")

