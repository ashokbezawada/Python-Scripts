import sys
# The main goal of this function is to return the node with shortest distance
# The function takes argument as unvisited_list and shortest_distance
def shortest_node(distance_lst,vertices):
    minimum = sys.maxsize
    for i in vertices:
        initial_min = min(distance_lst[i],minimum)
        if(initial_min < minimum):
            minimum = initial_min
            node = i
    return node
        

# The main goal of this function is to print the shortest distance from one node to rest of the nodes using dijkstra algo
# The function takes argument as graph and source
def dijkstra_algo(graph,source):
    length = len(graph)
    # I require four lists to store visited nodes, unvisited nodes, shortest distance, previous vertex
    visited = []
    unvisited = []
    shortest_distance = []
    previous_node = []
    
    # Intially dijkstra don't know anything about the shortest distances from one node to other so, everything will be infinity
    for i in range(length):
        shortest_distance.append(sys.maxsize)
        previous_node.append("undefined")
        unvisited.append(i)
    
    shortest_distance[source] = 0
    previous_node[source] = "nil"

    while(len(visited) <= length - 1):
        current = shortest_node(shortest_distance,unvisited)
        for (neighbour,neighbour_cost) in graph[current]:
            if neighbour not in visited:
                cost = shortest_distance[current] + neighbour_cost
                if (cost < shortest_distance[neighbour]):
                    shortest_distance[neighbour] = cost
                    previous_node[neighbour] = current
        
        unvisited.remove(current)
        visited.append(current)
    
    return shortest_distance

# main 

# Declaring graph
example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(3,2)],
                 [(3,2),(4,1)]]

start_vertex = int(input("Enter a valid starting point: "))
shortest_distance = dijkstra_algo(example_graph,start_vertex)
print(shortest_distance)