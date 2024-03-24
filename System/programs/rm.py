from System.core.filesystem import filesystem
import colorama as c

c.init(autoreset=True)

def run(params, username):
    fs = filesystem(username)
    if not fs.deleteFile(params):
        print(c.Fore.RED + "Failed to delete file. Is the path correct?")
    else:
        print(c.Fore.GREEN + "File deleted!")

def help():
    return "Delete a file. Usage: rm file.txt"
