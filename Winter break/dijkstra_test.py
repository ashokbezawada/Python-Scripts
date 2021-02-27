def shortest_known_distance(shortest_distance,unvisited):
    min_node = unvisited[0]
    min_distance = shortest_distance[min_node]
    for i in unvisited:
        if(shortest_distance[i] < min_distance):
            min_node = i
            min_distance = shortest_distance[i]
    return min_node

def dijkstra(graph,source):
    visited = []
    unvisited = []
    previous_node = {}
    shortest_distance = {}
    current = source
    length = len(graph)
    for i in range(length):
        unvisited.append(i)
        previous_node[i] = "undefined"
        shortest_distance[i] = 9999999
    shortest_distance[current] = 0
    while(len(unvisited) > 1):
        # visit the unvisited vertex with shortest known distance
        current = shortest_known_distance(shortest_distance,unvisited)
        for neighbour in graph[current]:
            node = neighbour[0]
            cost = neighbour[1]
            if node not in visited:
                alt_cost = shortest_distance[current] + cost
                if(alt_cost < shortest_distance[node]):
                    shortest_distance[node] = alt_cost
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

for i in range(len(example_graph) -1):
    shortest_calculated_distance = dijkstra(example_graph,i)
    print("The shortest distance from node 0 : " ,dijkstra(example_graph,i))