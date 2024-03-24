import colorama as c

c.init(autoreset=True)

def run(params, username):
    print(c.Fore.YELLOW + f"Have a nice day {username}!")
    exit()

def help():
    return "Safely exits the os. Usage: exit"
