import platform
import colorama as c

c.init(autoreset=True)

def run(params, username):
    print(c.Fore.BLUE + f"{username}" + " on PyOS " + str(platform.release()
                                                          ) + " running on " + c.Fore.RED + str(platform.system()) + ".")

def help():
    return "Gives basic info about the os. Usage: uname."
