def steps(lst,total_steps):
    possibility_lst = []
    result = 0
    for x in range(1,lst[-1]+1):
        for y in  range(1,lst[-1]+1):
            for z in  range(1,lst[-1]+1):
                for c in range(0,2):
                    if((x) + (y) + (z) + (c)== total_steps):
                        print(x, "---------",y,"----------",z,"---------------",c)
                        result = result + 1
    print(result)
    return possibility_lst


#main
total_steps_lst = [1,2,3]
total_steps = 4
final_lst = steps(total_steps_lst,total_steps)
print("The possible ways to print the no.of final steps is : ",final_lst)
