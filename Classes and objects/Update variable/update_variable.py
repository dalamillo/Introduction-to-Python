class Car:
    color = ""

    def description(self):  # we'll explain the self parameter later
        description_string = f"This is a {self.color} car."
        return description_string


car1 = Car()
car2 = Car()

car1.color = "blue"
car2.color = "red"

print(Car.description(car1))
print(Car.description(car2))
