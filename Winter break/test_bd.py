# The main goal of the function is to return the shortest distance from every node
import sys
# The main goal of the function is to generate a matrix which contains large values
# The function takes input as no.of rows and columns and returns matrix
def get_matrix(r,c):
    matrix = []
    for i in range(r):
        a = []
        for j in range(c):
            if(i == j):
                a.append(0)
            else:
                a.append(sys.maxsize)
        matrix.append(a)
    
    return matrix

# The main goal of this function is complete the 1st iteration in bellman ford problem
# The function takes argument as graph
def bellman_ford_f1(graph):
    need_matrix = get_matrix(r,c)
    length = len(graph)
    for i in range(length):
        for (node,distance) in graph[i]:
            if(distance < need_matrix[i][node]):
                need_matrix[i][node] = distance
    
    return need_matrix
#The main goal of this function is to complete all the iterations for bellman ford algorithm
# The function takes argumenst as matrix and graph
def bellman_ford_f2(req_matrix,graph):
    length_1 = len(graph)
    for j in range(length_1 - 1):
        for i in range(length_1):
            for (node,distance) in graph[i]:
                for final in range(length_1):
                    if(distance + req_matrix[node][final] < req_matrix[i][final]):
                        req_matrix[i][final] = distance + req_matrix[node][final]
    return req_matrix

# The main goal of this function is to return shortest distances from all vertices
# The function takes argument as matrix
def final_distance(final_matrix):
    for i in range(r):
        for j in range(c):
            print(final_matrix[i][j], end = " ")
        print()

# Main function
r = int(input("enter no.of rows which is same no.of nodes in graph : "))
c = int(input("enter no.of columns which is same no.of nodes in graph : "))

example_graph = [[(1,3),(2,1)],
                 [(0,3),(2,1),(3,8),(4,1)],
                 [(0,1),(1,1),(4,7)],
                 [(1,8),(4,4),(5,1)],
                 [(1,1),(2,7),(5,2),(3,4)],
                 [(3,1),(4,2)]]

req_matrix = bellman_ford_f1(example_graph)

shortest_distance = bellman_ford_f2(req_matrix,example_graph)

#Printing shortest distance from every node:
final_distance(shortest_distance)