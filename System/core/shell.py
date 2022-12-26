# Nothing here...
from System.auth import login
from System.programs import *
from System.core import commandhandler
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def shell(username):
    print(Fore.RED + "Warning: " + Fore.BLUE + "Due to a bug make sure to press space after each command if it has not any parameters.")
    while True:
        icommand = input(Fore.RED + f"{username}" + Fore.BLACK + "@" + Fore.GREEN + "pyos: " + Fore.BLACK)
        if icommand == "":
            pass
        else:
            try:
                command, params = icommand.split(" ")
            except ValueError:
                print(Fore.RED + "Sorry! At the time the shell can take one parameter.")
            else:
                print(Fore.BLUE + f"The command was {command} and the params where {params}.")
                if input(Fore.YELLOW + "Warning! Type handle to handle the command, this is a debug feature only! ") == "handle":
                    commandhandler.handle(command, params, username)
                else:
                    pass

