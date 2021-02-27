def binary_search(lst,req_num):
    length = len(lst)
    initial = 0
    final = length - 1
    
    while(initial <= final):
        middle = (initial + final)//2
        if (req_num == lst[middle]):
            print("The number found at index",middle)
            break
        else:
            if(req_num < lst[middle]):
                final = middle - 1
            else:
                initial = middle + 1
    return middle

lst = [10,20,30,40,50,60,70,80,90,100,110]
req_numbers = [10,60,80,110]
for i in req_numbers:
    req_index = binary_search(lst,i)
    if(i == 10):
        index = 0
        if(req_index == index):
            print("The function worked correctly: ",req_index,"and" ,index)
    if(i == 60):
        index = 5
        if(req_index == index):
            print("The function worked correctly")
    if(i == 80):
        index = 7
        if(req_index == index):
            print("The function worked correctly")
    if(i == 110):
        index = 10
        if(req_index == index):
            print("The function worked correctly")
    