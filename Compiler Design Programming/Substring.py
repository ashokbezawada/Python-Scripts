string1 = "ASHok"
string2 = "OK"

# The goal of this function is to check whether string2 is present in string1 irrespective of case
# function verify takes two arguments string1 and string2
# it returns true or false
def verify(string1,string2):
    # The function lower() converts the characters present in string1 to lower case and assigns it to a
    a = string1.lower()
    # The function lower() converts the characters present in string2 to lower case and assigns it to b
    b = string2.lower()
    # The if condition checks whether ok is present in a, if present returns true else returns false
    if b in a:
        return "true"
    return "false"
     
while True:
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    print(string2+" in "+string1+" : "+verify(string1,string2))




