

import socket


id=10
id="hello"

#create an socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding to hostname on the port 1234
hostname=socket.gethostname()
print("hostname:",hostname)
s.bind((hostname, 1234))
#listening for 5 backlog connections
s.listen(5)

#creating a loop to accept connections
while True:
    #wiating for connection
    clientsocket, address = s.accept()
    #received connection
    print("Connection from {address} has been established!")
    #sending back data
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))

