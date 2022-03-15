import socket

# Use the socket function to create the server
server = socket.socket()
print('socket is currently available')

# Bind the socket to a port number
server.bind(('localhost',9999))
# Make sure to use a free and open port number

server.listen(3)
print('searching for other users...')

# Create a loop that enables the server to accept connection from client
while True:
    Client, address = server.accept()
# Allow the server to receive the new connection and new port number
    name = Client.recv(1024).decode()
    print("Connection confirmed with", name, address)

    Client.send(bytes('Connection confirmed!','utf-8'))

    Client.close()