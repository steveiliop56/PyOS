# Nothing here...
from System.auth import login
from System.programs import *
from System.core import commandhandler
import time
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def shell(username):
    while True:
        icommand = input(Fore.RED + f"{username}" + Fore.BLUE + "@" + Fore.GREEN + "pyos: " + Fore.BLACK)
        if icommand == "":
            pass
        else:
            try:
                command, params = icommand.split(" ", 1)
            except ValueError:
                if input(Fore.YELLOW + "Warning! Type h to handle the command, this is a debug feature only! ") == "h":
                    commandhandler.handle(icommand, "", username)
                else:
                    pass           
            else:
                print(Fore.BLUE + f"The command was {command} and the params where {params}.")
                if input(Fore.YELLOW + "Warning! Type h to handle the command, this is a debug feature only! ") == "h":
                    commandhandler.handle(command, params, username)
                else:
                    pass

