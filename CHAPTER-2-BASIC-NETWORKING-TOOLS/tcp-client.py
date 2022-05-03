#!/bin/python3

import socket

target_host = "127.0.0.1"

target_port = 4747

# create a socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client

client.connect((target_host,target_port))

# send some data

client.send(b"g0dmax55")

# receive some data

response = client.recv(4096)

print(response.decode("utf-8"))

client.close()

