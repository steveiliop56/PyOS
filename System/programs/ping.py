from pythonping import ping

def pingd(params):
    ping(str(params), verbose=True, interval=1)

def command_info():
    return "Ping a website to check if it is up or down. Usage ping website."