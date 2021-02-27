def find1(str1, delimiter, tokens):
    str2=""
    flag=0

    for i in str1:
        for l in delimiter:
            if(l==i):
                print("hit delimitter")
                if(str2 != ""):
                    tokens.append(str2)
                str2 = ""
                flag=1
        if(flag != 1):
            str2=str2+i
        else:
            flag=0

    tokens.append(str2)
    return

str2 = ""                        
str1 = "hell:,ashok:,sravya"       
tokens1 = []                  
delimiter = [":",","," "]

# created a new list delimiter = [: , " "]
arg1=str1
arg2=" ,:"


tokens2=[]
arg3=tokens2
find1(arg1,arg2,arg3)
print(tokens2)