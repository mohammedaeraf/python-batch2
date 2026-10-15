import matplotlib.pyplot as plt

# Month labels and their corresponding sales values.
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 160, 220]

# Plot sales for each month, marking each data point with a circle.
plt.plot(months, sales, marker="o")

# Add a title and label each axis to make the chart clear.
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Display the finished chart.
plt.show()