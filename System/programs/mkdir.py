from System.core.filesystem import filesystem
import colorama as c

c.init(autoreset=True)

def run(params, username):
    fs = filesystem(username)
    if fs.pathExists(params):
        print(c.Fore.RED + "Cannot create directory! Path exists!")
    else:
        if fs.makeDirectory(params):
            print(c.Fore.GREEN + "Directory created!")
        else:
            print(c.Fore.RED + "You won't exploit me!")
    
def help():
    return "Create directories. Usage: mkdir somedir"