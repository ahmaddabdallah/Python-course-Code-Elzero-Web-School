# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

# a = 0
# while a < 10:
#     print(a)
#     a += 1
#     print("Loop is Done")  # True Become False

# while False:
#     print("Will Not Print")

#---------------------------------------

# ----------------------------
# -- Loop => While Training --
# ----------------------------
#----while condition_is_true
#----Code Will Run Until Condition Become False
# -----------------------

# myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]
# # print(len(myF))  # List Length [10]

# a = 0

# while a < len(myF):  # a < 10

#     print(f"#{str(a + 1).zfill(2)} {myF[a]}")

#     a += 1  # a = a + 1

# else:

#     print("All Friends Printed To Screen.")

#------------------------------------------------------

# # ----------------------------
# # -- Loop => While Training --
# # -- Simple Bookmark Manage --
# # ----------------------------

# # Empty List To Fill Later
# myFavouriteWebs = []

# # Maximum Allowed Websites
# maximumWebs = 5

# while maximumWebs > 0:

# # Input The New Website
#     web = input("Website Name Without https:// ")

# # Add The New Website To The List
#     myFavouriteWebs.append(f"https://{web.strip().lower()}")

# # Decrease One Number From Allowed Websites
#     maximumWebs -= 1  # maximumWebs = maximumWebs - 1

# # Print The Add Message
#     print(f"Website Added, {maximumWebs} Places Left")

# # Print The List
#     print(myFavouriteWebs)

# else:

#     print("Bookmark Is Full, You Cant Add More")

# # Check If List Is Not Empty
# if len(myFavouriteWebs) > 0:

# # Sort The List
#     myFavouriteWebs.sort()

#     index = 0

#     print("Printing The List Of Websites in Your Bookmark")

# while index < len(myFavouriteWebs):

#     print(myFavouriteWebs[index])

#     index += 1  # index = index + 1

#----------------------------------------

# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

# mainpassword = "ahmadabdallah"
# inputPassword = input("Write Your Password: ")

# tries = 5
# while inputPassword != mainpassword:  # True

#     tries -= 1  # tries = tries - 1

#     print(f"Wrong Password ,{" Last" if tries == 0 else tries} Chance left.")
    
#     inputPassword = input("Write Your Password: ")

#     if tries == 0 :
#             print("All Tries Is Finished.")
#             break

# else :
#     print("Correct Password")

# Taking user input for the student's score
score = int(input("Enter the Student's score: "))

# Using if, elif, and else to classify the grade
if score >= 90:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

# Displaying the result
print(f"The student's grade is: {grade}")