# The function print_list takes two arguments python_stmt and templist
# first it prints stars then python stmt
# prints all tokens in the statement
# prints each element in temp list 


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

# we are intialising tempstr as empty string and flag = 0
# the foor loop executes for the each character in python statement
# checks whether that character is present in python_delimiters or not
# if the character doesn't match checks whether flag = 1 or not
# appends the character in tempstr
# if python_stmt = python_delimiter 
# tokens will get get appeneded with characters present in tempstr
#      and flag set to 1 and temp str is changed to empty str
 
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
