# ----------------------------------------
# -- Object Oriented Programming ---------
# ----------------------------------------

class food:  # Base class
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"{self.name} is Created From Base Class")

    def eat(self):
        print("Eat method from Base class")


class Apple(food):  # Derived Class
    def __init__(self, name , price):
        self.name = name
        # food.__init__(self, name)  # Create Instant from Base class
        super().__init__(name, price)
        # self.price = price + 200
        print(
            f"{self.name} is Created From Derived Class , and Your price is : {self.price}")


# food_one = food()
food_two = Apple("Pizza" , 500)

# food_two.eat()
