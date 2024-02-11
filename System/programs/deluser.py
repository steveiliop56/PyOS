from System.core.database import database
import colorama as c

c.init(autoreset=True)


def run(params, username):
    del_username = params
    db = database()
    if username == "root":
        if del_username and not del_username.isspace():
            if del_username == "root":
                print(c.Fore.RED + "You can't delete yourself!")
            else:
                if db.check_username(username):
                    db.del_user(del_username)
                    print(c.Fore.GREEN + "Username " + c.Fore.YELLOW +
                          username + c.Fore.GREEN + " deleted!")
                else:
                    print(c.Fore.LIGHTBLACK_EX + "User does not exist!")
        else:
            print(c.Fore.RED + "No username supplied!")
    else:
        print(c.Fore.RED + "Only root can delete users!")


def help():
    return "With deluser you can delete different users from the os. Usage: deluser usertodelete. Note: Only root can delete user accounts."
