import socket  
import threading 
import os
import time
import argparse


def print_cube(b):
    cube = b*b*b
    print("The cube is : ",cube)
    return cube

def process_recv_data(data_recv_pc):
    t1 = data_recv_pc.decode("utf-8")
    t3 = int(t1)
    cube = print_cube(t3)
    cube_str = str(cube)
    msg1 = str.encode(cube_str)
    return msg1
	

def process_client_connection(client_socket,client_address):
    print("Got connection from: ",client_address)
    data = client_socket.recv(BUF_SIZE)
    #it will parse data buffer if this is being SMTP packet or not
    print("receved data:",data)
    time.sleep(60)
    # Function call for the received data
    msg = process_recv_data(data)
    client_socket.send(msg)


parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--serverport")
parser.add_argument("--outstandingconnections")
args = parser.parse_args()
port = int(args.serverport)
outstandingconnections = int(args.outstandingconnections)
# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
# reserve a port on your computer and bind
#port = int(input("Enter the server port number greater than 1024 to bind : "))    
s.bind(('', port))         
BUF_SIZE = 200
# put the socket into listening mode 
s.listen(outstandingconnections)      
print("socket is listening")            
# a forever loop until we interrupt it or  
# an error occurs 
while True:
    c, addr = s.accept()
    #process_client_connection(c,addr)
    t3 = threading.Thread(target=process_client_connection,args=(c,addr))
    t3.start()


  
  