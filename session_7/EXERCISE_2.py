import socket

#creating a socket or communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#same behaviour as a file
PORT = 8080
IP = '212.128.253.64'

#send a message to the server
while True:
    s.connect((IP, PORT))
    msg = input('Enter: ')
    s.send(str.encode(msg))

