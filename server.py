# Programmer: Jon Luis Koe
# Program Description: Creating a Server for a client to connect to
# Date: 09/23/2021
# Last Changed:09/27/2021

import socket

# creating the server socket using default par (ipv4, TCP)
server = socket.socket()
print("server socket created")

# bind only takes one argument, that's why use 2 (())
# bind ipaddress and port = 9999
server.bind(('localhost', 9999))

# server is going to connect with 3 clients at a given time
server.listen(3)
print("Server waiting for connections")

while True:
    client, ipaddress = server.accept() # retrieving client and its ip
    name = client.recv(1024).decode() # receiving data from lcient
    print("Server is now connected with ", ipaddress, name)
    client.send(bytes("You're now connected with the server", 'utf-8'))# sending the data to client
    client.close() # close the connection



