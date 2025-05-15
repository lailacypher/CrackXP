#!/usr/bin/env python3
# This Script Was Made By @Laila19

import os
import sys
from time import sleep

def clear_screen():
    os.system('clear')

def display_banner():
    print('''
\033[1;35m
 ________  ________  ________  ________  ___  __       ___    ___ ________   
|\   ____\|\   __  \|\   __  \|\   ____\|\  \|\  \    |\  \  /  /|\   __  \  
\ \  \___|\ \  \|\  \ \  \|\  \ \  \___|\ \  \/  /|_  \ \  \/  / | \  \|\  \ 
 \ \  \    \ \   _  _\ \   __  \ \  \    \ \   ___  \  \ \    / / \ \   ____\
  \ \  \____\ \  \\  \\ \  \ \  \ \  \____\ \  \\ \  \  /     \/   \ \  \___|
   \ \_______\ \__\\ _\\ \__\ \__\ \_______\ \__\\ \__\/  /\   \    \ \__\   
    \|_______|\|__|\|__|\|__|\|__|\|_______|\|__| \|__/__/ /\ __\    \|__|   
                                                      |__|/ \|__|            \033[0m

 
                                                                                       
{@} Coded By Laila19                                                              {@}  
{@} Github   - https://github.com/lailacypher                                     {@}  
   

MENU  
\033[1;30m
{1} Enable monitor mode
{2} Capture wifi signal
{3} Handshake capture (Besside-ng)
{4} Handshake capture (Airodump-ng)
{5} Cracking WPA2-PSK passwords (Aircrack-Ng)
{6} Cracking WPA2-PSK passwords (Hashcat)
{7} Disable monitor mode  
\033[0;31m{8} Disclaimer
\033[0m''')

def main_menu():
    while True:
        clear_screen()
        display_banner()
        choice = input('''\033[0;32m
┌─[ Enter the your choice ]─[~]
└──╼ # \033[0m ''')
        
        if choice == '1':
            enable_monitor_mode()
        elif choice == '2':
            capture_wifi_signal()
        elif choice == '3':
            handshake_capture_besside()
        elif choice == '4':
            handshake_capture_airodump()
        elif choice == '5':
            crack_wpa_aircrack()
        elif choice == '6':
            crack_wpa_hashcat()
        elif choice == '7':
            disable_monitor_mode()
        elif choice == '8':
            show_disclaimer()
            break
        else:
            print("Invalid choice. Please try again.")
            sleep(2)

def enable_monitor_mode():
    os.system('airmon-ng')
    interface = input("Enter your interface: ")
    os.system(f'airmon-ng start {interface}')
    input("Press Enter to continue...")

def capture_wifi_signal():
    # Implement capture wifi signal functionality
    print("Starting wifi signal capture...")
    sleep(2)

def handshake_capture_besside():
    # Implement besside-ng handshake capture
    os.makedirs('/root/Desktop/handshake', exist_ok=True)
    print("Starting handshake capture with besside-ng...")
    sleep(2)

def handshake_capture_airodump():
    # Implement airodump-ng handshake capture
    os.makedirs('/root/Desktop/handshake', exist_ok=True)
    print("Starting handshake capture with airodump-ng...")
    sleep(2)

def crack_wpa_aircrack():
    # Implement aircrack-ng cracking
    print("Starting WPA2-PSK cracking with Aircrack-Ng...")
    sleep(2)

def crack_wpa_hashcat():
    # Implement hashcat cracking
    print("Starting WPA2-PSK cracking with Hashcat...")
    sleep(2)

def disable_monitor_mode():
    os.system('airmon-ng')
    interface = input("Enter your interface: ")
    os.system(f'airmon-ng stop {interface}')
    input("Press Enter to continue...")

def show_disclaimer():
    print("\033[0;31mThis tool is for educational purposes only. Any activity or activity related to the information contained herein is solely your responsibility. Developers are not responsible for any damage caused by this script.\033[0m")
    sleep(5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
