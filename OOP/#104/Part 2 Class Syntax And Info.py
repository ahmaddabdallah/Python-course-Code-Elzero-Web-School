# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint Or Constructor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dander or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# -------------------------------------------------------------------

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function

class member:
    def __init__(self , name , age):
        self.name = name
        self.age = age

member_one = member("Ahmad" , 18)

print(member_one.name , member_one.age)

print(member_one.__class__)

# Benefit of OOP in py
# myDict = {
#     "name" : "Ahmad" ,
#     age : 16,
#     "month_salary" : 5000,
#     "yearly_salary" : ""
# }