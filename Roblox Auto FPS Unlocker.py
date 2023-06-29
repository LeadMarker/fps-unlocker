import colorama
from colorama import init, Fore, Back, Style
import os
import requests
import getpass
from os import system

roblox_directory = 'C:\\Users\\' + os.getlogin() + '\\AppData\\Local\\Roblox\\Versions'
JSON_FILE = 'https://raw.githubusercontent.com/LeadMarker/fps-unlocker/main/dependencies/ClientAppSettings.json'

system('title ' + 'Made by @leadmarker and @afyzone')

for filename in os.listdir(roblox_directory):
    f = os.path.join(roblox_directory, filename)
    final = f + '\ClientSettings'
    if not os.path.exists(final) and os.path.isdir(f):
        os.makedirs(final)

    if os.path.isdir(f):
        if not os.path.exists(final + '/ClientAppSettings.json'):
            r = requests.get(url = JSON_FILE)
            if r.status_code == 200:
                with open(final + '/ClientAppSettings.json', 'wb') as file:
                    file.write(r.content)

                print(Fore.GREEN + 'SUCCESS: Everything worked correctly, FPS unlocked for this version!')
            else:
                print(Fore.RED + 'ERROR: An error occured while attempting to call the URL!')
        else:
            print(Fore.BLUE + 'INFO: FPS already unlocked for this version!')

getpass.getpass(Fore.YELLOW + 'Press Enter key to exit!')
system("exit")
