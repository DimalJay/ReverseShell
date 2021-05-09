import os
import socket

host = "127.0.0.1"
port = 5000
BUFFER_SIZE = 1024*128
# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind a local socket to the port
server_address = (host, port)
sock.bind(server_address)
sock.listen(1)

print("Waiting for Connection")
conn, addr = sock.accept()
print("You Have Got a Connection from {0}".format(addr))

while True:
    cwd = conn.recv(BUFFER_SIZE).decode('utf-8')
    print("( {0}:{1} )".format(addr[0],addr[1]),cwd+"> ",end='')
    command = input().encode('utf-8')
    conn.send(command)
    print(conn.recv(BUFFER_SIZE).decode('utf-8'))
    
