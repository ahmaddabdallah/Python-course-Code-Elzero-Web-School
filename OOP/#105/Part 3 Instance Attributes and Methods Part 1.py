# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------


class member:
    def __init__(self, fName, mName, lName, gander):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.gander = gander

    def getFullName(self):
        return f"{self.fName} {self.mName} {self.lName}"

    def nameWithTitle(self):
        if self.gander == "Male":
            return f"Hello Mr {self.getFullName()}"
        elif self.gander == "Female":
            return f"Hello Ms {self.getFullName()}"
        else:
            return f"Hello {self.getFullName()}"


member_one = member("Ahmad", "Abdallah", "Mohamed", "Male")
member_two = member("Ali", "Ahmad", "Mohamed", "Male")
member_three = member("Asmaa", "Abdallah", "Mohamed", "Female")

# print(dir(member_one))

# Normal way to concat the get the full Name :
print(
    f"Normal way to concat the get the full Name : {member_one.fName} {member_one.mName} {member_one.lName}"
)

# the new way using create a Function that contain the full Name
print(
    f"The New Way using Create a Function that Contain the Full Name : {member_one.getFullName()}")

# Name with Title
print(member_one.nameWithTitle())
print(member_two.nameWithTitle())
print(member_three.nameWithTitle())
