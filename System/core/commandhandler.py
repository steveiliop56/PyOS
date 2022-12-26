from System.programs import adduser, deluser, passwd
from time import sleep

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
        case "exit":
            print("Executing exit...")
            exit()
