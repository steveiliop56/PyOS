from System.core.database import database
from getpass import getpass


def login_screen():
    username = input("PyOS login: ")
    password = getpass("Password: ")
    db = database()
    if db.check_password(username, password) == True:
        return True, username
    else:
        return False
