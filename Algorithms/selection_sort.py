# The main goal of this function is to sort the array in increasing order
# The function takes argument as array
import sys
def selection_sort(arr):
    sorted_array = []
    length = len(arr)
    while(len(sorted_array) < length):
        check_num = sys.maxsize
        for i in arr:
            if(i < check_num):
                check_num = i
        if check_num not in sorted_array:
            sorted_array.append(check_num)
            arr.remove(check_num)
    return sorted_array

# The main goal of this function is to sort the array in increasing order
# The function takes argument as array
def selection_sort_new(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i,length):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

# main
arr= [87,10,91,4,1]
final_arr = selection_sort(arr)
arr_new = [87,10,91,4,1]
sort_arr = selection_sort_new(arr_new)
print(sort_arr)

if (final_arr == sort_arr):
    print("both functions working correctly")
                



  
