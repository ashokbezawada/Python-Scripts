# followng program for prims algorithm
from random import randint
import sys
# below function will find the low cost edge from visited_vertices
# by checking all edges from those vertices
# arguments:
# graph: list of list of tuples
# visited_vertices: list of vertices from which to find next lowcost edge
# returns an edge as a tuple

def find_lowcost_edge(graph: [[()]], visited_vertices: []) -> ():
    min_cost = sys.maxsize
    for vertex in visited_vertices:
        for(neighbour_vertex, neighbor_cost) in graph[vertex]:
            if(neighbour_vertex not in visited_vertices and neighbor_cost < min_cost):
                min_cost = neighbor_cost
                min_vertex1 = vertex
                min_vertex2 = neighbour_vertex

    return (min_vertex1, min_vertex2)

 

# given a graph returns list of edges by following
# prims algorithm for minimum spanning tree
# graph: list of list of tuples
# returns list of edges as list of tuples

def prims(graph: [[()]]) -> [()]:
    prim_vertices = [randint(0, len(graph)-1)]
    prim_edges = []
    while(len(prim_vertices) != len(graph)):
        low_cost_edge = find_lowcost_edge(graph,prim_vertices)
        prim_edges.append(low_cost_edge)
        prim_vertices.append(low_cost_edge[1])

    return prim_edges

 

# main
example_graph = [[(1,10),(2,1)],

                 [(0,10),(2,8),(4,1)],

                 [(0,1),(1,8),(3,1)],

                 [(2,1),(4,5),(5,2)],

                 [(1,1),(3,5),(5,1)],

                 [(3,2),(4,1)]]

mst_edges = prims(example_graph)
print(mst_edges)

example_graph1 = [[(1,7),(2,8)],

                  [(0,7),(2,3),(3,6)],

                  [(0,8),(1,3),(3,4),(4,3)],

                  [(1,6),(2,4),(4,2),(5,5)],

                  [(2,3),(3,2),(5,2)],

                  [(3,5),(4,2)]

                 ]

mst_edges = prims(example_graph1)
print(mst_edges)

