input_file = open("F:\\python_scripts\\network programming\\city_assignment.txt",'r')
str1 = ""
lst1 = []
lst2 = []
for line in input_file:
    new_line = line
    new_line.replace('\n', '')
    for i in new_line:
        if(i!= ','):
            str1 = str1 + i
            continue
        lst1.append(str1)
        lst2.append(str1    )
    print(lst1)
    print(lst2) 
  

#         if(i!= ','):
#             str1 = str1 + i
#             continue
#         lst1.append(str1)
#         lst2.append(str1)
#         if(i == ','):
#             str1 = ""
# for i in lst1:
#     i = dict()
# input_file.close()