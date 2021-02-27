# Import socket module 
import socket   
# Create a socket object 
s = socket.socket()          
# Define the port on which you want to connect 
port = 12345
bufsize = 1024                
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# The main goal of the function is to get the city name from user
def toget_city():
    print("enter any city from Seattle, Kennewick, Idaho, Denver, Oklahoma, Dallas")
    city_name = input("enter a city : ")
    if city_name not in city_list:
        print("We still don't have data about" ,city_name, "we are still working on distances between all the cities to get updated in our database")
        city_name = input("Please enter a valid city")
    return city_name

city_list = ['seattle','kennewick','idaho','denver','oklahoma','dallas']	
city_name = toget_city()
msg1 = str.encode(city_name)
s.send(msg1)

while True:
    data=s.recv(bufsize)
    data = data.decode("utf-8")
    print(data)
    break
s.close 