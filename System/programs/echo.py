from System.core.filesystem import filesystem
import colorama as c

c.init(autoreset=True)

def run(params, username):
    if params.find(" > ") != -1:
        fs = filesystem(username)
        content = params[:params.index(" > ")]
        filename = params.split(" ")[-1]
        print(filename)
        try:
            path = filename[:filename.index("/")]
            filename = path[-1]
            if not fs.createFile(filename, content, path):
                print(c.Fore.RED + "You won't exploit me!")
        except:
            if not fs.createFile(filename, content):
                print(c.Fore.RED + "You won't exploit me!")
    else:
        print(c.Fore.BLUE + params)

def help():
    return "Print something to the console or write to a file. Usage: echo Hello world or echo Hello World > somefile.txt"
