import sqlite3
from System.auth.passwords import hash
import bcrypt
from os import path

class database():
    def __init__(self):
        self.dbLocation = "System/auth/users.sqlite"
        if not path.exists(self.dbLocation):
            self.connectDB()
            self.initDB()
        else:
            self.connectDB()

    def connectDB(self):
        self.db = sqlite3.connect(self.dbLocation)
        self.cursor = self.db.cursor()

    def initDB(self):
        self.cursor.execute(
            "create table users (username text not null unique, password text not null unique)")
        self.db.commit()
        self.addUser("root", hash("root"))

    def checkUsername(self, username):
        self.cursor.execute(
            f"select rowid from users where username = '{username}'")
        dbResult = self.cursor.fetchall()
        if len(dbResult) != 0:
            return True
        else:
            return False

    def checkPassword(self, username, password):
        if self.checkUsername(username):
            self.cursor.execute(
                f"select password from users where username = '{username}'")
            dbResult = self.cursor.fetchall()
            dbResult = dbResult[0][0]
            password = password.encode("utf-8")
            dbResult = dbResult.encode("utf-8")
            if bcrypt.checkpw(password, dbResult):
                return True
            else:
                return False
        else:
            return False

    def addUser(self, username, hashedPassword):
        self.cursor.execute(
            f"insert into users values ('{username}', '{hashedPassword}')")
        self.db.commit()

    def deleteUser(self, username):
        self.cursor.execute(f"delete from users where username = '{username}'")
        self.db.commit()

    def changePassword(self, username, hashedPassword):
        self.cursor.execute(
            f"update users set password = '{hashedPassword}' where username = '{username}'")
        self.db.commit()
