from System.auth import database_checker, password_hasher

def login_screen():
    username = input("PyOS login: ")
    password = password_hasher.hash(input("Password: "))
    if database_checker.check_username(username) == True:
        if database_checker.check_password(username, password) == True:
            return True
    else:
        return False