import sys
#The main goal of the function is to print the maximum coins required for given denomination
#The function takes argument as the required number which is x and returns the final list
def minimum_denom(x):
    coins  = [1,3,4]
    y = x + 1
    lst = [sys.maxsize]*y
    lst[0] = 0
    for i in coins:
        lst[i] = 1
    for i in range(y):
        if(i != 0 and i!= 1 and i!=3 and i!=4):
            no_of_coins = sys.maxsize
            for coin in coins:
                if(coin <= i):
                    min = i - coin
                    y = lst[min] + 1
                    if(y < no_of_coins):
                        no_of_coins = y
                    lst[i] = no_of_coins
    return lst

# The main goal of the function is to find what are the final denominations present in minimum coins given
# The function takes argument as list and number and returns denominations list
def coins_in_min_denominations(lst,x):
    coins = [1,3,4]
    final_coins = []
    min_no_of_coins = lst[x]
    new_min = sys.maxsize
    while(new_min != 0):
        new_min = sys.maxsize
        for coin in coins:
            min = x - coin
            if(min < new_min):
                new_min = min
                if(min_no_of_coins == lst[new_min] + 1):
                    final_coins.append(coin)
                    x = new_min
                    min_no_of_coins = lst[x]
                    break
    
    return final_coins
    

#main
test_lst = [5,6,7,8,9,10,12,13,14,15]
for i in test_lst:
    x = i 
    lst = minimum_denom(x)
    final_coins = coins_in_min_denominations(lst,x)
    print("The minimum coins required for" ,x, "is",lst[x])
    print("The coins denominations for " ,x,  "is" ,final_coins)
    if(lst[x] == len(final_coins)):
        print("The function is properly working")
    else:
        print("SOMETHING IS WRONG PLEASE CHECK AGAIN")
