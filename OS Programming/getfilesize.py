import os
# The main goal of the function is to find the no.of files and directories in a file
# The function takes as argument as path of the file
def find_dir(Path):
    dirCount = 0
    fileCount = 0
    for root, dirs, files in os.walk(Path):
        print("path :", root)
        for directories in Path:
            dirCount += 1
        for files in Path:
            fileCount += 1
    print("Number of files : ", fileCount)
    print("Number of directories : ", dirCount)
    print("total :", (dirCount+fileCount))

    return

    
#Main function
Path = input("Enter the path: ")
find_dir(Path)


