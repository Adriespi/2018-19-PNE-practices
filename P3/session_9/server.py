import socket, termcolor

PORT = 8080
IP = "212.128.253.113"
MAX_OPEN_REQUEST = 5 #maximum clients connected

def process_client(cs):#specialized at attending info from the client, reading a message from client and sending it back
    #reading the message from the client
    msg = cs.recv(2048).decode('utf-8')
    #printing the message
    termcolor.cprint('Message from the client: {}'.format(msg),'green')
    #now we send back the message to the client using the sent method. ECHO-SERVER
    cs.send(str.encode(msg))
    cs.close()

#now we need a socket (AF_INET will always be the same/ SOCK_STREAM is to make the socket as a file that can be edited)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#stablish the ip and port for the socket using the bind module

serversocket.bind((IP, PORT))

#We want a socket that listens to the requests

serversocket.listen(MAX_OPEN_REQUEST)#WAIT UNTIL THE stablished number of connections

print('Socket ready: {}'.format(serversocket))

#UNTIL NOW WE'VE JUST CONFIGURED THE SOCKET
while True: #and this will happen again
    print('Waiting for connections at: {}, {}'.format(IP,PORT))
    (clientsocket, address) = serversocket.accept()#this method will block the server and wait until a client is connected

    # -- Process the client request
    print('Attending client: {}'.format(address))

    process_client(clientsocket)