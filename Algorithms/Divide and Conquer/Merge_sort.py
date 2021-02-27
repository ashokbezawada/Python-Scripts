# The main goal of this function is to divide the lists into sub lists 
# and pass left and right sub lists values into merge sort function
# The function takes argument as array
def merge_sort(arr):
    length = len(arr)
    if (length > 1):
        mid = length//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left,right,arr)

    return arr

# The main goal of this function is to sort the unsorted array 
# The function takes argument as left right and main array

def merge(left,right,arr):
    left_length = len(left)
    right_length = len(right)
    i = j = k = 0
    while(i < left_length and j < right_length):
        if(left[i] <= right[j]):
            arr[k] = left[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = right[j]
            k = k + 1
            j = j + 1
        
    # if any of the sublists exhaust we have to process the list which contains elements in it
    while(i < left_length):
        arr[k] = left[i]
        i = i + 1
        k = k + 1
        
    while(j < right_length):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


#main
sorted_arr = merge_sort([2,4,1,6,8,5,3,7])
print(sorted_arr)



