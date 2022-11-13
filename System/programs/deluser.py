import sqlite3
from System.programs import passwd
from System.auth import database_checker, password_hasher

db = sqlite3.connect("System/auth/credentials.db")
cursor = db.cursor()

def deluser(username):
    global db
    global cursor
    if database_checker.check_password(username, password_hasher.hash(input(f"Enter password to delete {username}: "))) == True:
        print(f"Removing user `{username}' ...\nWarning: group `{username}' has no more members.\nDone.")
        cursor.execute(f"delete from users where username = '{username}'")
        db.commit()
    else:
        print("deluser: Authentication token manipulation error \ndeluser: user undeleted")