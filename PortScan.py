import socket

def PortScan():
    s = socket.socket()
    for port in range(20, 25):
        try:
            s.connect(("210.117.188.61", port))
            mseeage = 'Primal Security \n'
            s.send(mseeage.encode())
            banner = s.recv(1024).decode()
            if banner:
                print("Port:" + str(port) + " open" )
            s.close()
        except: pass

PortScan()
