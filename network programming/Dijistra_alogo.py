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

example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(3,2)],
                 [(3,2),(4,1)]]

for i in range(len(example_graph)):
    shortest_calculated_distance = Dijkstra_algo(example_graph,i)
    print(shortest_calculated_distance)
    
    