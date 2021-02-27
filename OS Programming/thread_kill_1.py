import threading
import time
# function to create a file and put a character a init
#def file_function(number):
    #filepath="F:\\python_scripts\\Os Programming\\temp\\"+str(i)
    #input_file = open(filepath,'a')
    #input_file.write("ashok")
    #input_file.close()

#for i in range(10):
    #t1 = threading.Thread(target=file_function, args=[1])
    #t1.start()
    #t1.is_alive()
    #t1.join()
    #print("thread killed")

def file_function_1(number):
    file_path = "F:\\python_scripts\\Os Programming\\temp1\\" +str(1)
    input_file = open(file_path, 'a')
    input_file.write("this is test1")
    input_file.close()

t2 = threading.Thread(target=file_function_1, args=[1])
t2.start


