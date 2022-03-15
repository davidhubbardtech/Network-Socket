import socket

# Use the socket function to create the client
Client = socket.socket()
Client.connect(('localhost',9999))


# Get client to input name
name = input("Type your name here: ")
Client.send(bytes(name, 'utf-8'))

print(Client.recv(1024).decode())