import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = '192.168.1.13'
port = 8000

serversocket.bind((hostname, port))
serversocket.listen(3)

while True:
    client, address = serversocket.accept()
    print('connection from', address)

    message = "hello to the server"
    
    client.send(message.encode('ascii'))
    client.close()
