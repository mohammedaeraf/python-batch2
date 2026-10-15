import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Monitor"]
sales = [25, 80, 15]

plt.pie(sales, labels=products)
plt.title("Product Sales")
plt.show()