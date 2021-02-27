# function print_tokens takes two arguments lex_string and lex_tokens
# when the loop is executed, it prints every element in lex_tokens
def print_tokens(lex_tokens):
    print("All tokens in the lexical string")
    print("---------------------------------")
    lst1 = []
    for l in lex_tokens:
        if (l == "\""):
            lst1.append(l)
        print(l)
        
    print("----------------------------------")
    return


# the function lexical analyser takes three arguments
# lex_string will have a python statement
# lex_delimit is of list type containing all the delimiters
# lex_tokens will get updated with all tokens in the lex_string
def lexical_analyser(lex_string,lex_delimit,lex_tokens):
    # Intalising str2 is empty and flag = 0
    str2 = ""
    flag = 0

    # The loop checks for ele in lex_ string == deli in lex_delimit
    # if ele != deli and flag!= 1, str2 is incremented with ele
    # if ele == deli prints elements matches delimiter
    # the characters present in str2 is incremented to lex_tokens and flag is set to 0
    for ele in lex_string:
        for deli in lex_delimit:
            if (ele == deli):
                # print("Element matches with delimiter")
                if(str2 != ""):
                    lex_tokens.append(str2)
                   
                lex_tokens.append(deli)
                flag = 1
                break
               
        if (flag == 1):
            str2 = ""
            flag = 0
        else:
            str2 += ele
    
    lex_tokens.append(str2)
    return

# the main goal of the function is to read every line from the file and print all the tokens
# the argument of funct_file is file
def funct_file(input_file, final_tokens):
    for x in input_file:
        # please add a line to ignore those that start with #
        if not x.startswith('#'):
            lex_string = x
        # Some delimiters
        lex_delimit = [" ",",",":","+","-","!","*","&","%",".","(",")","\n","=","==","\""]
        # lex_tokens is empty list
        lex_tokens = []
        #function call for lexical_analyser
        lexical_analyser(lex_string,lex_delimit,lex_tokens)
        # function call for print_tokens
        #print_tokens(lex_tokens)
        final_tokens.extend(lex_tokens)
    return

# thid function takes a some list with tokens and if it sees a token as ""
# it will remove that entry and all following entries till next ""
# all the removed entries will be added as single entry to the list at the same position


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

def backto_original(final_tokens2,file_path1):
    for i in final_tokens2:
        file_path1.write("%s" % i)

    return


# main function ----------------------------------
# importing file
input_file = open("F:\\python_scripts\\network Programming\\newserver.py",'r')
final_tokens=[]  
funct_file(input_file,final_tokens)   
print(final_tokens)
final_tokens_1 = final_tokens
print("******************* after modifying **********************")
modify_list_tokens_totakecarequotes(final_tokens_1)
print(final_tokens_1)


