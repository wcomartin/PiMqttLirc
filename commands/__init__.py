from py_irsend import irsend


def send_once(device, cmd):
    try:
        irsend.send_once(device, [cmd])
        print("Sent: " + device + " - " + cmd)
    except:
        print("Failed to send: " + device + " - " + cmd)