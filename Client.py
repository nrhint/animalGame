##Nathan Hinton

import socket

HOST = '192.168.85.56'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input("inputMessage: ")
        s.sendall(data.encode('utf-8'))
        #data = s.recv(1024)
