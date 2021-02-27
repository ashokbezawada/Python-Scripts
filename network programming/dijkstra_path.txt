def find_path(previous_destinations,source,destination):
    #previous_node[0] = 0
    lst2 = []
    lst2.append(destination)
    while (lst2[-1] != source):
        lst2.append(previous_destinations[destination])
        if(lst2[-1] != source):
            lst2.append(previous_destinations[lst2[-1]])
            destination = lst2[-1]

    return lst2

def find_path_3(previous_destinations,source,destination):
    lst1 = []
    lst1.append(destination)
    while(destination != source):
        lst1.append(previous_destinations[destination])
        destination = lst1[-1]
    print(lst1)
    

 
previous_destinations = {'seattle':'spokane', 'spokane':'montana','montana':'denver','denver':'dallas','dallas':'austin'}
lst2 = find_path(previous_destinations,'austin','seattle')
print(lst2)

def find_path_1(previous_destinations,source,destination):
    lst1 = []
    lst1.append(destination)
    while(lst1[-1] != source):
        lst1.append(previous_destinations[lst1[-1]])
    print(lst1)

lst2 = find_path(previous_destinations,'austin','seattle')
find_path_3(previous_destinations,'austin','seattle')
find_path_1(previous_destinations,'austin','seattle')