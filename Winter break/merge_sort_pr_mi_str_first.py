# The main goal of this function is to compare the elements in both the lists and update them into a final lst
# The function takes argument as three lists and returns list
def merge(l_lst,r_lst,lst):
    l_length = len(l_lst)
    r_length = len(r_lst)
    i=j=k=0
    while(i < l_length and j < r_length):
        if(l_lst[i] <= r_lst[j]):
            lst[k] = l_lst[i]
            i = i + 1
        else:
            lst[k] = r_lst[j]
            j = j + 1
        k = k + 1
    # The above condition only works till the length of l_list, any of the left or right lists will have no more elements 
    # to process, in that case we need to pick the elements from unprocessed list
    while(i < l_length):
        lst[k] = l_lst[i]
        i = i + 1
        k = k + 1

    while(j < r_length):
        lst[k] = r_lst[j]
        j = j + 1
        k = k + 1


# The main goal of this function is to divide the list into equal halves until length of the list is 1
# The function takes argument as list and returns the sorted lst
def merge_sort(lst):
    length = len(lst)
    if (length > 1):
        middle = length//2
        left_lst = lst[:middle]
        right_lst = lst[middle:]

        # recursion calls
        merge_sort(left_lst)
        merge_sort(right_lst)
        #function call to sort
        merge(left_lst,right_lst,lst)

    return lst

# The main goal of this function is to print the strings in ascending order 
# The function takes argument as lst
def print_min_string(lst):
    test_lst = []
    test_lst_1 = []
    for i in lst:
        test_lst.append(len(i))
        test_lst_1.append(len(i))

    sort_lst = merge_sort(test_lst)

    for i in sort_lst:
        for j in test_lst_1:
            if(i == j):
                x = test_lst_1.index(j)
                print(lst[x])
                test_lst_1[x] = ''
                break
   




#main 
#lst = ["str","a","ab","abcde","asd","aa"]
lst = ["strasd","abb","aa","a","asd","aa"]
print_min_string(lst)

