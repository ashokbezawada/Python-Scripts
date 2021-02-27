#Minutes to Seconds
def change_min_tosec(x):
 if(x == 0):
  print("enter a number greater than zero")
 else:
    y = 60*x
    return y
 x = int(input("enter the no.of minutes to convert in seconds:"))
 y = change_min_tosec(x)
 print("seconds is:",y)
