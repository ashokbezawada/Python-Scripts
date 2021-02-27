# The main goal of this function is to reverse the string without affecting the special characters
# The function takes argument as a string and returns the reversed string
def reverse_spl_character(str):
    lst = []
    str2 = ""
    length = len(str)
    temp = length - 1
    from_left = 0
    
    # to compare the characters from left and right i am appending each character in string to list
    for i in str:
        lst.append(i)

    while from_left < temp:
        if (lst[from_left].isalpha() == False):
            from_left = from_left + 1

        elif (lst[temp].isalpha() == False):
            temp = temp - 1
        
        else:
            swap_temp = lst[temp]
            lst[temp] = lst[from_left]
            lst[from_left] = swap_temp
            from_left = from_left + 1
            temp = temp - 1

    for i in lst:
        str2 = str2 + i
    
    
    return str2



#main
# test_str ="ad!c"
test_str = "a!!!b.c.d,e'f,ghi"
revr_str = reverse_spl_character(test_str)
final_str = "i!!!h.g.f,e'd,cba"

#test case
if(revr_str == final_str):
    print("Function working properly")
else:
    print("error")
