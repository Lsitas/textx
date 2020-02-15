import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = 'localhost'          # Get local machine name
port = 3419                 # Reserve a port for your service.



s.connect((host, port))
while True:
    print(s.recv(1024))
s.close()