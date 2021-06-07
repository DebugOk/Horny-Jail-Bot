from os import read
import requests
import subprocess
import time
import filecmp
import os

checkingPrint = False
downloadPrint = True

from requests.api import delete
URL = 'https://raw.githack.com/DebugOk/Horny-Jail-Bot/main/HornyJailBot.py'

print("[Autopull] Downloading latest version")
file = requests.get(URL)
open('./bot.py', 'wb').write(file.content)
p = subprocess.Popen(['python3', 'bot.py', 'arg1', 'arg2'])
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
        p = subprocess.Popen(['python3', 'bot.py', 'arg1', 'arg2'])
    else:
        if checkingPrint:
            print("[Autopull] No changes found!")