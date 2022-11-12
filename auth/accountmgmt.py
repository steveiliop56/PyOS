from getpass import getpass

def create_account(databse, cursor):
    print("Enter credentials to create account.\n")
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    if str(cursor.execute(f"select rowid from users where username = ?", (username,)).fetchall()).find("1") != -1:
        print("Account exists!")
    else:
        cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password}')")
        databse.commit()
        print("Account created!")
    return True

def login(cursor, deletetorf):
    print("Please login.\n")
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    cursor.execute("select rowid from users where username = ?", (username,))
    db_result = cursor.fetchall()
    if len(db_result) == 0:
        print(f"There is no account named {username}.")
        return False
    else:
        print("Username found! Checking password...")
        cursor.execute("select rowid from users where password = ?", (password, ))
        db_result = cursor.fetchall()
        if len(db_result) == 0:
            print("Invalid password!")
            return False
        else:
            print("Logged in!")
            if deletetorf == True:
                global delaccvar
                delaccvar = username
            else:
                pass
            return True

def delaccount(database, cursor):
    global delaccvar
    print("Please enter the account username and password that you want to delete.\n")
    deletecheck = login(cursor, True)
    if deletecheck == True:
        cursor.execute("delete from users where username = ?", (delaccvar, ))
        del delaccvar
        database.commit()
    print("Account deleted!")
    return True
       
def changepass(database, cursor):
    print("Not ready!")

def what(database, cursor):
    print("Welcome to pyos auth!")
    whattodo = input("Please enter login, create, changepass or delaccount: ")
    match whattodo:
        case "create":
            create_account(database, cursor)
            return True
        case "login":
            login(cursor, False)
            return True
        case "delaccount":
            delaccount(database, cursor)
            return True
        case "changepass":
            changepass(database, cursor)
            return True
        case _:
            print("Invalid option! Exiting...")
            return False



