import subprocess

# The goal of the function is to open a process
def open_proc(process_name):
    pid = subprocess.Popen(process_name)
    print("pid is", pid.pid)
    return pid.pid
    
def kill_proc(val_kill):
    command = "taskkill /f /pid "+ str(val_kill)
    print("command to kill",command)
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    return

#main function
process_name = input("enter a process : ")
pid = open_proc(process_name)
kill_proc(pid)









