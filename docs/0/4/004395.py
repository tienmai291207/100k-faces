import subprocess
import os
import time

def mtt_setup(command):
    os.system("clear")
    print(f"\033[93mĐang setup: {command}\033[0m")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        pass  
commands = [
    "pkg install php -y",
    "pkg install python3 -y",
    "pkg install git -y",
    "pkg install wget -y",
    "pkg install termux-api -y",
    "pip install faker",
    "pip install rich",
    "pip install pycurl",
    "pip install bs4",
    "pip install colorama",
    "pip install pystyle",
    "pip install pyTelegramBotAPI", 
    "pip install aiohttp"
]
start_time = time.time()
for cmd in commands:
    mtt_setup(cmd)
end_time = time.time()
elapsed_time = end_time - start_time
os.system("clear")
print("\033[32mSetup thành công!")
print(f"\033[37mThời gian setup: {elapsed_time:.2f} giây")
print("Group 1: https://t.me/nolow_2k7")
print("Group 2: https://t.me/pulfsharemodchat")
print("Created by ᴍʀ ᴄs 🌷")
subprocess.run(["termux-open-url", "https://t.me/nolow_2k7"])
