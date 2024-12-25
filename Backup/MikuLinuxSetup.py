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
#right here we are putting the program title.
username = os.getlogin()
username = "/home/" + username + "/"
print(" |  \/  (_) |        ( )     | |    (_)                   / ____|    | |")
print(" | \  / |_| | ___   _|/ ___  | |     _ _ __  _   ___  __ | (___   ___| |_ _   _ _ __")
print(" | |\/| | | |/ / | | | / __| | |    | | '_ \| | | \ \/ /  \___ \ / _ \ __| | | | '_ *")
print(" | |  | | |   <| |_| | \__ \ | |____| | | | | |_| |>  <   ____) |  __/ |_| |_| | |_) |")
print(" |_|  |_|_|_|\_\*__,_| |___/ |______|_|_| |_|\__,_/_/\_\ |_____/ \___|\__|\__,_| .__/")
print("                                                                                | |")
print("Welcome! This program will set up your POP_os rice!                             |_|")
#now we start installing all the apt related programs
print("The first step: Downloading catimg so we use terminal pixels to diplay cool images 🖼️")
pause = input("Please press ENTER to continue...")
install_package('catimg')
print("")
print("Next we install neofetch 😎")
pause = input("Please press ENTER to continue...")
install_package('neofetch')
bashrcLocation = username + ".bashrc"
shutil.copyfile('bashrc', bashrcLocation)
#
#
print("")
print("You should be set up!")
chooice1 = input("Would you like to addtionally install neovim with LazyVim config? ✏️   (Y/n)")
if chooice1 == 'Y':
    print("Note: we are going to install this using Flatpak instead of the APT repository.")
    print("On POP_os, Flatpak has seem to have the more up to date and stable version of the program.")
    pause = input("Please press ENTER to continue...")
    install_flatpak('io.neovim.nvim')
    print("We are finished with nvim installation!")
chooice2 = input("It makes sence that we need a cool task manager, right? Shall we Install btop?📈 (Y/n)")
if chooice2 == 'Y':
    install_package("btop")

