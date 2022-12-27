from System.programs import adduser, deluser, passwd, ping, neofetch, uname, clear
from colorama import Fore
import colorama
colorama.init(autoreset=True)

def handle(command, params, currentusername):
    match command:
        case "adduser":
            print("Executing adduser...")
            adduser.adduser(params, currentusername)
        case "deluser":
            print("Executing deluser...")
            deluser.deluser(params, currentusername)
        case "passwd":
            print("Executing passwd..")
            passwd.passwd(params, currentusername)
        case "echo":
            print(params)
        case "exit":
            print("Executing exit...")
            exit()
        case "ping":
            print("Executig ping...")
            print(Fore.YELLOW + str(ping.ping(params)))
        case "neofetch":
            print("Executing neofetch...")
            neofetch.neofetch(currentusername)
        case "uname":
            print("Executing uname...")
            uname.uname(currentusername)
        case "clear":
            print("Executing clear...")
            clear.clear()
        case _:
            print(Fore.RED + "CommandHandler: Command " + Fore.YELLOW + command + Fore.RED + " not found!")
