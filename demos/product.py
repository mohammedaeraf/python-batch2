class Product:
    
    # constructor method
    def __init__(self, t, p, q):
        self.title = t
        self.price = p
        self.quantity = q

    def display(self):
        print()
        print("Displaying Product Details\n---------------------")
        print("Title:", self.title)
        print("Price: Rs", self.price)
        print("Quantity: ", self.quantity)

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self, discount_value):
        discount = self.price * discount_value / 100
        self.price = self.price - discount

        
# creating an object
title = input("Enter product name: ")
product1 = Product(title,5000, 5)
product1.display()
print("Total Value: ", product1.calculate_total())
product1.apply_discount(10)
product1.display()


product2 = Product("HP Pavillion Laptop",55400, 4)
product2.display()
print("Total Value: ", product2.calculate_total())
