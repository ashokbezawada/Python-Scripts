import threading
# function to create a file and put a character a init
def file_function(number):
    filepath="F:\\python_scripts\\Os Programming\\temp\\"+str(1)
    input_file = open(filepath,'a')
    input_file.write("ashok")
    input_file.close()


t1 = threading.Thread(target=file_function, args=[1])
t1.start()
t1.is_alive()
t1.join()
print("thread killed")


