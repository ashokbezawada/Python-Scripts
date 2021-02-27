# following program reads from a file with below format and turns that into adjescent graph

# city1 city2 100 -> this means distance b/w city1 and city2 is 100

# it produces an adjescent graph on which dijkstras and bellmanford algorithms can be run

 

def addtodict(city:str,graph:[],dt:dict,vertex:int):

    if city in dt: return vertex

    dt[city] = vertex

    graph.append([])

    vertex=vertex+1

    return vertex

 

def makeagraph(filename:str) -> [[()]]:

    dt = dict()

    graph=[]

    vertex=0

    #rf=open(filename)

    rf = filename

    for line in rf:

        if not line: break

        (city1,city2,distance) = line.split()

        vertex = addtodict(city1,graph,dt,vertex)

        vertex = addtodict(city2,graph,dt,vertex)

        graph[dt[city1]].append((dt[city2],int(distance)))

        #graph[dt[city2]].append((dt[city1],int(distance)))

        #break

    rf.close()

    return graph,dt

 

# main

#filename = "c:\\temp\\city_assignment.txt"

filename = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')

g,dt = makeagraph(filename)

print(g)

print(dt)