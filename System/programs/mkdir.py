from System.core.filesystem import filesystem
import colorama as c

c.init(autoreset=True)

def run(params, username):
    fs = filesystem(username)
    if fs.path_exists(params):
        print(c.Fore.RED + "Cannot create directory! Path exists!")
    else:
        fs.make_directory(params)
        print(c.Fore.GREEN + "Directory created!")
    
def help():
    return "Create directories. Usage: mkdir somedir"