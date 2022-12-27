import colorama
from colorama import Fore

colorama.init(autoreset=True)

def neofetch(username):
    print(Fore.BLACK + "        #####    " + Fore.RED + f"       {username}" + Fore.BLUE + "@" + Fore.GREEN + "pyos")
    print(Fore.BLACK + "       #######    " + Fore.BLUE + "      ------------------")
    print(Fore.BLACK + "       ##"+ Fore.WHITE + "O" + Fore.BLACK + "#" + Fore.WHITE + "O" + Fore.BLACK + "##" + Fore.RED + "          OS:" + Fore.GREEN + " PyOS") 
    print(Fore.BLACK + "       #" + Fore.YELLOW + "#####" + Fore.BLACK + "#" + Fore.RED +"          Host:" + Fore.GREEN + " Python")
    print(Fore.BLACK + "     ##" + Fore.WHITE + "##" + Fore.YELLOW + "###" + Fore.WHITE + "##" + Fore.BLACK + "##" + Fore.RED + "        Kernel:" + Fore.GREEN + " pyos-8.7")
    print(Fore.BLACK + "    #" + Fore.WHITE + "##########" + Fore.BLACK + "##" + Fore.RED + "       Uptime:" + Fore.GREEN + " Who knows?")
    print(Fore.BLACK + "   #" + Fore.WHITE + "############" + Fore.BLACK + "##      " + Fore.RED + "Packages: " + Fore.GREEN + "None")
    print(Fore.BLACK + "   #" + Fore.WHITE + "############" + Fore.BLACK + "###     " + Fore.RED + "Shell: " + Fore.GREEN + "pyshell1.0")
    print(Fore.YELLOW + "  ##" + Fore.BLACK + "#" + Fore.WHITE + "###########" + Fore.BLACK + "##" + Fore.YELLOW + "#     " + Fore.RED + "Resolution: " + Fore.GREEN + "None")
    print(Fore.YELLOW + "######" + Fore.BLACK + "#" + Fore.WHITE + "#######" + Fore.BLACK +"#" + Fore.YELLOW + "######   " + Fore.RED +"Terminal: " + Fore.GREEN + "shell.py")
    print(Fore.YELLOW + "#######" + Fore.BLACK + "#" + Fore.WHITE + "#####" + Fore.BLACK + "#" + Fore.YELLOW + "#######   " + Fore.RED + "CPU: " + Fore.GREEN + "PyCPU (1) @ 0.005GHz")
    print(Fore.YELLOW + "  #####" + Fore.BLACK + "#######" + Fore.YELLOW + "#####     " + Fore.RED + "Memory: " + Fore.GREEN + "1MiB / 2MiB")