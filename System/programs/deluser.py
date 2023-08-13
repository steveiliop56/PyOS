import sqlite3
from System.programs import passwd
from System.auth import database_checker, password_hasher
import colorama
from colorama import Fore

colorama.init(autoreset=True)


db = sqlite3.connect("System/auth/credentials.db")
cursor = db.cursor()

def deluser(username, currentusername):
    global db
    global cursor
    if currentusername == "root":
        if username == "root":
            print(Fore.RED + "You can't delete yourself!" + Fore.LIGHTBLACK_EX)
        else:
            if database_checker.check_username(username) == True:
                print(f"Removing user `{username}' ...\nWarning: group `{username}' has no more members.\nDone.")
                cursor.execute(f"delete from users where username = '{username}'")
                db.commit()
            else:
                print(Fore.LIGHTBLACK_EX + "deluser: User does not exist!")
    else:
        print(Fore.RED + "Only root can delete users!" + Fore.LIGHTBLACK_EX)

def command_info():
    return "With deluser you can delete different users from the os. Usage: deluser usertodelete. Note: Only root can delete user accounts."