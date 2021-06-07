from os import read
import requests
import subprocess
import time
import filecmp
import os
import sys

checkingPrint = False
downloadPrint = True
shouldSelfUpdate = True

from requests.api import delete
URL = 'https://raw.githack.com/DebugOk/Horny-Jail-Bot/main/HornyJailBot.py'
URLSelf = 'https://raw.githack.com/DebugOk/Horny-Jail-Bot/main/Main.py'

print("[Autopull] Downloading latest version")
if shouldSelfUpdate:
    print("[Autopull] Also checking for self updates")
file = requests.get(URL)
open('./bot.py', 'wb').write(file.content)
p = subprocess.Popen(['python3', 'bot.py'])
while True:
    time.sleep(120)
    if checkingPrint:
        print("[Autopull] Checking for new commits")
    file = requests.get(URL)
    open('./temp.py', 'wb').write(file.content)
    if not filecmp.cmp("./temp.py","./bot.py"):
        if downloadPrint:
            print("[Autopull] Updating file and restarting...")
        open('./bot.py', 'wb').write(file.content)
        p = subprocess.Popen(['python3', 'bot.py'])
    else:
        if checkingPrint:
            print("[Autopull] No changes found")
    if shouldSelfUpdate:
        file = requests.get(URLSelf)
        open('./tempself.py', 'wb').write(file.content)
        if not filecmp.cmp("./tempself.py","./Main.py"):
            if downloadPrint:
                print("[Autopull] Updating self and fully restarting...")
            open('./Main.py', 'wb').write(file.content)
            sys.exit()