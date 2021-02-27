names = ["ashok",1,"sravya"]
print(names[1])
print(names[2])
print(names[0:2])
print(names[-2])
names.append(5)
print(names[3])

# to print each and every element in list
for name in names:
    print(name)

# To print each element and index in a list
for i,name in enumerate(names):
    print(i,name)

# str1 = "hello ashok"
# print(str1[0

# how to get last element in a list 
print(names[-1])

# to delete a element in a list 
# we pass argument as index
names.pop(1)
print(names)

