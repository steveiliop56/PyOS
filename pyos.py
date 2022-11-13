from System.auth import login
from System.programs import adduser, deluser

if login.login_screen() == True:
    print("Logged in!")
else:
    print("Loggin error")

