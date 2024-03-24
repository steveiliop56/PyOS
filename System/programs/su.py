from System.core.database import database
from System.core.shell import setShellUsername
from getpass import getpass
import colorama as c

c.init(autoreset=True)

def run(params, username):
    username = params
    db = database()
    if username and not username.isspace():
        if db.checkPassword(username, getpass("Password: ")):
            setShellUsername(username)
        else:
            print(c.Fore.RED + "Authentication failure!")
    else:
        print(
            c.Fore.RED + f"User does not exist!")

def help():
    return "Su allows you to change your shell to other username. Usage: su username."
