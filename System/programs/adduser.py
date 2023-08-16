import sqlite3
from System.programs import passwd
from System.auth import database_checker, password_hasher
import colorama
from colorama import Fore

colorama.init(autoreset=True)

db = sqlite3.connect("System/auth/credentials.sqlite")
cursor = db.cursor()

def adduser(username, currenusername):
    global db
    global cursor
    if currenusername == "root":
        print(Fore.BLUE + f"Adding user '{username}'" + Fore.LIGHTBLACK_EX)
        if database_checker.check_username(username) == True:
            print(Fore.RED + f"adduser: The user `{username}' already exists." + Fore.LIGHTBLACK_EX)
        else:
            cursor.execute(f"insert into users values ('{username}', 'userpass')")
            print(f"Adding new group `{username}' (1001) ...\nAdding new user `{username}' (1001) with group `{username}' ..\nCreating home directory `/home/{username}' ...\nCopying files from `/etc/skel' ...'.")
            cursor.execute(f"update users set password = '' where username = '{username}'")
            db.commit()
            while passwd.password_changer(username, True) == False:
                print(Fore.RED + "Sorry, passwords do not match." + Fore.LIGHTBLACK_EX)
                if input("Try again? [y/N] ").find("y") != -1:
                    break 
            print(f"Changing the user information for {username}\nEnter the new value, or press ENTER for the default")
            input("\tFull Name []:")
            input("\tRoom Number []:")
            input("\tWork Phone []:")
            input("\tHome Phone []:")
            input("\tOther []:")
            input("Is the information correct? [Y/n]")
    else:
        print(Fore.RED + "Only root can add users!" + Fore.LIGHTBLACK_EX)

def command_info():
    return "With adduser you can create new user accounts that can be used in the os. Usage: adduser username. Note: Only root can create user accounts."