import sqlite3
from System.programs import passwd
from System.auth import database_checker, password_hasher
import colorama
from colorama import Fore

colorama.init(autoreset=True)

db = sqlite3.connect("System/auth/credentials.db")
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
            new_passwd = password_hasher.hash(input("New password: "))
            verify = password_hasher.hash(input("Retype new password: "))
            if new_passwd == verify:
                cursor.execute(f"update users set password = '{new_passwd}' where username = '{username}'")
                db.commit()
                print("passwd: password updated successfully")
            print(f"Changing the user information for {username}\nEnter the new value, or press ENTER for the default")
            input("\tFull Name []:")
            input("\tRoom Number []:")
            input("\tWork Phone []:")
            input("\tHome Phone []:")
            input("\tOther []:")
            input("Is the information correct? [Y/n]")
    else:
        print(Fore.RED + "Only root can add users!" + Fore.LIGHTBLACK_EX)