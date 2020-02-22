from _thread import start_new_thread
import socket

s = socket.socket()

host = 'localhost'
port = 3419
s.bind((host,port))
s.listen(5)
print((host,port))

senders = []
listeners = []


def server_thread():
   while True:
      if len(senders) > 0:
         msg = senders[0].recv(1024)
         print("recieved ",msg," from sender")
         for i in listeners:
            i.sendall(msg)

start_new_thread(server_thread,())
while True:
   print("waiting on new connection")
   conn, addr = s.accept()     # Establish connection with client.
   msg = conn.recv(1)
   if (msg == bytes(1)):
      print('Got connection from', addr, ' as Sender')
      senders.append(conn)
   else:
      print('Got connection from', addr, ' as Listener')
      listeners.append(conn)

for i in senders:
   i.close()
for i in listeners:
   i.close()