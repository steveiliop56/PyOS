from pythonping import ping

def pingd(params):
    ping(str(params), verbose=True, interval=1)
