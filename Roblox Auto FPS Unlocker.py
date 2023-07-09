from colorama import Fore
import os
import requests
import getpass

roblox_directory = os.path.isdir('C:\\Users\\' + os.getlogin() + '\\AppData\\Local\\Roblox') and os.path.isdir('C:\\Users\\' + os.getlogin() + '\\AppData\\Local\\Roblox\\Versions') and 'C:\\Users\\' + os.getlogin() + '\\AppData\\Local\\Roblox\\Versions' or os.path.isdir('C:\\Program Files (x86)\\Roblox') and os.path.isdir('C:\\Program Files (x86)\\Roblox\\Versions') and 'C:\\Program Files (x86)\\Roblox\\Versions'
JSON_FILE = 'https://raw.githubusercontent.com/LeadMarker/fps-unlocker/main/dependencies/ClientAppSettings.json'

os.system('title ' + 'Made by @leadmarker and @afyzone')

for filename in os.listdir(roblox_directory):
    final = os.path.join(roblox_directory, filename) + '\ClientSettings'
    
    if not os.path.isdir(os.path.join(roblox_directory, filename)): continue
    if not os.path.exists(final): os.makedirs(final)

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
os.system("exit")
