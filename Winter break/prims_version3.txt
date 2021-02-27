import random
import sys

# The main goal of the function is return minimum cost edge.
# The fnction takes arguments as graph, current,prims_vertices 
def find_lowcost_edge(graph,current,prims_vertices):
    distance = sys.maxsize
    for current in prims_vertices:
        for neighbour in graph[current]:
            node = neighbour[0]
            cost = neighbour[1]
            if node not in prims_vertices:
                if(cost < distance):
                    distance = cost
                    new_node = current
                    neighbour_node = node
                
    return(new_node,neighbour_node)

# The main gaol of the function is to find the minimum spanning tree
# The function takes argument as graph 
def prims_algo(graph):
    prims_vertices = []
    prims_edges = []
    length = len(graph) - 1
    current = random.randint(0,length)
    print("The source vertex is : ",current)
    prims_vertices.append(current)
    while(len(prims_vertices) < len(graph)):
        edge_of_lowcost = find_lowcost_edge(graph,current,prims_vertices)
        prims_edges.append(edge_of_lowcost)
        prims_vertices.append(edge_of_lowcost[1])

    return (prims_edges,prims_vertices)


# Main Function
example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(5,1)],
                 [(3,2),(4,1)]]

prims_edges = prims_algo(example_graph)
print("edges are : " , prims_edges[0])
print("vertices are : " , prims_edges[1])


# example 2
example_graph_1 = [[(1,2),(2,1)],
                   [(0,2),(2,3),(3,1)],
                   [(0,1),(1,3),(3,4)],
                   [(1,1),(2,4)]]
    
prims_edges = prims_algo(example_graph_1)
print("edges are : " , prims_edges[0])
print("vertices are : " , prims_edges[1])

# example 3
example_graph_2  = [[(1,3)],
                    [(0,3)]]
prims_edges = prims_algo(example_graph_2)
print("edges are : " , prims_edges[0])
print("vertices are : " , prims_edges[1])

example_graph_3   = [[(1,1),(2,2)],
                     [(0,1),(2,1)],
                     [(0,2),(1,1)]]

prims_edges = prims_algo(example_graph_3)
print("edges are : " , prims_edges[0])
print("vertices are : " , prims_edges[1])
                    

                                 









