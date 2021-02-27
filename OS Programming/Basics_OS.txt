import os

# How to get current working directory
# The function takes the argument as str
# The main goal of the function is to return the current working directory
curDir = ""
def toget_cwd(curDir):
    curDir = os.getcwd()
    print(curDir)
 
    return
toget_cwd(curDir)

# How to change directory
# the main goal of the function is to change the current working directory
# The function takes argument as string
navi = ""
def navi_cwd(navi):
    navi = os.chdir("F:/python_scripts/")
    print(os.getcwd())

    return

navi_cwd(navi)

# How to see what are the folders present working directory
# The main goal of the function is to print all the files
# The function takes argument as str

pri_all = ""
def print1_all(pri_all):
    pri_all = os.listdir()
    print(pri_all)

    return
print1_all(pri_all)


# How to create a new folder 
# The main goal of the function is create a file
# The function takes argument as string

makedir = ""
def create1_new(makedir):
    makedir = os.mkdir('os testing')
    print(makedir)

    return

create1_new(makedir)

# How to delete folders
# The main goal of the function is to delete a file
# the function takes argument as string
remove_dir = ""
def delete1_dir(remove_dir):
    remove_dir = os.rmdir('os testing')
    print(os.listdir())

    return

delete1_dir(remove_dir)

# How to rename a file
# The main goal of the function is to change the name of a file
# The function takes argument as str
cha_name = ""
def rename1_file(cha_name):
    cha_name = os.rename('os testing','os testing1')
    print(os.listdir())
    return
rename1_file(cha_name)

# How to open a word file
# The main goal of the function is to open
# The function takes argument as str
str1 = ""
def open_fil(str1):
    str1 = os.system("notepad.exe")
    print("executed")

    return

open_fil(str1)