# The main goal of the function is to find the input string from a string given
# The function takes input as a main string and sub string

def find_a_string(main_str,sub_str):
    # length variable stores the length of main string
    length = len(main_str)
    temp_str = ""
    count = 0
    for i in range(length-1):
        temp_str = main_str[i] + main_str[i+1]
        if(temp_str == sub_str):
            count = count + 1
        temp_str = ""
    
    return count

# main function
original_str = "karamekaramaka"
to_find = "ka"

# function call
count = find_a_string(original_str,to_find)
print("The no.of times that string" ,to_find, "repeated is : ",count)