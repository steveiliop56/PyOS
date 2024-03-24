from System.auth.passwords import hash, new
from System.core.database import database
from getpass import getpass
import colorama as c

c.init(autoreset=True)

def run(params, username):
    db = database()
    if params == "":
        print(c.Fore.BLUE + f"Changing password for yourself...")
        if db.checkPassword(username, getpass("Enter current password: ")):
            ok, passwd = new()
            if ok:
                db.changePassword(username, hash(passwd))
                print(c.Fore.GREEN + "Password updated!")
            else:
                print(c.Fore.RED + "Passwords do not match!")
        else:
            print(c.Fore.RED + "Authentication failed!")
    else:
        if username == "root":
            print(c.Fore.BLUE + f"Changing password for username {params}...")
            if db.checkUsername(params):
                ok, passwd = new()
                if ok:
                    db.changePassword(params, hash(passwd))
                    print(c.Fore.GREEN + "Password updated!")
                else:
                    print(c.Fore.RED + "Passwords do not match!")
            else:
                print(c.Fore.RED + f"Cannot find user {params}!")
        else:
            print(c.Fore.RED + "Only root can change other user's passwords!")

def help():
    return "Chnage your password or change the passowrd of a user. Usage: passwd or passwd username. Note: only root can change other user's password."
