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
        if skip_current == True or database_checker.check_password(username, getpass(Fore.RESET + "Current password: ")) == True:
            new_passwd = getpass(Fore.RESET + "New password: ")
            verify = getpass(Fore.RESET + "Retype new password: ")
            if new_passwd == verify:
                if new_passwd != "":
                    cursor.execute(f"update users set password = '{password_hasher.hash(new_passwd)}' where username = '{username}'")
                    db.commit()
                    print(Fore.GREEN + "passwd: password updated successfully" + Fore.LIGHTBLACK_EX)
                    return True
                else:
                    print("passwd: No password supplied!")
            else:
                print(Fore.RED + "passwd: Authentication token manipulation error! \npasswd: password unchanged!" + Fore.LIGHTBLACK_EX)
                return False
        else:
            print(Fore.RED + "passwd: Invalid password supplied!" + Fore.LIGHTBLACK_EX)
    else:
        print(f"passwd: user '{username}' does not exist!") 

def passwd(username, currentusername):
    if username and not username.isspace():
        if currentusername == "root":
            password_changer(username, True)
        else:
            print(Fore.RED + f"passwd: Only root can change other account's password!" + Fore.LIGHTBLACK_EX)
    else:
        password_changer(currentusername, False)

def command_info():
    return "Chnage your password or change the passowrd of a user. Usage: passwd or passwd username. Note: only root can change other user's password."