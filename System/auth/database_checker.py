import sqlite3
from System.auth import password_hasher

db = sqlite3.connect("System/auth/credentials.db")
cursor = db.cursor()

def check_username(username):
    cursor.execute("select rowid from users where username = ?", (str(username),))
    db_result = cursor.fetchall()
    if len(db_result) == 0:
        return False
    else:
        return True

def check_password(username, password):
    if check_username(username) == True:
        cursor.execute("select rowid from users where password = ?", (str(password), ))
        db_result = cursor.fetchall()
        if len(db_result) == 0:
            return False
        else:
            return True
