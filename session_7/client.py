#programming our first client

import socket

#creating a socket or communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
#same behaviour as a file
