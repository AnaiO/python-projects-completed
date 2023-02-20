import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = '192.168.1.13'
port = 8000

clientsocket.connect((hostname, port))

message = clientsocket.recv(1024)
clientsocket.close()

print(message.decode('ascii'))