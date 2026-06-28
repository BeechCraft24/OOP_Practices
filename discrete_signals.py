import socket

HOST = "192.168.12.224"
PORT = 5000

class MONA:
    def mona_signal(self):
        return b"00"
        

class SNET:
    def snet_signal(self):
        return b"01"
        

class SYSCO:
    def sysco_signal(self):
        return b"10"
        

class STATUS:              
    def __init__(self):
        self.mona=MONA()
        self.snet=SNET()
        self.sysco=SYSCO()

    def alerts(self, client):
        signal = self.mona.mona_signal()
        client.sendall(signal)

        signal = self.snet.snet_signal()
        client.sendall(signal)

        signal = self.sysco.sysco_signal()
        client .sendall(signal)

        self.mona.mona_signal()
        self.snet.snet_signal()
        self.sysco.sysco_signal()

x=STATUS()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    x.alerts(client)