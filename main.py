from colorama import Fore, Style
import os
import csv
import base64
import string
import openpyxl
import urllib3
from requests.packages.urllib3.util.retry import Retry
import logging
import chardet
from requests.adapters import HTTPAdapter
import random
from pystyle import Colorate, Colors
from pystyle import *
from colorama import Fore, init
import subprocess
import requests

def username():
    def check_website(url):
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url}")

    username = input("send username: @ ")

    sites = [
        f"https://vk.com/{username}",
        f"https://github.com/{username}",
        f"https://t.me/{username}",
        f"https://www.tiktok.com/@{username}",
        f"https://github.com/{username}",
        f"https://www.youtube.com/{username}",
    ]

    for site in sites:
        check_website(site)
    return

encoded_password = "QW5nZWxOZXVsb3ZpbQ=="
correct_password = base64.b64decode(encoded_password).decode('utf-8')


while True:
    password_attempt = input("Введите пароль: ")
    if base64.b64decode(encoded_password).decode() == password_attempt:
        break
    else:
        print(Fore.RED + "Неверный пароль!" + Style.RESET_ALL)
        
        
def bd():
    subprocess.run(["python", "bd.py"])
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
COLOR_CODE = {
    "DARK": "\033[90m"  
}

banner = """
██████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████▓▓▓▓▓▓█████████████████████████████████████
█████████████████████████████████████████▓▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒█████████████████████████████████
████████████████████████████████████████▒▒▓▓████▓▓▓▓▓▒▒▓▒█████████████████████████████████
██████████████████████████████████████████▓▓▓▓▒▒▒▒▓▓██████████████████████████████████████
████████████████████████████▒▒▓▓▓█████████████████████████████████████████████████████████
████████████████████████████▒░░░▓█████████████████████████████████████████████████████████
████████████████████████████░░░░██████████████████████████████████████████████████████████
████████████████████████████░░▒▒██████████████████████████████████████████████████████████
███████████████████████████░░░░▓██▓████▒██████▓████▒▓███████▒▒████████████████████████████
██████████████████████████▒░░░░███░░██▒░████▓░░▒███░▒▒░░▒▓█▒░▒████████████████████████████
████████████████████████▓▒░░▒░░▓██░░▒█░░███▒░░▓░█▓░░░▓▓▓▓██▒░▒████████████████████████████
██████████████████████▓▓▒░░░▒░░▓▓█░░░█░░█░░░▒█████▓░░░▒▓███░░▒█▓▒▒████████████████████████
███████████████████████▓░░███░░██▓░░▒▒░░▒░░░█▒░░░░▓░░█████▓░░░░░▒▓████████████████████████
███████████████████████░░▓███▒░██▓▒░█░░▒██▓░░▓▓░▒██░░▓▒▒▓▓░░▒▒████████████████████████████
██████████████████████▒░▓█████▒▓██▓░█▒░▒████░░▒████▒░▒▓█▓▓▓███████████████████████████████
███████████████████████████████████████▒█████▓▒████▓▒█████████████████████████████████████
███████████████████████████████████████▓███████▓██████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████████████████
by @AngelNeulovim

        ╭────────────────────────────╮        ╭────────────────────────────╮
        │  [1] ПОИСК ПО БАЗЕ ДАННЫХ  │        │  [2]   ВЫХОД С СОФТА       │
        ╰────────────────────────────╯        ╰────────────────────────────╯








"""
print(Colorate.Horizontal(Colors.black_to_red, Center.XCenter(banner)))
while True:  
    select = input(f'{COLOR_CODE["DARK"]}[+]{COLOR_CODE["DARK"]} выберите номер функции: {COLOR_CODE["DARK"]}')
    if select == '1':
        bd()   
 
    elif select == '2':
        quit()