# visit the unvisited vertex with the shortest known distance
def visit_unvisited_vertex_shortest_distance(distance,unvisited):
    min_node = unvisited[0]
    minimum = distance[min_node]
    for i in unvisited:
        if(distance[i] < minimum):
            minimum = distance[i]
            min_node = i
    return min_node

def Dijkstra_algo(graph,source):
    visited = []
    path = []
    unvisited = []
    current = source
    shortest_distance = {}
    previous_node = {}
    length = len(graph)
    for i in range(length):
        unvisited.append(i)
        shortest_distance[i] = 999999
        previous_node[i] = 'undefined'
    
    for i in previous_node:
        path.append(i)
    
    shortest_distance[current] = 0
    while (len(unvisited) > 1):
        # Visit the unvisited vertex with the shortest known distance
        current = visit_unvisited_vertex_shortest_distance(shortest_distance,unvisited)
        for neighbour in graph[current]:
            node = neighbour[0]
            cost = neighbour[1]
            if node not in visited:
                alt_cost = shortest_distance[current] + cost
                if(alt_cost < shortest_distance[node]):
                    shortest_distance[node] = alt_cost
                    previous_node[node] = current
            
        # Removing visited vertex in unvisited vertex
        unvisited.remove(current)
        visited.append(current)
    return previous_node

def find_path(previous_node,source,destination):
    previous_node[0] = 0
    lst1 = []
    # lst1.append(previous_node[destination])
    # lst1.append(previous_node[lst1[-1]])
    # lst1.append(previous_node[lst1[-1]])
    # if (source = lst[-1]):
    lst1.append(destination)
    while (lst1[-1] != source):
        lst1.append(previous_node[destination])
        lst1.append(previous_node[lst1[-1]])
        destination = lst1[-1]

    return lst1


example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(3,2)],
                 [(3,2),(4,1)]]

example_graph_1 = [[(1,4),(4,8)],
                   [(0,4),(2,8),(4,11)],
                   [(1,8),(8,2),(6,4),(3,7)],
                   [(2,7),(7,9),(6,14)],
                   [(0,8),(8,7),(5,1),(1,11)],
                   [(4,1),(6,2),(8,6)],
                   [(5,2),(7,10),(2,4),(3,14)],
                   [(6,10),(3,9)],
                   [(4,7),(5,6),(2,2)]]
#shortest_calculated_distance = Dijkstra_algo(example_graph,0)

new_dict = Dijkstra_algo(example_graph,0)
lst1 = find_path(new_dict,0,5)
print(lst1)





