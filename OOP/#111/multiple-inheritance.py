# ----------------------------------------
# -- Object Oriented Programming ---------
# ----------------------------------------

class baseOne:
    def __init__(self):
        print("Base one")

    def func_one(self):
        print("Function one ")


class baseTwo:
    def __init__(self):
        print("Base two")

    def func_two(self):
        print("Function two.")


class Derived(baseOne, baseTwo):
    pass


my_var = Derived()

print(my_var.func_one())
print(my_var.func_two())

# print(Derived.mro()) # The order of the classes


class base:
    pass


class DerivedOne(base):
    pass


class DerivedTwo(DerivedOne):
    pass
