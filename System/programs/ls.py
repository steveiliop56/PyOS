from System.core.filesystem import filesystem
import colorama as c

c.init(autoreset=True)

def run(params, username):
    fs = filesystem(username)
    files = fs.getFiles()
    for i in range(len(files)):
        print(c.Fore.CYAN + files[i])

def help():
    return "List files and folders in the current directory. Usage: ls"
