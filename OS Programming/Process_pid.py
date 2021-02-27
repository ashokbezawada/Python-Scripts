import os
from multiprocessing import Process, current_process

# Function to find square 
# The function takes argument as number from the list

def square(number):
    result = number*number
    # we can use os module to print process id
    process_id = os.getpid()
    print(f"the process id: ", process_id)

    print(f"The number {number} squares to {result}.")

if __name__ == '__main__':

    processes = []
    numbers = [1,2,3,4]

    for number in numbers:
        process = Process(target = square, args=(number,)) 
        processes.append(process)

        process.start()