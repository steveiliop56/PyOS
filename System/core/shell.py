# Nothing here...
from System.auth import login
from System.programs import *
from System.core import commandhandler
import time
import colorama
from colorama import Fore
import readline

colorama.init(autoreset=True)

def shell(username):
    while True:
        icommand = input(Fore.RED + f"{username}" + Fore.BLUE + "@" + Fore.GREEN + "pyos: " + Fore.LIGHTBLACK_EX)
        if icommand == "":
            pass
        else:
            try:
                command, params = icommand.split(" ", 1)
            except ValueError:
                params = ""
                command = icommand
            commandhandler.handle(command, params, username)