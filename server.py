import socket

s = socket.socket()

host = 'localhost'
port = 3419
s.bind((host,port))
s.listen(5)

print((host,port))
while True:
   sender, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr, ' as Sender')
   listener, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr, ' as Listener')
   while True:
      name = sender.recv(1024)
      listener.send(bytes("Thanks for connecting, ", 'utf-8') + name)
   sender.close()
   listener.close()