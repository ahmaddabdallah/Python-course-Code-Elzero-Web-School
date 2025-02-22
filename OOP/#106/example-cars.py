class Car:
    def __init__(self, name, color, price, speed):
        self.name = name
        self.color = color
        self.price = price
        self.speed = speed

    def start_engine(self):
        return f"{self.name}: the Engine is start."

    def stop_engine(self):
        return f"{self.name}: the Engin is Stop"



car1 = Car("BMW M5", "Blue", 200000, 250)
car2 = Car("Mercedes AMG", "Red", 220000, 280)

print(car1.start_engine())
print(car2.stop_engine())

print(car1.color)
car1.color = "Red"

print(car1.color)

class empty:
    pass