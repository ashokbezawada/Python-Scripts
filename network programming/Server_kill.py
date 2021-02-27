# first of all import the socket library 
import socket   
import subprocess
import os
def open_proc(process_name):
    pid = subprocess.Popen(process_name)
    print("pid is", pid.pid)
    return pid.pid

def kill_proc(proc_name):
	os.system("taskkill /f /im " + b)
  
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

   # Establish connection with client. 
	c, addr = s.accept()      
	print('Got connection from', addr)

	data = c.recv(BUF_SIZE)
    #it will parse data buffer if this is being SMTP packet or not
	print("receved data",data)
	t1 = data.decode("utf-8")
	t3 = t1.split(" ")
	lst1 = []
	lst2 = []
	if 'stop' not in t3:
		for i in t3:
			lst1.append(i)
			break
		a = lst1[0]
		pid_pid = open_proc(a)
		print(pid_pid)
		msg = str(pid_pid).encode()
		c.send(msg)
	if 'start' not in t3:
		for i in t3:
			lst2.append(i)
			break 
		b = lst2[0]
		kill_proc(b)
	if not data:
		break
	c.close()
	break

  
  