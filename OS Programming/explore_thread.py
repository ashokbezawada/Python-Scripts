import threading


# function to create a file and put a character a init
def file_function(number):
    i=0
    while(True):
        i = i+1
        filepath="F:\\python_scripts\\Os Programming\\temp\\"+str(i)
        input_file = open(filepath,'a')
        input_file.write("ashok")
        input_file.close()


for i in range(1000):
    t1 = threading.Thread(target=file_function, args=[1])
    t1.start()
#str1 = input("enter something : ")
#while True:
    #print(str1)
# when i kept thread creation in loop it created 884 threads, and used 64% of cpu
