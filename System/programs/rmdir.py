from System.core.filesystem import filesystem
import colorama as c

c.init(autoreset=True)

def run(params, username):
    fs = filesystem(username)
    if fs.path_exists(params):
        if fs.remove_directory(params):
            print(c.Fore.GREEN + "Directory deleted!")
        else:
            print(c.Fore.RED + "Failed to delete directory!")
    else:
        print(c.Fore.RED + "Failed to delete directory! Did you provide the correct path?")

def help():
    return "Delete directories. Usage: rmdir somedir"