import socket
import sys
from _thread import start_new_thread

HOST = '' # all availabe interfaces
PORT = 3419 # arbitrary non privileged port

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Could not create socket. Error Code: ")
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except:
    print("Bind Failed. Error Code: {} Error: {}")
    sys.exit()

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):
    conn.send(bytes("Welcome to the Server. Type messages and press enter to send.\n",'ascii'))

    while True:
        data = conn.recv(1024)
        if not data:
            break
        reply = bytes("OK . . ",'ascii') + data
        conn.sendall(reply)
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()