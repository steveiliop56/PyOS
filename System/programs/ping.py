from pythonping import ping

def run(params, username):
    ping(str(params), verbose=True, interval=1)

def help():
    return "Ping a website to check if it is up or down. Usage ping website."
