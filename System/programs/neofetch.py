import colorama as c

c.init(autoreset=True)

def run(params, username):
    print(c.Fore.LIGHTBLACK_EX + "        #####    " + c.Fore.RED +
          f"       {username}" + c.Fore.BLUE + "@" + c.Fore.GREEN + "pyos")
    print(c.Fore.LIGHTBLACK_EX + "       #######    " +
          c.Fore.BLUE + "      ------------------")
    print(c.Fore.LIGHTBLACK_EX + "       ##" + c.Fore.WHITE + "O" + c.Fore.LIGHTBLACK_EX + "#" +
          c.Fore.WHITE + "O" + c.Fore.LIGHTBLACK_EX + "##" + c.Fore.RED + "          OS:" + c.Fore.GREEN + " PyOS")
    print(c.Fore.LIGHTBLACK_EX + "       #" + c.Fore.YELLOW + "#####" +
          c.Fore.LIGHTBLACK_EX + "#" + c.Fore.RED + "          Host:" + c.Fore.GREEN + " Python")
    print(c.Fore.LIGHTBLACK_EX + "     ##" + c.Fore.WHITE + "##" + c.Fore.YELLOW + "###" + c.Fore.WHITE +
          "##" + c.Fore.LIGHTBLACK_EX + "##" + c.Fore.RED + "        Kernel:" + c.Fore.GREEN + " pyos-8.7")
    print(c.Fore.LIGHTBLACK_EX + "    #" + c.Fore.WHITE + "##########" + c.Fore.LIGHTBLACK_EX +
          "##" + c.Fore.RED + "       Uptime:" + c.Fore.GREEN + " Who knows?")
    print(c.Fore.LIGHTBLACK_EX + "   #" + c.Fore.WHITE + "############" +
          c.Fore.LIGHTBLACK_EX + "##      " + c.Fore.RED + "Packages: " + c.Fore.GREEN + "None")
    print(c.Fore.LIGHTBLACK_EX + "   #" + c.Fore.WHITE + "############" +
          c.Fore.LIGHTBLACK_EX + "###     " + c.Fore.RED + "Shell: " + c.Fore.GREEN + "pyshell1.0")
    print(c.Fore.YELLOW + "  ##" + c.Fore.LIGHTBLACK_EX + "#" + c.Fore.WHITE + "###########" +
          c.Fore.LIGHTBLACK_EX + "##" + c.Fore.YELLOW + "#     " + c.Fore.RED + "Resolution: " + c.Fore.GREEN + "None")
    print(c.Fore.YELLOW + "######" + c.Fore.LIGHTBLACK_EX + "#" + c.Fore.WHITE + "#######" + c.Fore.LIGHTBLACK_EX +
          "#" + c.Fore.YELLOW + "######   " + c.Fore.RED + "Terminal: " + c.Fore.GREEN + "shell.py")
    print(c.Fore.YELLOW + "#######" + c.Fore.LIGHTBLACK_EX + "#" + c.Fore.WHITE + "#####" + c.Fore.LIGHTBLACK_EX +
          "#" + c.Fore.YELLOW + "#######   " + c.Fore.RED + "CPU: " + c.Fore.GREEN + "PyCPU (1) @ 0.005GHz")
    print(c.Fore.YELLOW + "  #####" + c.Fore.LIGHTBLACK_EX + "#######" + c.Fore.YELLOW +
          "#####     " + c.Fore.RED + "Memory: " + c.Fore.GREEN + "1MiB / 2MiB")

def help():
    return "Gives info about the system a nice format. Usage: neofetch."
