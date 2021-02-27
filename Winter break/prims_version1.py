# Then main goal of the function is to return the minimum spanning tree having all the vertices.
# The function takes argument as a graph
import random
def prims_algo(graph):
    # creating empty lists 
    check_vertices = []
    prims_vertices = []
    prims_edges = []
    prims_edges_1 = []
    # Intializing distance to a large number
    distance = 999999
    # current is random number in the range 0 to length of the graph
    length = len(graph) - 1
    current = random.randint(0,length)
    print("The source node is :" ,current)
    prims_vertices.append(current)
    check_vertices.append(current)
    while (len(prims_vertices) <= length):
        # Finding which node to visit from neighbours who are at shortest distance
        for neighbour in graph[current]:
            min_node = neighbour[0]
            minimum_distance = neighbour[1]
            if min_node not in prims_vertices:
                if(minimum_distance < distance):
                    distance = minimum_distance
                    min_node = neighbour[0]

        # Checking shortest distance from vertices which are present in check vertices and not in prims vertices            
        if (len(check_vertices) != 0):
            for x in check_vertices:
                for neighbour in graph[x]:
                    new_node = neighbour[0]
                    new_distance = neighbour[1]
                    if new_node not in prims_vertices:
                        if(new_distance <= distance):
                            distance = new_distance
                            min_node = neighbour[0]
                            min_node_1 = neighbour[0]
        prims_edges_1.append((current,min_node))
        prims_edges_1.append((x,min_node_1))
        prims_vertices.append(min_node)
        check_vertices.append(min_node)
        prims_edges.append((min_node,distance))
        current = min_node
        distance = 999999
    return (prims_edges,prims_edges_1)
    

example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(5,1)],
                 [(3,2),(4,1)]]

prims_edges = prims_algo(example_graph)
print("The minimum edges that are going to be in minimum spanning tree are : " , prims_edges[0])
print(prims_edges[1])