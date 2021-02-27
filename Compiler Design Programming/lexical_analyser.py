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

# The main goal of the function is to remove the comments in start of a line and in middle
# the function takes arguments input_file,le_str1,final_tokens
def funct_file(input_file,le_str1,final_tokens):
    flag = 0
    str2 = ""
    str3 = ""
    # to read every line in input file
    for x in input_file:
        # to read every element in the line                   
        for i in x:
            if( i!= '#' and flag == 0):
                le_str1 = le_str1 + i
            if( i == '#'):
                str2 = str2 + i
                
                flag = 1
            if(flag == 1):
                str3 = str3 + i
                flag = 1
        flag = 0
        lex_string = le_str1
        le_str1 = ""
         # Some delimiters
        lex_delimit = [" ",",",":","+","-","!","*","&","%",".","(",")","\n","=","==","\""]
        # lex_tokens is empty list
        lex_tokens = []
        #function call for lexical_analyser
        lex_parse(lex_string,lex_delimit,lex_tokens)
        # function call for print_tokens
        #print_tokens(lex_tokens)
        final_tokens.extend(lex_tokens)

    return  


# below function takes care of putting together strings
def modify_list_tokens_totakecarequotes (l_tokens):
    le_tok=[]
    str1=""
    listlength= len(l_tokens)
    i=0
    while(i < listlength):
        current = l_tokens[i]
        if(current != "\""):
            le_tok.append(current)
        else:
            str1 = str1+current
            while(i+1 < listlength):
                i = i+1
                str1 = str1 + l_tokens[i]
                if(l_tokens[i] == "\""):
                    le_tok.append(str1)
                    str1=""
                    break
        i = i + 1
            
    l_tokens = le_tok
    return


# The main goal of the function is to form an original content after doing lexical analysis with help of final tokens
# The function takes argument as file_path1,final_tokens2
def backto_original(final_tokens2,file_path1):
    for i in final_tokens2:
        file_path1.write("%s" % i)

    return


# main function
input_file = open("F:\\python_scripts\\network Programming\\newserver.py",'r')
final_tokens=[]  
le_str1 = ""
funct_file(input_file,le_str1,final_tokens)   
print(final_tokens)
final_tokens1 = final_tokens
modify_list_tokens_totakecarequotes(final_tokens1)
print("*********after taking care of double quotes******")
print(final_tokens1)
lexical_string = ""

final_tokens2 = []
file_path1 = open("F:\\python_scripts\\Compiler Design Programming\\lexical_analysis_test.txt",'a+')
final_tokens2 = final_tokens1
backto_original(final_tokens2,file_path1)





