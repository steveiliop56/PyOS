#!/usr/bin/python3

from System.core import shell
from System.auth import login
import colorama
from colorama import Fore

colorama.init(autoreset=True)

# Check that you are running the code directly 

if __name__ == "__main__":
    
    # Wait for user to login
    print(Fore.BLUE + "Welcome, please login!" + Fore.BLACK)
    logstats = login.login_screen()
    while list([logstats])[0] == False:
        print(Fore.RED + "Invalid username or password! Please try again." + Fore.BLACK)
        logstats = login.login_screen()

    # Activate the shell and tell it what username to use
    shell.shell(logstats[1])

