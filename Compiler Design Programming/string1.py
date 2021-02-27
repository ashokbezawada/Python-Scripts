
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



def print_list(python_stmt, templist):
    print("*************************")
    print("given stmt:"+python_stmt)
    print("all tokens in this statement")
    for temp in templist:
        print(temp)
    print("*************************")
    return


#this function goal is to put all tokens into a list
#python_statement : a line in python code
#python_delimitters : all python delimitters
#tokens : this contains all the tokens in that line of python code

def lex_parse(python_statement, python_delimitters, tokens):
    tempstr =""
    flag = 0

    for character in python_statement:
        for delimitter_character in python_delimitters:
            if(character == delimitter_character):
                if(tempstr!=""):
                    tokens.append(tempstr)
                
                tokens.append(delimitter_character)
                flag = 1
                break
        
        if(flag == 1):
            tempstr = ""
            flag = 0
        else:
            tempstr += character
    
    tokens.append(tempstr)
    return


p_arg1 = "def find3(python_statement, python_delimitters, tokens):"
p_arg2 = " ():,+-=/%*.<>!&"

p_arg3 = []
lex_parse(p_arg1,p_arg2,p_arg3)
print_list(p_arg1,p_arg3)

ifstatement= 'if(tempstr!=""):'
lex_parse(ifstatement,p_arg2,p_arg3)
print_list(ifstatement,p_arg3)


# str2 = ""                           #creating a empty string str2
# str1 = "hell:,ashok:,sravya"       #created string str1 with values
# tokens1 = []                       # creating an empty list(tokens)
# delimiter = [":",","," "]  
#         # created a new list delimiter = [: , " "]
# arg1=str1
# arg2=" ,:"
# arg3=tokens1

# find(arg1,arg2,arg3)       #function call
# print(tokens1)                #printing tokens1


# tokens2=[]
# arg3=tokens2
# find1(arg1,arg2,arg3)
# print(tokens2)