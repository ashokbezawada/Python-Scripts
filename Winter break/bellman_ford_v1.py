def bellman_ford(graph):
    all_vertices = []
    #bellmanford_vertices = []
    shortest_distance_0 = {}
    shortest_distance_1 = {}
    shortest_distance_2 = {}
    shortest_distance_3 = {}
    shortest_distance_4 = {}
    shortest_distance_5 = {}
    previous_node_0 = {}
    previous_node_1 = {}
    previous_node_2 = {}
    previous_node_3 = {}
    previous_node_4 = {}
    previous_node_5 = {}
    length = len(graph)
    for i in range(length):
        all_vertices.append(i)
        shortest_distance_0[i] = 999999
        shortest_distance_1[i] = 999999
        shortest_distance_2[i] = 999999
        shortest_distance_3[i] = 999999
        shortest_distance_4[i] = 999999
        shortest_distance_5[i] = 999999
        previous_node_0[i] = 'udf'
        previous_node_1[i] = 'udf'
        previous_node_2[i] = 'udf'
        previous_node_3[i] = 'udf'
        previous_node_4[i] = 'udf'
        previous_node_5[i] = 'udf' 
        
    shortest_distance_0[0] = 0
    shortest_distance_1[1] = 0
    shortest_distance_2[2] = 0
    shortest_distance_3[3] = 0
    shortest_distance_4[4] = 0
    shortest_distance_5[5] = 0
    for i in all_vertices:
        for neighbours in graph[i]:
            node = neighbours[0]
            distance = neighbours[1]
            if(i == 0):
                if(distance < shortest_distance_0[i]):
                    shortest_distance_0[i] = distance
                    previous_node_0[i] = node
            if(i == 1):
                if(distance < shortest_distance_0[i]):
                    shortest_distance_1[i] = distance
                    previous_node_1[i] = node
            if(i == 2):
                if(distance < shortest_distance_0[i]):
                    shortest_distance_2[i] = distance
                    previous_node_2[i] = node
            if(i == 3):
                if(distance < shortest_distance_0[i]):
                    shortest_distance_3[i] = distance
                    previous_node_3[i] = node
            if(i == 4):
                if(distance < shortest_distance_0[i]):
                    shortest_distance_4[i] = distance
                    previous_node_4[i] = node
            if(i == 5):
                if(distance < shortest_distance_0[i]):
                    shortest_distance_5[i] = distance
                    previous_node_5[i] = node
    
    print(shortest_distance_0)
    print(shortest_distance_1)
    print(shortest_distance_2)
    print(shortest_distance_3)
    print(shortest_distance_4)
    print(shortest_distance_5)
example_graph =  [[(1,10),(2,1)],
                  [(0,10),(2,8),(4,1)],
                  [(0,1),(1,8),(3,1)],
                  [(2,1),(4,5),(5,2)],
                  [(1,1),(3,5),(5,1)],
                  [(3,2),(4,1)]]
bellman_ford(example_graph)