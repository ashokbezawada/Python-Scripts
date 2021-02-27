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

# Main
input_file = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
new_lists = graphfrom_textfile_f1(input_file)
input_file_1 = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
new_cities_graph = graphfrom_textfile_f2(new_lists[0],new_lists[1],input_file_1)
print(new_cities_graph)

print("The shortest distance from node 1 : " ,Dijkstra_algo(new_cities_graph,1))

    
