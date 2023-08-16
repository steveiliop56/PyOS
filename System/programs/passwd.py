from System.auth import password_hasher, database_checker
import sqlite3
import colorama
from colorama import Fore
from getpass import getpass

colorama.init(autoreset=True)

db = sqlite3.connect("System/auth/credentials.sqlite")
cursor = db.cursor()

def password_changer(username, skip_current):
    if database_checker.check_username(username) == True:
        print(Fore.BLUE + f"Changing password for {username}." + Fore.LIGHTBLACK_EX)
        if skip_current == True or database_checker.check_password(username, getpass("Current password: ")) == True:
            new_passwd = getpass("New password: ")
            verify = getpass("Retype new password: ")
            if new_passwd == verify:
                if new_passwd != "":
                    cursor.execute(f"update users set password = '{password_hasher.hash(new_passwd)}' where username = '{username}'")
                    db.commit()
                    print(Fore.GREEN + "passwd: password updated successfully" + Fore.LIGHTBLACK_EX)
                    return True
                else:
                    print("No password supplied!")
            else:
                print("passwd: Authentication token manipulation error \npasswd: password unchanged")
                return False
        else:
            print("No password supplied!")
    else:
        print(f"passwd: user '{username}' does not exist") 

def passwd(username, currentusername):
    if username == "":
        password_changer(currentusername, False)
    elif username != "":
        if currentusername == "root":
            password_changer(username, False)
        else:
            print(Fore.RED + f"Only root can change other account's password!" + Fore.LIGHTBLACK_EX)

def command_info():
    return "Chnage your password or change the passowrd of a user. Usage: passwd or passwd username. Note: only root can change other user's password."