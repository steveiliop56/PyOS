import sqlite3
from System.programs import passwd
from System.auth import database_checker
import colorama
from colorama import Fore

colorama.init(autoreset=True)


db = sqlite3.connect("System/auth/credentials.sqlite")
cursor = db.cursor()

def deluser(username, currentusername):
    if currentusername == "root":
        if username and not username.isspace():
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
            print(Fore.RED + "deluser: No username supplied!" + Fore.LIGHTBLACK_EX)
    else:
        print(Fore.RED + "deluser: Only root can delete users!" + Fore.LIGHTBLACK_EX)

def command_info():
    return "With deluser you can delete different users from the os. Usage: deluser usertodelete. Note: Only root can delete user accounts."