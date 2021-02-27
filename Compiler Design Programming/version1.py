def find(str1,delimiter,tokens):           #creating a function that takes one argument as string and other as delimiter and tokens

    str2 = ""                              # creating an empty string str2
    for i in str1:                         # the loop runs for each value of str1 and stores in i
        for l in delimiter:                #  The loop runs for each of value of delimiter  
            if(l == i):                    #   checks whether l == i
                print("hit delimiter")
                
                tokens.append(str2)
                str2 = ""
            elif(l != i):
                str2 = str2 + i
    tokens.append(str2)       
    return


str2 = ""                           #creating a empty string str2
str1 = "hell:,ashok:,sravya"       #created string str1 with values
tokens1 = []                       # creating an empty list(tokens)
delimiter = [":",","," "]  
# created a new list delimiter = [: , " "]
arg1=str1
arg2=" ,:"
arg3=tokens1

find(arg1,arg2,arg3)       #function call
print(tokens1)                #printing tokens1
