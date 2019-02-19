#programming our first client

import socket

#creating a socket or communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
#same behaviour as a file
PORT = 8080
IP = '212.128.253.64'

#connect to the server
s.connect((IP,PORT))

#send a message to the server
s.send(str.encode('HELLO FROM MY CLIENT')) #encode is to translate the string into bytes

#receive a message from the server
msg = s.recv(2048).decode('utf-8')
print('Message from the server: ')
print(msg)
s.close()

print('The end')
