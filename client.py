import socket               # Import socket module


s = socket.socket()  # Create a socket object
host = 'localhost'  # Get local machine name
port = 3419  # Reserve a port for your service.
s.connect((host, port))
name = ''
while name != 'q':
    name = input("Name: ")
    s.send(bytes(name, 'utf-8'))
    print(str(s.recv(1024),'utf-8'))
    print(str(s.recv(1024),'utf-8'))

s.close()
