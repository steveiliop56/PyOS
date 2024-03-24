import bcrypt
from getpass import getpass


def hash(password):
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    hash = hash.decode("utf-8")
    return hash


def new():
    password = getpass("New Password: ")
    passwordVerify = getpass("Retype password: ")
    if password == passwordVerify:
        return True, password
    else:
        return False, ""
