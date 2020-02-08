import socket               # Import socket module


s = socket.socket()  # Create a socket object
host = '192.168.1.160'  # Get local machine name
port = 9999  # Reserve a port for your service.
s.connect((host, port))
name = ''
while name != 'q':
    name = input("Name: ")
    s.send(bytes(name, 'ascii'))
    print(str(s.recv(1024),'ascii'))

s.close()
