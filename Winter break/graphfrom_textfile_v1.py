# The main goal of this function is it will return all cities present in a text file
# The function takes argument as file path
def graphfrom_textfile_f1(file):
    cities = []
    new_cities_graph = []
    for line in file:
        new_line = line.split()
        for i in new_line:
            if i not in cities:
                if (i.isnumeric()) == False:
                    cities.append(i)
    for i in range(len(cities)):
        i = []
        new_cities_graph.append(i)
    
    return(cities,new_cities_graph)

# The main goal of the function is to create graph with help of lists
# The function takes arguments lists and file_path
def graphfrom_textfile_f2(cities,new_cities_graph,file_1):
    for line in file_1:
        new_line = line.split()
        for city in new_line:
            if city in cities:
                city_index = cities.index(city)
                for new_city in new_line:
                    if(city != new_city and new_city.isnumeric() == False):
                        new_city_index = cities.index(new_city)
                    if (new_city.isnumeric()) == True:
                        distance = int(new_city)
                        #print(distance)
            new_cities_graph[city_index].append((new_city_index,distance))
            break
    
    return new_cities_graph

    
# Main
input_file = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
new_lists = graphfrom_textfile_f1(input_file)
input_file_1 = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
new_cities_graph = graphfrom_textfile_f2(new_lists[0],new_lists[1],input_file_1)
print(new_cities_graph)

