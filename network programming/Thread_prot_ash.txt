import socket  
import threading 
import os
import time

def print_cube(b):
	t1 = threading.Thread(target=print_cube, args=(b,)) 
	print("Cube : {}".format(b*b*b))
	return t1

def print_square(a):
	t2 = threading.Thread(target=print_square, args=(a,)) 
	#t2.start()
	#print("Square : {}".format(a*a))
	#t2.join()
	#print("Done!")

def recv_data(data):
	t1 = data.decode("utf-8")
	t3 = t1.split(" ")
	str1 = ""
	str2 = ""
	if 'stop' not in t3:
		for i in t3:
			if(i != 'start'):
				str1 = str1 + i
				continue
			b = int(str1)
			print(b)
			t1 = print_cube(b)
			t1.start()
			t1.join()

	if 'start' not in t3:
		for i in t3:
			if(i != 'stop'):
				str2 = str2 + i
			a = int(str2)
			print_square(a)
			break




# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer in our 
port = 12345     
           
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
  
BUF_SIZE = 200
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 

while True: 
	s.listen(5)
   # Establish connection with client. 
	c, addr = s.accept()      
	data = c.recv(BUF_SIZE)
    #it will parse data buffer if this is being SMTP packet or not
	print("receved data",data)
	# Function call for the received data
	recv_data(data)
	print('Got connection from', addr)
	#data = c.recv(BUF_SIZE)
	while True:
		print("I want to connect to another client")
		c, addr = s.accept()
		data = c.recv(BUF_SIZE)
		print("received data",data) 
		recv_data(data)   
	
	print("The socket is in listening state")
	if not data:
		break
	c.close()
	break

  
  