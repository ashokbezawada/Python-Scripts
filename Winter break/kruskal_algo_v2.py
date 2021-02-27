# The main goal of the function is to return all the edges in their incresing order
# The function takes argument as graph
def kruskal_algorithm(graph):
    length = len(graph)
    current = 0
    edges = []
    #edge_dict = {}
    while (current <= length - 1):
        for (neighbour_vertex,neighbour_cost) in graph[current]:
            edge_vertex1 = current
            edge_vertex2 = neighbour_vertex
            cost = neighbour_cost
            edges.append((cost,(edge_vertex1,edge_vertex2)))
            #edge_dict[cost] = ((edge_vertex1,edge_vertex2))
        current = current + 1
    edges.sort()
    #print(edges)
    return edges

# The main goal of this function is to return the mst edges calculated by kruskal's algorithm
# The function takes argument as edges
def kruskal_mst(edge):
    kruskal_edge_initial = []
    kruskal_edge_final = []
    edge_new = []
    mst = []
    for (cost,edge) in edge:
        edge_new.append(edge)
    for (edge_ini,edge_final) in edge_new:
        if(not((edge_ini in kruskal_edge_initial or edge_ini in kruskal_edge_final) and 
          (edge_final in kruskal_edge_final or edge_final in kruskal_edge_initial))):
            mst.append((edge_ini,edge_final))
            if(edge_ini not in kruskal_edge_initial):
                kruskal_edge_initial.append(edge_ini)
            if(edge_final not in kruskal_edge_final):
                kruskal_edge_final.append(edge_final)
        
    
    print(mst)

#main
example_graph =   [[(1,10),(2,1)],
                  [(0,10),(2,8),(4,1)],
                  [(0,1),(1,8),(3,1)],
                  [(2,1),(4,5),(5,2)],
                  [(1,1),(3,5),(5,1)],
                  [(3,2),(4,1)]]
                
example_graph_1 = [[(1,3),(2,1)],
                  [(0,3),(2,1),(3,8),(4,1)],
                  [(0,1),(1,1),(4,7)],
                  [(1,8),(4,4),(5,1)],
                  [(1,1),(2,7),(5,2),(3,4)],
                  [(3,1),(4,2)]]

edges = kruskal_algorithm(example_graph)
kruskal_mst(edges)
edges_1 = kruskal_algorithm(example_graph_1)
kruskal_mst(edges_1)

