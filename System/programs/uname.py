import platform
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def uname(username):
    print(Fore.BLUE + f"{username}" + " on PyOS " + str(platform.release()) + " running on " + Fore.RED + str(platform.system()) + ".")

uname 