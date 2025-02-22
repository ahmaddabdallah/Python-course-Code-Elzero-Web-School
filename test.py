# Lesson eight
# ----------------------------
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------

# Back Space
print("Helloo\bWorld")  # Will Remove o

# Escape New Line + Back Slash
print("Hello \
I Love \
Python")

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Quote
print('I Love Single Quote \'Test\' ')

# Escape Double Quotes
print("I Love Double Quotes \"Test\" ")

# Line Feed
print("Hello World\nSecond Line")

# Carriage Return
print("123456\rAbcde")

# Horizontal Tab
print("Hello\tPython")

# Character Hex Value
print("\x4F\x73")

print("=" *70)

# Lesson ten

# -------------------
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

full = msg + " " + lang
print(full)

a = "First \nSecond \nThird"

b = "A \
B \
C"

print(a + "\n" + b)

# print("Hello " + 1)  # Error

print("=" *60)

# lesson eleven

# -------------
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''

myStringSix = """First
Second "Test" \\\ 'Test'
Third"""

print(myStringFive)
print(myStringSix)

print("="* 60)

# lesson 12

# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First Character From End
print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

print(myString[::2])
print(myString[::3])

print("=" * 50)

# lesson 13
# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "Ahmad"

print(g.upper())

# lower()

h = "AHmad"

print(h.lower())

print("=" * 50)

# lesson 14

# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

# center()

e ="Ahmad"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))

print("=" * 50)

# lesson 15

# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)

a = "I Love Python"
# print(a.index("P"))  # Index Number 7
# print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "Ahmad"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Ahmad"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "Ahmad_elzero"
eight = "AhmadElzero100"
nine = "Ahamd--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

print("=" *50)

# lesson 16

# ---------------------
# -- Strings Methods --
# ---------------------

# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable)

myList = ["Ahamd", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

print("=" * 50)

# lesson 17

# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Ahmad"
age = 15
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "Ahmad")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %.2f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Ahmad"
l = "Python"
y = 10

print("My Name is %s I am %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)

print("=" * 50)

# lesson 18 

# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

name = "Ahmad"
age = 15
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: {}".format("Ahmad"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Ahmad"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")

print("=" *50)

# lesson 19

# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print("Real Part Is: {}".format(myComplexNumber.real))
print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
print("=" * 50)
# lesson 20

# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# Addition

print(10 + 30)  # 40
print(-10 + 20)  # 10
print(1 + 2.66)  # 3.66
print(1.2 + 1.2)  # 2.4

# Subtraction

print(60 - 30)  # 30
print(-30 - 20)  # -50
print(-30 - -20)  # -10
print(5.66 - 3.44)  # 2.22

# Multiplication

print(10 * 3)  # 30
print(5 + 10 * 100)  # 1005
print((5 + 10) * 100)  # 1500

# Division

print(100 / 20)  # 5.0
print(int(100 / 20))  # 5

# Modulus

print(8 % 2)  # 0
print(9 % 2)  # 1
print(20 % 5)  # 0
print(22 % 5)  # 2

# Exponent

print(2 ** 5)  # 32
print(2 * 2 * 2 * 2 * 2)  # 32
print(5 ** 4)  # 625
print(5 * 5 * 5 * 5)  # 625

# Floor Division

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7
print("=" * 50)
# lesson 21

# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A"]
print(myAwesomeList)

print("=" * 50)

# lesson 22

# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

print("=" * 50)

# lesson 23

# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))

print("=" *50)

# lesson 24
# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
f.insert(-1, "Test")

print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))

print("=" * 50)

# lesson 24

# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

myAwesomeTupleOne = ("Osama", "Ahmed")
myAwesomeTupleTwo = "Osama", "Ahmed"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# Tuple Assign Values

myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data

myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])

print("=" *50)

# lesson 25

# -----------
# -- Tuple --
# -----------

# Tuple With One Element

myTuple1 = ("Osama",)
myTuple2 = "Osama",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

# Tuple, List, String Repeat (*)

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()

a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct

a = ("A", "B", 4, "C")

x, y, _, z = a

print(x)
print(y)
print(z)

print("=" * 50)

# lesson 26

# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)

print("="*50)

# lesson 27

# -----------------
# -- Set Methods --
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "Css"])
j.update(k)

print(j)

print("="*50)

# lessson 28

# -----------------
# -- Set Methods --
# -----------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # a - b
print(a)

print("=" * 40)  # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # c - d
print(c)

print("=" * 40)  # Separator

# intersection()

e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

print("=" * 40)  # Separator

# intersection_update()

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)

print("=" * 40)  # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)

print("=" * 80)

# lesson 29

# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True
print("="*80)

# lesson 30

# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
  "name": "Osama",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)

print("=" *50)

# lesson 31

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {
  "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
  "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())

print("*" *50)

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {
  "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
  "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())

print("=" *50)

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
  "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {
  "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
  "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())

# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# True Values

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))


# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False


# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False

# ---------------------
# -- Type Conversion --
# ----------------------

# str()

a = 10
print(type(a))
print(type(str(a)))

print("#" * 50)

# tuple()

c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

# list()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("#" * 50)

# set()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("#" * 50)

# dict()

d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

print(dict(d))
print(dict(e))

# ----------------
# -- User Input --
# ----------------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")

# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()

theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "Osama@elzero.org"
# print(email[:email.index("@")])

# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age
age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You Lived For:')
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")

