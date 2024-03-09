# -*- coding: utf-8 -*-

from menu import Menu
from colorama import Fore, Back, Style, just_fix_windows_console
import os, time, webbrowser

class Start:
    def __init__(self):
        just_fix_windows_console()
        print(Fore.BLUE + Style.BRIGHT + "·▄▄▄▄  ▪  ▄▄▄  ▄▄▄▄▄ ▄· ▄▌    ▄▄▄▄·       • ▌ ▄ ·. ▄▄▄▄· ▄▄▄ .▄▄▄  \n██▪ ██ ██ ▀▄ █·•██  ▐█▪██▌    ▐█ ▀█▪▪     ·██ ▐███▪▐█ ▀█▪▀▄.▀·▀▄ █·\n" + Fore.YELLOW + Style.BRIGHT + "▐█· ▐█▌▐█·▐▀▀▄  ▐█.▪▐█▌▐█▪    ▐█▀▀█▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▪▄▐▀▀▄ \n██. ██ ▐█▌▐█•█▌ ▐█▌· ▐█▀·.    ██▄▪▐█▐█▌.▐▌██ ██▌▐█▌██▄▪▐█▐█▄▄▌▐█•█▌\n▀▀▀▀▀• ▀▀▀.▀  ▀ ▀▀▀   ▀ •     ·▀▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀·▀▀▀▀  ▀▀▀ .▀  ▀" + Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu().mainMenu()

Start()
