import sqlite3
from System.auth import password_hasher
import bcrypt

db = sqlite3.connect("System/auth/credentials.sqlite")
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
        db_result = db_result[0][0]
        password = password.encode("utf-8")
        db_result = db_result.encode("utf-8")
        if bcrypt.checkpw(password, db_result) == True:
            return True
        else:
            return False
            
