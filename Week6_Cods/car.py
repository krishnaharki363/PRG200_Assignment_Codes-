class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)

car1 = Car("Toyota", "Corolla", 2022)
car1.display()