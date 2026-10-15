import matplotlib.pyplot as plt

# Each sales value corresponds to the product at the same position.
products = ["Laptop", "Mouse", "Monitor"]
sales = [25, 80, 15]

# Draw one pie slice per product and use product names as the slice labels.
plt.pie(sales, labels=products)
# Add a title, then display the finished chart.
plt.title("Product Sales")
plt.show()