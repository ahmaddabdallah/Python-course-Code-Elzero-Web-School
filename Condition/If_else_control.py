# # --------------------
# # --  Control Flow  --
# # -- If, Elif, Else --
# # -- Make Decisions --
# # --------------------

# uName = "Ahmad"
# uCountry = "Egypt"
# isSudent = "No"
# cName = "Python Course"
# cPrice = 100

# if uCountry == "Egypt" or uCountry== "KSA" or "Quater":

#     if isSudent =="Yes":
#         print(f"Hello {uName} Because You Are From {uCountry} and You are Student")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")
#     else:
#         print(f"Hello {uName} Because You Are From {uCountry}")
#         print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

# elif uCountry== "Kwaite" or uCountry == "Iruq" :
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

# else :
#     print(f"Hello {uName} Because You Are From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 20}")
# print("#" * 50)

# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

# country = "Quator"

# if country == "Egypt":
#     print(f"The Wheather in {country} Is 20.") 

# elif country == "KSA":
#     print(f"The wheather in {country} Is 38")

# else:
#     print("The country is not the list")
    
# movieRate = 18
# age = 18
# if age <movieRate:
#     print("the movie is not good for you")
# else:
#     print("Movie S Good 4U And Happy Watching") # Condition If False

# print("the movie is not good for you" if age < movieRate else "Movie S Good 4U And Happy Watching")
# # Condition If True | If Condition | Else | Condition If False
# print("#" *50)

# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)

#Collect age data
age = input("Please Write Your age : ").strip()
#Collect Time Unit
unit = input("Please Choose Time Unit: Months, Weeks, Days : ").strip().lower()

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == "m":
    print("You are Choose the Months.")
    print(f"You Lived for {months:,} Months.")

elif unit == "weeks" or unit == "w":
    print("You are Choose the Weeks.")
    print(f"You Lived for {weeks:,} Weeks.")

elif unit == "days" or unit == "d":
    print("You are Choose the Days.")
    print(f"You Lived for {days:,} Days.")
