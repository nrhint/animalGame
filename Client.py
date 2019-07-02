<<<<<<< HEAD
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
=======
##Nathan Hinton

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
##Here is the start of the game:
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ##Sending required data to the server:
    data = input('what is your player name: ')
    s.sendall(data.encode('utf-8'))
    while True:
        data = input("Command: ")
        s.sendall(data.encode())
>>>>>>> 406a32634192f4950cbfeb0fb83cc91999957251
