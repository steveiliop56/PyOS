from System.auth import database_checker
from getpass import getpass
from colorama import Fore

def login_screen():
    username = input("PyOS login: ")
    password = getpass(Fore.RESET + "Password: ")
    if database_checker.check_username(username) == True:
        if database_checker.check_password(username, password) == True:
            return True, username
        else:
            return False
    else:
        return False