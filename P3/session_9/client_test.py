import socket

# SERVER IP, PORT
IP = "212.128.253.113"
PORT = 8080

while True:
    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = input("> ") #we only connect to the server when you have data to send to the server, if not, it will block the server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))



    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()