# The main goal of this function is to sort the array in increasing order
# The function takes argument as array

def insertion_sort(arr):
    length = len(arr)
    for i in range(1,length):
        value = arr[i]
        current = i
        while(current > 0 and arr[current-1]>value):
            arr[current] = arr[current-1]
            current = current - 1 
        arr[current] = value
    return arr

# main 
lst = [89,56,100,10,1]
sorted_arr = insertion_sort(lst)
print(sorted_arr)

