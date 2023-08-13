from System.programs import adduser, deluser, passwd, ping, neofetch, uname, clear
from colorama import Fore
import colorama
colorama.init(autoreset=True)

def handle(command, params, currentusername):
    match command:
        case "adduser":
            adduser.adduser(params, currentusername)
        case "deluser":
            deluser.deluser(params, currentusername)
        case "passwd":
            passwd.passwd(params, currentusername)
        case "echo":
            print(params)
        case "exit":
            exit()
        case "ping":
            print(Fore.YELLOW + str(ping.ping(params)))
        case "neofetch":
            neofetch.neofetch(currentusername)
        case "uname":
            uname.uname(currentusername)
        case "clear":
            clear.clear()
        case _:
            print(Fore.RED + "CommandHandler: Command " + Fore.YELLOW + command + Fore.RED + " not found!")
