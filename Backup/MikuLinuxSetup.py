#!/usr/bin/env python3
import subprocess # to run O.S.commands
import os
import sys

#defining the funtions
def install_package(package_name):
    try:
        #subprocess.run(['sudo', 'apt', 'install', package_name, '-y'], check=True)
        subprocess.run(['sudo', 'apt', 'install', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def install_flatpak(package_name):
    try:
        #subprocess.run(['sudo', 'apt', 'install', package_name, '-y'], check=True)
        subprocess.run(['sudo', 'apt', 'install', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

#right here we are putting the program title.
print(" |  \/  (_) |        ( )     | |    (_)                   / ____|    | |")
print(" | \  / |_| | ___   _|/ ___  | |     _ _ __  _   ___  __ | (___   ___| |_ _   _ _ __")
print(" | |\/| | | |/ / | | | / __| | |    | | '_ \| | | \ \/ /  \___ \ / _ \ __| | | | '_ *")
print(" | |  | | |   <| |_| | \__ \ | |____| | | | | |_| |>  <   ____) |  __/ |_| |_| | |_) |")
print(" |_|  |_|_|_|\_\*__,_| |___/ |______|_|_| |_|\__,_/_/\_\ |_____/ \___|\__|\__,_| .__/")
print("                                                                                | |")
print("Welcome! This program will set up your POP_os rice!                             |_|")
#now we start
print("The first step: Downloading catimg so we use terminal pixels to desplay cool images 🖼️")
install_package('catimg')
print("Next we install neofetch 😎")
pause = input("Please press ENTER to continue...")
install_package('neofetch')
print("It makes sence that we need a cool task manager, right? gotta install btop!📈")
pause = input("Please press ENTER to continue...")
install_package('neofetch')
print("Next we install neovim 📝")
print("Please note: we are going to install this using Flatpak instead of the APT repository.")
print("On POP_os, Flatpak has seem to have the more up to date and stable version of the program.")
pause = input("Please press ENTER to continue...")
#install_flatpak('neovim')
