# The main goal of the function is to find the minimum spanning tree
# The function takes arguments as graph and source and returns the final path
def prims_algo(graph,source):
    all_vertices = []
    prims_vertices = []
    final_path = []
    distance = 999999
    current = source
    length = len(graph)
    for i in range(length):
        all_vertices.append(i)
    all_vertices[current] = 0
    all_vertices.remove(current)
    prims_vertices.append(current)
    while (len(all_vertices) > 1):
        if current not in all_vertices:
            for neighbours   in graph[current]:
                min_node = neighbours[0]
                minimum_distance = neighbours[1]
                if(minimum_distance <= distance):
                    distance = minimum_distance
                    min_node = neighbours[0]
        prims_vertices.append(min_node)
        all_vertices.remove(min_node)
        current = min_node
    final_path = prims_vertices + all_vertices
    return final_path



example_graph = [[(1,10),(2,1)],
                 [(0,10),(2,8),(4,1)],
                 [(0,1),(1,8),(3,1)],
                 [(2,1),(4,5),(5,2)],
                 [(1,1),(3,5),(3,2)],
                 [(3,2),(4,1)]]

final_path = prims_algo(example_graph,0)
print(final_path)