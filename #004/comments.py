# -------------------------------
# Information About File
# License
# Who Created The File
# When The File Created
# Why The File Created
# Write Beside The Programming Line
# Write Before The Programming Line
# Prevent Code From Run
# -------------------------------

# This is Comment
print("I Love Python")  # This is Inline Comment
print("Programming")  # I Used This Method Because of Bla Bla Bla
print("Programming")  # If You Used Test Method Will Through Error

# this is single line comment

"""
this is 
multiple line 
comment
"""

# value = "Enter your PassWord : "

# inputData = input(value)

# print(inputData)

array = [1,2,3]

array[0] = 5

print(array)

tuple_list = (1,2,3,4)

print(tuple_list[-1])

# colors = ("red", "green", "blue")
# print(colors[0])


# colors[0] = "Blue" #Error

# print(colors)

dict_type = {"key" : "value"}

dict_type["key"] = "New Value"
print(dict_type)

# Ternary Operator

# In JS we will write :
# condition ? expiration_1_if True : expiration_1_if false


# in Python we will write :

# condition_if True if condition else condition if false 

# When you know what is the number of iteration
for i in range(5):
    print(i)
    
a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

myString = "Osama "
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
# mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

# print(mySetThree)

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)

user = {
  "name": "Osama",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}


print(user["name"])
print(user.get("skills"))

user.update({"name" : "Ahmad"})

print(user)


Main = {
    "name" : "Ahmad"
} 

print(Main.keys)
print(Main.values)