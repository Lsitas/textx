import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'localhost'          # Get local machine name
port = 3419                 # Reserve a port for your service.



s.connect((host, port))
s.sendall(bytes(1))
while True:
    name = input("")
    s.send(bytes(name, 'utf-8'))
s.close()