#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" 
# instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".


# loop runs in the range i = 0 to 50
for i in range(51):
    #The if condition checks whether i %3,5 == 0 or not
    # continue returns to for i in range(51) 

    if(i % 3 == 0 and i % 5 ==0):
        print("FizzBuzz")
        continue

    elif (i % 3 == 0):
        print("Fizz")
        continue

    elif (i % 5 == 0):
        print("Buzz")
        continue

    else:
        print(i)
    
