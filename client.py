import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'localhost'          # Get local machine name
port = 3419                 # Reserve a port for your service.
name = input("Name: ")


s.connect((host, port))
s.send(bytes(name, 'utf-8'))
print(s.recv(1024))
s.close()