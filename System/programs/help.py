import platform
import colorama as c

c.init(autoreset=True)

def run(params, username):
    print(c.Fore.BLUE +
          f"PyShell V1.0 running on {platform.system()}" + c.Fore.LIGHTBLACK_EX)
    if params == "":
        print(c.Fore.RED + "Program name required!" + c.Fore.LIGHTBLACK_EX)
    else:
        module = __import__(f"System.programs.{params}", fromlist=['help'])
        print(c.Fore.BLUE + f"{params}" + c.Fore.YELLOW + " - " +
              c.Fore.GREEN + f"{module.help()}" + c.Fore.LIGHTBLACK_EX)

def help():
    return "Gives info about a command and displays its usage. Usage: help commandname."
