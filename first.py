# # ----------------------------------------------------
# # ---- User Input
# # ----------------------------------------------------

# FirstName = input("What\'s Your First Name?")
# MiddleName = input("What\'s Your Middle Name?")
# LastName = input("What\'s Your Last Name?")

# FirstName = FirstName.strip().capitalize()
# MiddleName = MiddleName.strip().capitalize()
# LastName = LastName.strip().capitalize()
# print(f"Hello {FirstName} {MiddleName:.2s} {LastName} Happy to See You.")     

#print("#" * 50)

#---------------------------
#--- Practical Email Slice
#---------------------------

# TheName = input("What\'s your Name ?").strip().capitalize()
# TheEmail = input("What\'s your Email ?").capitalize()
# TheUserName = TheEmail[:TheEmail.index("@")]
# Website =  TheEmail[TheEmail.index("@") + 1:]

# print(f"Hello {TheName} Your Email Is {TheEmail}")
# print(f"Your UserName Is {TheUserName} \nYour Domain IS {Website}")

# email = "ahmadaballahhossen@gmail.com"

# print(email[:email.index("@")])

#-----------------------------
#-----Input Age
#-----------------------------
#Input Age
age =int(input("What \'s Your Age ?"))

months = age * 12
weeks = months * 4
days = age * 365
hours  = days * 24
minutes  = hours * 60
seconds = minutes * 60

print("You Lived for:")
print(f"{months} Months. ")
print(f"{weeks:,} Weeks. ")
print(f"{days:,} Days. ")
print(f"{hours:,} Hours. ")
print(f"{minutes:,} Minuts. ")
print(f"{seconds:,} Seconds. ")
