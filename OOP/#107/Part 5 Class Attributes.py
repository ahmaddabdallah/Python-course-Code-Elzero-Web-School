# -----------------------------------------------------
# -- Object Oriented Programming => Class Attributes --
# -----------------------------------------------------
# Class Attributes: Attributes Defined Outside The Constructor
# -----------------------------------------------------------

class member:
    not_allowed_names = ["Shit", "Hell", "Ballot"]

    user_count = 0

    def __init__(self, fName, mName, lName, gander):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.gander = gander
        member.user_count += 1

    def getFullName(self):
        if self.fName in member.not_allowed_names:
            raise ValueError("Your Name is not allow to name.")
        else:
            return f"{self.fName} {self.mName} {self.lName}"

    def nameWithTitle(self):
        if self.gander == "Male":
            return f"Hello Mr {self.getFullName()}"
        elif self.gander == "Female":
            return f"Hello Ms {self.getFullName()}"
        else:
            return f"Hello {self.getFullName()}"

    def removeElement(self):
        member.user_count -= 1
        return f"{self.fName} is deleted."


member_one = member("Ahmad", "Abdallah", "Mohamed", "Male")
member_two = member("Ali", "Ahmad", "Mohamed", "Male")
member_three = member("Asmaa", "Abdallah", "Mohamed", "Female")
# member_four = member("Shit", "Hell", "Mohamed", "DD") # Not Allowed Names

# print(dir(member_one))

# Normal way to concat the get the full Name :
# print(f"Normal way to concat the get the full Name : {member_one.fName} {member_one.mName} {member_one.lName}")

# the new way using create a Function that contain the full Name
# print(f"The New Way using Create a Function that Contain the Full Name : {member_one.getFullName()}")

# Name with Title
print(member.user_count)

print(member_one.nameWithTitle())
print(member_two.nameWithTitle())
print(member_three.nameWithTitle())
print(member_three.removeElement())

print(member.user_count)
