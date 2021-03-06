import socket
host = 'localhost'
port = 3419
name = ''
inputs = ''

def client_handler(c, addr):
   global inputs
   print('Got connection from', addr)
   name = c.recv(1024)
   name = str(name, 'utf-8')
   inputs += name
   if name == 'q':
      c.send(bytes("Good Bye, " + name, 'utf-8'))
   else:
      c.send(bytes("Thanks for connecting, " + name, 'utf-8'))
   c.send(bytes(inputs, 'utf-8'))
   print(inputs)



s = socket.socket()

s.bind((host,port))
s.listen(5)

print((host,port))
while name != 'q':
   c, addr = s.accept()     # Establish connection with client.
   client_handler(c,addr)   # set up a client handler
c.close()