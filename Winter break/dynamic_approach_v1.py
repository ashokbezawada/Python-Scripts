import sys
#The main goal of the function is to print the maximum coins required for given denomination
#The function takes argument as the required number which is x and returns the final list
# def minimum_denom(x):
#     coins  = [1,3,4]
#     y = x + 1
#     lst = [sys.maxsize]*y
#     lst[0] = 0
#     for i in coins:
#         lst[i] = 1
#     for i in range(y):
#         if(i != 0 and i!= 1 and i!=3 and i!=4):
#             no_of_coins = sys.maxsize
#             for coin in coins:
#                 if(coin <= i):
#                     min = i - coin
#                     y = lst[min] + 1
#                     if(y < no_of_coins):
#                         no_of_coins = y
#                     lst[i] = no_of_coins
#     return lst

def minimum_denom_coins(x):
    coins  = [1,3,4]
    y = x + 1
    coins_lst = [sys.maxsize]*y
    lst = [sys.maxsize]*y
    lst[0] = 0
    for i in coins:
        lst[i] = 1
    
    for i in  range(y):
        coins_lst[i] = []
        if(i == 0):
            coins_lst[i].append(0)
        if(i == 1):
            coins_lst[i].append(1)
        if(i == 3):
            coins_lst[i].append(3)
        if(i == 4):
            coins_lst[i].append(4)
    
    for i in range(y):
        if(i != 0 and i!= 1 and i!=3 and i!=4):
            no_of_coins = sys.maxsize
            for coin in coins:
                if(coin <= i):
                    min = i - coin
                    y = lst[min] + 1
                    if(y < no_of_coins):
                        no_of_coins = y
                        new_min = min
                        new_coin = coin
                    lst[i] = no_of_coins
           
            coins_lst[i] = coins_lst[new_min] + coins_lst[new_coin]
    return (lst,coins_lst)


#main
x = 17
(final_list,final_coins) = minimum_denom_coins(x)
print(final_list)
print("The minimum coins required for" ,x, "is :" ,final_list[x])
print(final_coins)
print("The minimum denominations required for" ,x, "is :" ,final_coins[x])