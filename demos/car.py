class Car:

    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year

    def display(self):

        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Year =", self.year)


car1 = Car("Toyota", "Corolla", 2025)

car1.display()