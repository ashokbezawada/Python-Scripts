import threading

def file_function(number):
    filepath="F:\\python_scripts\\Os Programming\\temp\\"+str(number)
    input_file = open(filepath,'a')
    input_file.write("ashok")
    input_file.close()

file_function(1)
