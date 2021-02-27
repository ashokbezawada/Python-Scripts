import sys
# The main goal of the function is to fibonacci series
# The function takes argument as number and returns fibonacci list
def fibonaci_dynamic_approach(x):
    total = x + 1
    fib_lst = [sys.maxsize]*total
    
    fib_lst[0] = 0
    fib_lst[1] = 1
    fib_lst[2] = 1
     
    for i in range(total):
        if (i != 0 and i != 1 and i != 2):
            while(i <= total):
                x = fib_lst[i-1] + fib_lst[i - 2]
                fib_lst[i] = x
                break
    
    return fib_lst


#main 
x = 10
fib_list = fibonaci_dynamic_approach(x)
print("The number present in fibonacci series in position" ,x, "is :",fib_list[x])
print(fib_list)