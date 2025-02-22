# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

print("#" * 50)

# ---------------
# -- Nested If --
# ---------------

uName = "Osama"
isStudent = "Yes"
uCountry = "Egypt"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

    if isStudent == "Yes":

        print(f"Hi {uName} Because U R From {uCountry} And Student")
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

    else:

        print(f"Hi {uName} Because U R From {uCountry}")
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


elif uCountry == "Kuwait" or uCountry == "Bahrain":

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

    print(f"Hi {uName} Because U R From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
print("#" * 50)
# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "A"

if country == "Egypt" : print(f"The Weather in {country} Is 15")
elif country == "KSA" : print(f"The Weather in {country} Is 30")
else : print("Country is Not in The List")

# Short If

movieRate = 18
age = 18

if age < movieRate :

    print("Movie S Not Good 4U") # Condition If True

else :

    print("Movie S Good 4U And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False
print("#" * 50)
# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)

# Collect Age Data
age = input("Please Write Your Age").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == 'm':

    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

    print("You Choosed The Unit Days")
    print(f"You Lived For {days:,} Days.")
print("#" * 50)
# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if myCountry in countriesOne:

    print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:

    print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else:

    print("You Have No Discount")
print("#" * 50)
# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your Name ").strip().capitalize()

# If Name is In Admin
if name in admins:

  print(f"Hello {name} Welcome Back")

  option = input("Delete Or Update Your Name ?").strip().capitalize()

  # Update Option
  if option == 'Update' or option == 'U':

    theNewName = input("Your New Name Please ").strip().capitalize()

    admins[admins.index(name)] = theNewName

    print("Name Updated.")

    print(admins)

  # Delete Option
  elif option == 'Delete' or option == 'D':

    admins.remove(name)

    print("Name Deleted")

    print(admins)

  # Wrong Option
  else:

    print("Wrong Option Choosed")

else:

  status = input("Not Admin, Add You Y, N ? ").strip().capitalize()

  if status == "Yes" or status == "Y":

    print("You Have Been Added")

    admins.append(name)

    print(admins)

  else:

    print("You Are Not Added.")
    
print("#" * 50)
