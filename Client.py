import socket
from secAuth import signed2
host = socket.gethostname()  
port = 80

client_socket = socket.socket()
client_socket.connect((host, port))

message = signed2   # take input

while True:
        print("----------CLIENT---------------")
        client_socket.send(str(message).encode())
        
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        break

client_socket.close()
