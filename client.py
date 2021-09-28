# Programmer: Jon Luis Koe
# Program Description: Creating a client to connect to server
# Date: 09/23/2021
# Last Changed:09/27/2021

import socket

# creating the client socket
client = socket.socket()

# connecting to the server with given IP and port number
client.connect(('localhost', 9999))

name = input("Enter your host name")

client.send(bytes(name, 'utf-8')) # sending the data to server

print(client.recv(1024).decode()) # receiving data from server
