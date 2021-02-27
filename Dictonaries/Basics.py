# How to Create an empty dictionary 
# we represent dictionary in {}
Dict = {}
print ("Empty Dictionary : ", Dict)

# creating a dictionary with integer keys,
# The print statement here prints the keys and their values
Dict_1 = {1: 'ashok1', 2: 'ash2', 3: 'madrid'}
print(Dict_1)

# creating a dictionary with dict method
Dict_2 = dict({1: 'goal de', 2: 'nada', 3:'hala'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict_2) 

# Creating a Dictionary with each item as pair
Dict_3 = dict([(1,'first'), (2,'second')])
print(Dict_3)

# Adding elements to Dictionary
Dict_4 = {}
Dict_4[0] = 'something'
Dict_4[2] = 'For'
Dict_4[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict_4) 

# Adding set of values  
# to a single Key
Dict_4['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict_4) 

# Accessing elements from a dictionary

# Creating a Dictionary  
Dict = {1: 'ashok1', 'name': 'For', 3: 'madrid'} 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict['name']) 
  
# accessing a element using key 
print("Acessing a element using key:") 
print(Dict[1]) 
  
# accessing a element using get() 
# method 
print("Acessing a element using get:") 
print(Dict.get(3)) 
