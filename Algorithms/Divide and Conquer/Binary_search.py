# The main goal of this function is to search an element in the array by reducing the size of array in half
# The function takes argument as array and search number

def binary_search(lst,search_number):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + (end -1))//2
        if lst[mid] == search_number:
            return mid
        # if the search number is greater ignore the left half
        elif lst[mid] < search_number:
                start = mid + 1
        # if search number is lesser ignore the right half
        else:
            if lst[mid] > search_number:
                end = mid -1
    
    return False


# main
lst = [1,20,89,100,150]
num = 89

x = binary_search(lst,num)
print(lst[x])
