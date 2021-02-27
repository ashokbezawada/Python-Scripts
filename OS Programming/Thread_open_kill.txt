import threading
import time
# function to create a file and put a character a init
def file_function(number):
    filepath="F:\\python_scripts\\Os Programming\\temp1\\"+str(number)
    input_file = open(filepath,'a')
    input_file.write("ashok")
    input_file.close()

def sleep_function(number=10):
    time.sleep(number)

threadlist=[]

# creating 5 threads and storing them in a list
for i in range(5):
    t1 = threading.Thread(target=file_function, args=[i])
    threadlist.append(t1)
    t1.start()

print(i)

th1 = threading.Thread(target=sleep_function)
threadlist.append(th1)
th1.start()

# waiting for each thread to complete 
for i in threadlist:
    i.join()
print(i)

print("ashok")  
   