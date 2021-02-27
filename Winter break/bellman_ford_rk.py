import sys

 

def bellmanford(graph:[[()]],source) -> ([],[]):

    distance=[sys.maxsize for _ in range(len(graph))]

    prenode = ['none' for _ in range(len(graph))]

    distance[source] = 0

    prenode[source] = source

   

    for x in range(len(graph)-1):

        for i in range(len(graph)):

            for(neighbor,n_distance) in graph[i]:

                if (distance[i]+n_distance < distance[neighbor]):

                    distance[neighbor] = distance[i]+n_distance

                    prenode[neighbor] = i

    return (distance,prenode)

 

#main

example_graph = [[(1,10),(2,1)],

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

(distance,prenode) = bellmanford(example_graph_1,0)

print("printing distances from source 0") 

print(distance)

print("printing the prenodes to reach from source 0 to every node")

print(prenode)