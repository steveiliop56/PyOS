import platform
import os

def run(params, username):
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")

def help():
    return "This command clears the screen. Usage: clear."
