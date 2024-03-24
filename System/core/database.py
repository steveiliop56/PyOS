import sqlite3
from System.auth.passwords import hash
import bcrypt
from os import path

class database():
    def __init__(self):
        self.db_location = "System/auth/users.sqlite"
        if not path.exists(self.db_location):
            self.connect_db()
            self.init_db()
        else:
            self.connect_db()

    def connectDB(self):
        self.db = sqlite3.connect(self.db_location)
        self.cursor = self.db.cursor()

    def initDB(self):
        self.cursor.execute(
            "create table users (username text not null unique, password text not null unique)")
        self.db.commit()
        self.add_user("root", hash("root"))

    def checkUsername(self, username):
        self.cursor.execute(
            f"select rowid from users where username = '{username}'")
        db_result = self.cursor.fetchall()
        if len(db_result) != 0:
            return True
        else:
            return False

    def checkPassword(self, username, password):
        if self.check_username(username):
            self.cursor.execute(
                f"select password from users where username = '{username}'")
            db_result = self.cursor.fetchall()
            db_result = db_result[0][0]
            password = password.encode("utf-8")
            db_result = db_result.encode("utf-8")
            if bcrypt.checkpw(password, db_result):
                return True
            else:
                return False
        else:
            return False

    def addUser(self, username, hashed_password):
        self.cursor.execute(
            f"insert into users values ('{username}', '{hashed_password}')")
        self.db.commit()

    def deleteUser(self, username):
        self.cursor.execute(f"delete from users where username = '{username}'")
        self.db.commit()

    def changePassword(self, username, new_hashed_password):
        self.cursor.execute(
            f"update users set password = '{new_hashed_password}' where username = '{username}'")
        self.db.commit()
