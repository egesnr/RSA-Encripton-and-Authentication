import socket
from secAuth import verified2
host = socket.gethostname()
port = 80

server_socket = socket.socket()  # get instance
server_socket.bind((host, port))  # bind host address and port together
server_socket.listen(5)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
while True:
        print("-------------SERVER----------------")
        data = conn.recv(1024).decode()
        print("from connected user: " + str(data))
        if verified2:
         conn.send("Hello Client. Authenticatin is correct".encode())
        else:
          conn.send("ERROR. Authentication is wrong".encode())
        break
conn.close()
