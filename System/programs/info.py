from colorama import Fore
import colorama
import platform
import importlib

colorama.init(autoreset=True)

def info(command):
    print(Fore.BLUE + f"PyShell V1.0 running on {platform.system()}" + Fore.LIGHTBLACK_EX)
    if command == "":
        print(Fore.RED + "Command name required!" + Fore.LIGHTBLACK_EX)
    else:
        if command == "info":
            print(Fore.BLUE + f"{command}" + Fore.YELLOW + " - " + Fore.GREEN + f"{command_info()}" + Fore.LIGHTBLACK_EX)
        else:
            module = importlib.import_module(f"System.programs.{command}")
            run_command = getattr(module, "command_info")
            print(Fore.BLUE + f"{command}" + Fore.YELLOW + " - " + Fore.GREEN + f"{run_command()}" + Fore.LIGHTBLACK_EX)
            # except:
                #     print(Fore.RED + f"Command {command} does not have callable info!" + Fore.LIGHTBLACK_EX)         

def command_info():
    return "Gives info about a command and displays its usage. Usage: info commandname."