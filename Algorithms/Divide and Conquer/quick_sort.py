# The main goal of this function is to sort the array by implementing quick sort algorithm

def quick_sort(array,start,end):
    if len(array) == 1:
        return array
    if start < end:
        # to get the index of pivot after rearrangement
        p_index = partition(array,start,end)
        # to sort the segement left of partition index
        quick_sort(array,start,p_index-1)
        # To sort the segement right of partition index
        quick_sort(array,p_index+1,end)
        #return array

# The main goal of this function is to partition the array using pivot
# partition in such a way that all graeater than pivot are on right, all elements lesser than pivot are on left

def partition(array,start,end):
    pivot = array[end]
    p_index = start - 1
    for i in range(start, end):
        if (array[i] <= pivot):
            p_index = p_index + 1
            array[p_index], array[i] = array[i],array[p_index]
    array[p_index + 1],array[end] = array[end],array[p_index + 1]
    return p_index + 1

#main
array = [7,6,5,4,3,2,1,0]
n = len(array)
quick_sort(array,0,n-1)
n = len(array)
for i in range(n):
    print(array[i])