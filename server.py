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
   c.send(bytes("thanks for connecting", 'utf-8'))
   c.close()