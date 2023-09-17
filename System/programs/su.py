from System.auth import database_checker
from System.core import shell
from getpass import getpass
from colorama import Fore

def su(username, currentusername):
    if username and not username.isspace():
        if database_checker.check_username(username) == True:
            if currentusername == "root" or database_checker.check_password(username, getpass(Fore.RESET + "Password: ")) == True:
                shell.shell(username)
            else:
                print(Fore.RED + "su: Authentication failure!" + Fore.LIGHTBLACK_EX)
        else:
            print(Fore.RED + f"su: User {username} does not exist!" + Fore.LIGHTBLACK_EX)
    else:
        print(Fore.RED + "su: No username supplied!" + Fore.LIGHTBLACK_EX)

def command_info():
    return "Su allows you to change your shell to other username. Usage: su username."