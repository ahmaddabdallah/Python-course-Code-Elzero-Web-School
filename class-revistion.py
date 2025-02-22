def greet():
    return "Hello world From Base function"


class test:
    def functionTitle():
        return "Hello world from function inside class"


print(greet())

greetClass = test

print(greetClass.functionTitle())

print("-" * 50)

# Class Attribute


class test_code:
    name = "Ahmad"
    age = 18


print(test_code.name)
print(test_code.age)
print("-" * 50)

# Instant Attributes


class InstantAttr:
    def __init__(self, name, age):
        self.name = name
        self.age = age


instantAttOne = InstantAttr("Ahmad", 505050)

print(instantAttOne.name , instantAttOne.age)


tuple_type = (10 , 20 , 30 , 10)

print(tuple_type)

# tuple_type[0] = "Blue" # Error

# print(tuple_type)