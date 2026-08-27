import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Sales": [25, 80, 60, 35, 20],
    "Price": [55000, 800, 1500, 12000, 7000]
}

df = pd.DataFrame(data)

print("DATA")
print(df)

print("\nAverage Sales =", df["Sales"].mean())
print("Highest Sales =", df["Sales"].max())
print("Lowest Sales =", df["Sales"].min())

sns.barplot(
    x="Product",
    y="Sales",
    data=df
)

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()