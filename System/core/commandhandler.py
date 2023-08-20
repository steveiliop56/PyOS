from colorama import Fore
import colorama
import importlib

colorama.init(autoreset=True)

def handle(command, params, currentusername):
    try:
        module = importlib.import_module(f"System.programs.{command}")
        run_command = getattr(module, command)
    except:
        pass
    match command:
        case "adduser":
            run_command(params, currentusername)
        case "deluser":
            run_command(params, currentusername)
        case "passwd":
            run_command(params, currentusername)
        case "echo":
            print(params)
        case "exit":
            exit()
        case "ping":
            print(Fore.YELLOW + str(run_command(params)))
        case "neofetch":
            run_command(currentusername)
        case "uname":
            run_command(currentusername)
        case "clear":
            run_command()
        case "info":
            run_command(params)
        case "su":
            run_command(params)
        case _:
            print(Fore.RED + "CommandHandler: Command " + Fore.YELLOW + command + Fore.RED + " not found!")
