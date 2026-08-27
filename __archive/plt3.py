import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
sales = [25, 80, 60, 35]

plt.pie(sales, labels=products)

plt.title("Product Sales")

plt.show()