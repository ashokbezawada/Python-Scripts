
import socket

T_PORT = 6001

#TCP_IP = '127.0.0.1'
#TCP_IP = '172.217.1.142'
TCP_IP = '192.168.0.15'
BUF_SIZE = 1024

MSG = b'Hello karl'

# create a socket object name 'k'

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((TCP_IP, T_PORT))
while True:
    k.send(MSG)
    k.send(b'hello ashok')
    data = k.recv(BUF_SIZE)
    print(data)

k.close