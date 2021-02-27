input_file = open("F:\\python_scripts\\hello.txt",'r')

def new_funct(input_file):
    for x in input_file:
        line = input_file.readline()
        while(line = ''):
            print(line)
            line=input_file.readline()

    
    return 

new_funct(input_file)
 
