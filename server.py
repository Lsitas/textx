import socket

s = socket.socket()

host = 'localhost'
port = 3419
s.bind((host,port))
s.listen(5)
print((host,port))

senders = []
listeners = []






while True:
   conn, addr = s.accept()     # Establish connection with client.
   if (conn.recv(1) == bytes(1)):
      print('Got connection from', addr, ' as Sender')
      senders.append(conn)
   else:
      print('Got connection from', addr, ' as Listener')
      listeners.append(conn)

   for i in senders:
      i.close()
   for i in listeners:
      i.close()