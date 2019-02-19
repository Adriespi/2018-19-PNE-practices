import socket

#defining data
IP = "212.128.253.113"
PORT = 8085
MAX_OPEN_REQUEST = 5

def process_client(cs):#specialized at attending info from the client, reading a message from client and sending it back
    #reading the message from the client
    msg = cs.recv(2048).decode('utf-8')
    #printing the message
    print('Message from the client: {}'.format(msg))
    #now we send back the message to the client using the sent method. ECHO-SERVER
    cs.send(str.encode(msg))
    cs.close()

#Creating the socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))

#The socket needs to listen to some requests
serversocket.listen(MAX_OPEN_REQUEST)

print('Socket created: {}'.format(serversocket))

while True:
    print('Waiting for connections... {}, {}'.format(PORT, IP))
    (clientsocket, address) = serversocket.accept()  # this method will block the server and wait until a client is connected
    # -- Process the client request
    print('Attending client: {}'.format(address))

    process_client(clientsocket)


