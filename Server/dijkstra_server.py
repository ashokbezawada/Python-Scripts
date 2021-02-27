import socket  
# The main goal of this function is it will return all cities present in a text file
# The function takes argument as file path
def graphfrom_textfile_f1(file):
    cities = []
    new_cities_graph = []
    for line in file:
        new_line = line.split()
        for i in new_line:
            if i not in cities:
                if (i.isnumeric()) == False:
                    cities.append(i)
    for i in range(len(cities)):
        i = []
        new_cities_graph.append(i)
    
    return(cities,new_cities_graph)

# The main goal of the function is to create graph with help of lists
# The function takes arguments lists and file_path
def graphfrom_textfile_f2(cities,new_cities_graph,file_1):
    for line in file_1:
        new_line = line.split()
        for city in new_line:
            if city in cities:
                city_index = cities.index(city)
                for new_city in new_line:
                    if(city != new_city and new_city.isnumeric() == False):
                        new_city_index = cities.index(new_city)
                    if (new_city.isnumeric()) == True:
                        distance = int(new_city)
                        #print(distance)
            new_cities_graph[city_index].append((new_city_index,distance))
            break
    
    return new_cities_graph

# visit the unvisited vertex with the shortest known distance
def visit_unvisited_vertex_shortest_distance(distance,unvisited):
    min_node = unvisited[0]
    minimum = distance[min_node]
    for i in unvisited:
        if(distance[i] <= minimum):
            minimum = distance[i]
            min_node = i
    return min_node
        
def Dijkstra_algo(graph,source):
    visited = []
    unvisited = []
    current = source
    shortest_distance = {}
    previous_node = {}
    length = len(graph)
    for i in range(length):
        unvisited.append(i)
        shortest_distance[i] = 999999
        previous_node[i] = 'undefined'
    
    shortest_distance[current] = 0
    while (len(unvisited) > 1):
        # Visit the unvisited vertex with the shortest known distance
        current = visit_unvisited_vertex_shortest_distance(shortest_distance,unvisited)
        for neighbours in graph[current]:
            node = neighbours[0]
            cost = neighbours[1]
            if node not in visited:
                alt_cost = shortest_distance[current] + cost
                if(alt_cost < shortest_distance[node]):
                    shortest_distance[node] = alt_cost
                    previous_node[node] = current

        # Removing visited vertex in unvisited vertex
        unvisited.remove(current)
        visited.append(current)
    return shortest_distance

def convert_nodes_to_cities(shortest_distance,city_lst):
    final_cityand_distance = []
    for i in range(len(city_lst)):
        city = city_lst[i]
        distance = shortest_distance[i]
        final_cityand_distance.append((city,distance))
    
    return final_cityand_distance


# Main function
input_file = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
new_lists = graphfrom_textfile_f1(input_file)
input_file_1 = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
new_cities_graph = graphfrom_textfile_f2(new_lists[0],new_lists[1],input_file_1)
city_lst = ['seattle','kennewick','idaho','denver','oklahoma','dallas']
s = socket.socket()
print("Socket successfully created")
port = 12345     
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
        shortest_calculated_distance = Dijkstra_algo(new_cities_graph,source_number)
        final_cityand_distance = convert_nodes_to_cities(shortest_calculated_distance,city_lst)
        #final_cityand_distance = str(final_cityand_distance).encode()
        final_cityand_distance_1 = ("The distance from" ,source_city, "to other cities is : " ,final_cityand_distance)
        final_cityand_distance_1 = str(final_cityand_distance_1).encode()
        c.send(final_cityand_distance_1)
        
    if not data:
        break
    c.close()
    break


  