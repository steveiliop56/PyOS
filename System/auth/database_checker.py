import sqlite3
from System.auth import password_hasher

db = sqlite3.connect("System/auth/credentials.db")
cursor = db.cursor()

def check_username(username):
    cursor.execute(f"select rowid from users where username = '{username}'")
    db_result = cursor.fetchall()
    if len(db_result) == 0:
        return False
    else:
        return True

def check_password(username, password):
    if check_username(username) == True:
        cursor.execute(f"select password from users where username = '{username}'")
        db_result = cursor.fetchall()
        if str(db_result).find(str(password)) != -1:
            return True
        else:
            return False
            
