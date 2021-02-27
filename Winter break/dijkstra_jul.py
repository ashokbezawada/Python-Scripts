def min_node(unvisited,shortest_distance):
    min_node = unvisited[0]
    min_dist = shortest_distance[min_node]
    for i in range(len(unvisited)):
        if(shortest_distance[i] <= min_dist):
            min_dist = shortest_distance[i]
            min_node = i
    return min_node

def dijkstra_algo(graph,source):
    visited = []
    unvisited = []
    shortest_distance = {}
    previous_node = {}
    
    for i in range(len(graph)):
        unvisited.append(i)
        previous_node[i] = 'undefined'
        shortest_distance[i] = 9999999
    
    shortest_distance[source] = 0
    while(len(unvisited)>1):
        current = min_node(unvisited,shortest_distance)
        for neighbours in graph[current]:
            node = neighbours[0]
            cost = neighbours[1]
            new_cost = shortest_distance[current] + cost
            if(new_cost < shortest_distance[node]):
                shortest_distance[node] = new_cost
                previous_node[node] = current
        unvisited.remove(current)
        visited.append(current)
    return shortest_distance
 





#main
example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(3,2)],
                 [(3,2),(4,1)]]
shortest_distance = dijkstra_algo(example_graph,0)
print(shortest_distance)