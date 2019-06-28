##Nathan Hinton

print("server starting...")

import socket
from threading import Thread

class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New thread started for %s:%s"%(ip, str(port)))
    def run(self):
        while True:
            data = conn.recv(2048)
            data = data.decode()
            print(data+"--FROM--:"+self.ip)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
threads = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        #print("server listening...")
        (conn, (ip, port)) = s.accept()#addr = s.accept()
        newthread = ClientThread(ip, port)
        newthread.start()
        threads.append(newthread)
'''    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data+b". From server")
'''
