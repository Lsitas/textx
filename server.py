import socket

s = socket.socket()

host = 'localhost'
port = 3419
s.bind((host,port))
s.listen(5)

print((host,port))
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   name = c.recv(1024)
   c.send(bytes("Thanks for connecting, ", 'utf-8') + name)
   c.close()