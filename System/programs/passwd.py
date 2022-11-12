from System.auth import password_hasher, database_checker
import sqlite3

db = sqlite3.connect("System/auth/credentials.db")
cursor = db.cursor()

def passwd(username):
    if database_checker.check_username(username) == True:
        print(f"Changing password for {username}.")
        if database_checker.check_password(username, password_hasher.hash(input("Current password: "))) == True:
            new_passwd = password_hasher.hash(input("New password: "))
            verify = password_hasher.hash(input("Retype new password: "))
            if new_passwd == verify:
                cursor.execute("update users set password = ? where username = ?", (new_passwd, username))
                db.commit()
                print("passwd: password updated successfully")
        else:
            print("passwd: Authentication token manipulation error \npasswd: password unchanged")
    else:
        print(f"passwd: user '{username}' does not exist")
