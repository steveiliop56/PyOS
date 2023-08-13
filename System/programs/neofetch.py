import colorama
from colorama import Fore

colorama.init(autoreset=True)

def neofetch(username):
    print(Fore.LIGHTBLACK_EX + "        #####    " + Fore.RED + f"       {username}" + Fore.BLUE + "@" + Fore.GREEN + "pyos")
    print(Fore.LIGHTBLACK_EX + "       #######    " + Fore.BLUE + "      ------------------")
    print(Fore.LIGHTBLACK_EX + "       ##"+ Fore.WHITE + "O" + Fore.LIGHTBLACK_EX + "#" + Fore.WHITE + "O" + Fore.LIGHTBLACK_EX + "##" + Fore.RED + "          OS:" + Fore.GREEN + " PyOS") 
    print(Fore.LIGHTBLACK_EX + "       #" + Fore.YELLOW + "#####" + Fore.LIGHTBLACK_EX + "#" + Fore.RED +"          Host:" + Fore.GREEN + " Python")
    print(Fore.LIGHTBLACK_EX + "     ##" + Fore.WHITE + "##" + Fore.YELLOW + "###" + Fore.WHITE + "##" + Fore.LIGHTBLACK_EX + "##" + Fore.RED + "        Kernel:" + Fore.GREEN + " pyos-8.7")
    print(Fore.LIGHTBLACK_EX + "    #" + Fore.WHITE + "##########" + Fore.LIGHTBLACK_EX + "##" + Fore.RED + "       Uptime:" + Fore.GREEN + " Who knows?")
    print(Fore.LIGHTBLACK_EX + "   #" + Fore.WHITE + "############" + Fore.LIGHTBLACK_EX + "##      " + Fore.RED + "Packages: " + Fore.GREEN + "None")
    print(Fore.LIGHTBLACK_EX + "   #" + Fore.WHITE + "############" + Fore.LIGHTBLACK_EX + "###     " + Fore.RED + "Shell: " + Fore.GREEN + "pyshell1.0")
    print(Fore.YELLOW + "  ##" + Fore.LIGHTBLACK_EX + "#" + Fore.WHITE + "###########" + Fore.LIGHTBLACK_EX + "##" + Fore.YELLOW + "#     " + Fore.RED + "Resolution: " + Fore.GREEN + "None")
    print(Fore.YELLOW + "######" + Fore.LIGHTBLACK_EX + "#" + Fore.WHITE + "#######" + Fore.LIGHTBLACK_EX +"#" + Fore.YELLOW + "######   " + Fore.RED +"Terminal: " + Fore.GREEN + "shell.py")
    print(Fore.YELLOW + "#######" + Fore.LIGHTBLACK_EX + "#" + Fore.WHITE + "#####" + Fore.LIGHTBLACK_EX + "#" + Fore.YELLOW + "#######   " + Fore.RED + "CPU: " + Fore.GREEN + "PyCPU (1) @ 0.005GHz")
    print(Fore.YELLOW + "  #####" + Fore.LIGHTBLACK_EX + "#######" + Fore.YELLOW + "#####     " + Fore.RED + "Memory: " + Fore.GREEN + "1MiB / 2MiB")