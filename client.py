import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.1.85'          # Get local machine name
port = 3419                 # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024))
s.close()