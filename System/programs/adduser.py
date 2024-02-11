from System.core.database import database
from System.auth.passwords import hash, new
import colorama as c

c.init(autoreset=True)


def run(params, username):
    new_username = params
    db = database()
    if username == "root":
        if username and not username.isspace():
            if db.check_username(new_username):
                print(c.Fore.RED + f"Username {new_username} already exists!")
            else:
                print(c.Fore.BLUE +
                      f"Adding new user {new_username}...")
                ok, passwd = new()
                tries = 0
                while not ok:
                    tries += 1
                    if tries > 3:
                        print(
                            c.Fore.RED + "Password limit reached! Using pyos...")
                        passwd = "pyos"
                        ok = False
                    print(
                        c.Fore.RED + "Passwords do not match! Please try again!")
                    ok, passwd = new()
                db.add_user(new_username, hash(passwd))
                print(c.Fore.GREEN + "Username " + c.Fore.YELLOW +
                      new_username + c.Fore.GREEN + " added!")
        else:
            print(c.Fore.RED + "The username cannot be empty!")
    else:
        print(c.Fore.RED + "Only root can add new users!")


def help():
    return "With adduser you can create new user accounts that can be used in the os. Usage: adduser username. Note: Only root can create user accounts."
