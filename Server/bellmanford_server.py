import sys
import socket
# following program reads from a file with below format and turns that into adjescent graph
# city1 city2 100 -> this means distance b/w city1 and city2 is 100
# it produces an adjescent graph on which dijkstras and bellmanford algorithms can be run
def addtodict(city:str,graph:[],dt:dict,vertex:int):
    if city in dt: return vertex
    dt[city] = vertex
    graph.append([])
    vertex=vertex+1
    return vertex

def makeagraph(filename:str) -> [[()]]:
    dt = dict()
    graph=[]
    vertex=0
    rf = filename
    for line in rf:
        if not line: break
        (city1,city2,distance) = line.split()
        vertex = addtodict(city1,graph,dt,vertex)
        vertex = addtodict(city2,graph,dt,vertex)
        graph[dt[city1]].append((dt[city2],int(distance)))
    rf.close()
    return graph,dt

def bellmanford(graph:[[()]],source) -> ([],[]):
    distance=[sys.maxsize for _ in range(len(graph))]
    prenode = ['none' for _ in range(len(graph))]
    distance[source] = 0
    prenode[source] = source
    for x in range(len(graph)-1):
        for i in range(len(graph)):
            for(neighbor,n_distance) in graph[i]:
                if (distance[i]+n_distance < distance[neighbor]):
                    distance[neighbor] = distance[i]+n_distance
                    prenode[neighbor] = i

    return (distance,prenode)

def convert_nodes_to_cities(distance,city_lst):
    final_cityand_distance = []
    for i in range(len(city_lst)):
        city = city_lst[i]
        distance_new = distance[i]
        final_cityand_distance.append((city,distance_new))
    
    return final_cityand_distance


 

#(distance,prenode) = bellmanford(example_graph_1,0)

#print("printing distances from source 0") 

#print(distance)

#print("printing the prenodes to reach from source 0 to every node")

#print(prenode)






 

# main
filename = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
g,dt = makeagraph(filename)
city_lst = ['seattle','kennewick','idaho','denver','oklahoma','dallas']
s = socket.socket()
print("Socket successfully created")
port = 18185    
s.bind(('', port))
BUF_SIZE = 200
s.listen(5)
print("socket is listening")
while True: 
    # Establish connection with client. 
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(BUF_SIZE)
    #it will parse data buffer if this is being SMTP packet or not
    print("receved data",data)
    source_city = data.decode("utf-8")
    if source_city in city_lst:
        source_number = city_lst.index(source_city)
        shortest_calculated_distance = bellmanford(g,source_number)
        final_cityand_distance = convert_nodes_to_cities(shortest_calculated_distance[0],city_lst)
        #final_cityand_distance = str(final_cityand_distance).encode()
        final_cityand_distance_1 = ("The distance from" ,source_city, "to other cities is : " ,final_cityand_distance)
        final_cityand_distance_1 = str(final_cityand_distance_1).encode()
        c.send(final_cityand_distance_1)
        
    if not data:
        break
    c.close()
    break
