import subprocess
#main function


pid = subprocess.Popen("notepad.exe")
print("pid is", pid.pid)
print("killing")

value = pid.pid




command = "taskkill /pid "+ str(value)

print("command to kill",command)

p = subprocess.Popen("taskkill /pid "+ str(value), stdout=subprocess.PIPE)
