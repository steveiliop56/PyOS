import bcrypt
from getpass import getpass


def hash(password):
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    hash = hash.decode("utf-8")
    return hash


def new():
    passwd = getpass("New Password: ")
    passwd_verify = getpass("Retype password: ")
    if passwd == passwd_verify:
        return True, passwd
    else:
        return False, ""
