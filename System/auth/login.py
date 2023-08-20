from System.auth import database_checker
from getpass import getpass

def login_screen():
    username = input("PyOS login: ")
    password = getpass("Password: ")
    if database_checker.check_username(username) == True:
        if database_checker.check_password(username, password) == True:
            return True, username
        else:
            return False
    else:
        return False