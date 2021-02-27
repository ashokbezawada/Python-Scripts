import socket
T_PORT = 14567
TCP_IP = '192.168.0.107'
#TCP_IP = '172.217.1.142' #google ip address

BUF_SIZE = 200
# create a socket object name 'k'
k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
#g = socket.socket (socket_family, type_of_socket, protocol=value)
k.bind((TCP_IP,T_PORT)) #bind is used to bind address (host name port number to socket 
print ("waiting for connections")
k.listen(5) #listen  is used to establish and start TCP listener.
con, addr = k.accept() # accept()  is used to TCP client connection until the connection arrives.
print ('Connection Address is: ' , addr) 
while True :
    data = con.recv(BUF_SIZE)
    #it will parse data buffer if this is being SMTP packet or not
    print("receved data",data)
    if not data:
      break
    con.send(b"1")
    con.close()
    break


print ("Received data", data)
con.send(data)
con.close()
