# Example -1
# creating a new class 
class Test:
    # A sample method or function
    def fun(self):
        print("hello")

# Main function
# we are creating an object for class test which is obj
obj = Test()
obj.fun()

# Example - 2
# The method init is useful to do any intialization you want to do with your object
class person:
    def __init__(self,name):
        self.name = name
    def say_something(self):
        print("Hello my mom's name is : ", self.name)

# creating object for the class
p = person('rama')
p.say_something()

# Example - 3 
# class variables are variables whose value assigned inside the class

class MS_student:
    
    # class variable
    stream = "masters in cs"

    def __init__(self,roll):
        self.roll = roll
    
# Objects of MS_student class
a = MS_student(101)
b = MS_student(102)
print(a.stream)
print(b.stream)
print(a.roll)
print(b.roll)

# class variables can be accessed by using class name
print(MS_student.stream)

# Example - 4
# Program to show that we can create instance variables inside methods

class Ms_student_a:
    # class variable
    stream = "Master in CS"

    def __init__(self,roll):
        # instance variable
        self.roll = roll

    def setAddress(self, address):
        self.address = address
    
    def getAddress(self):     
        return self.address
    
# Main function
c = Ms_student_a(101)
c.setAddress("Ongole, AP")
print(c.getAddress())

d = Ms_student_a(103)
d.setAddress("M.nidmanuru, AP")
print(d.getAddress())
