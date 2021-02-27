# define a delimiter function which seperates the values of string based on the delimiter intialized

#define a function that takes one argument as string and another argument as delimmiter, it prints the string delimmited by that delimmited
#example:
#argument1 = "ashok sravya", argument2 = " " ==> prints ashok sravya


str2=""
str1 = "hell:,,,ashok:,sravya"
tokens1=[]

def find(str1,delimiter,tokens):
    str2 = ""
    for k in str1:
        if (delimiter == k):
            tokens.append(str2)
            str2 = ""
            continue
        str2 = str2 + k
    
    tokens.append(str2)
    return 

find(str1,":",tokens1)
print(tokens1)
tokens1=[]





  




