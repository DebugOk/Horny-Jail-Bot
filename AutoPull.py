from os import read
import requests
import subprocess
import time
import filecmp
import os

from requests.api import delete
URL = 'https://gitcdn.xyz/repo/DebugOk/Horny-Jail-Bot/main/HornyJailBot.py'
URL = 'https://raw.githack.com/DebugOk/Horny-Jail-Bot/main/HornyJailBot.py'

print("[Autopull] Downloading latest version")
file = requests.get(URL)
os.remove("./bot.py")
open('./bot.py', 'wb').write(file.content)
p = subprocess.Popen(['python3', 'bot.py', 'arg1', 'arg2'])
while True:
    time.sleep(15)
    print("[Autopull] Checking for new commits")
    file = requests.get(URL)
    os.remove("./temp.py")
    open('./temp.py', 'wb').write(file.content)
    if not filecmp.cmp("./temp.py","./bot.py"):
        print("[Autopull] Updating file and restarting...")
        os.remove("./bot.py")
        open('./bot.py', 'wb').write(file.content)
        p = subprocess.Popen(['python3', 'bot.py', 'arg1', 'arg2'])
    else:
        print("[Autopull] No changes found!")