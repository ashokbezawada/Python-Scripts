# How do you create a new dictionary we use ex: ash = {}
ashok = {'name' : 'ash','age' : 18}
print(ashok)

# How to print ash from dictionary 
print(ashok['name'])

# How to add something in dictionary
ashok['height'] = 183
print(ashok)

# we can store multiple items in a dictionary
ashok['course'] = ['operating systems','computer networks']
print(ashok)

# To update multiple things and add a mew key
ashok.update({'name':'sra','age':20,'phone':4442332})
print(ashok)

# to delete something in dictionary
del ashok['age']
print(ashok)

# to get all keys in dictionary
print(ashok.keys())