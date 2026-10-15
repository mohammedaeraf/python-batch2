import pandas as pd

df = pd.read_csv("sample_sales_data.csv")

print(df)

# Display the first 5 records
print(df.head())

# Display the last 5 records
print(df.tail())

# Check the number of rows and columns
print(df.shape)

# View column names and data types
print(df.info())

# Generate statistical summary
print(df.describe())

# Calculate total sales
print(df["Sales_Amount_INR"].sum())

# Calculate average sales
print(df["Sales_Amount_INR"].mean())

# Find the highest sales transaction
print(df["Sales_Amount_INR"].max())

# Display only Electronics sales
print(df[df["Category"] == "Electronics"])

# Sort by sales amount, highest first
print(df.sort_values("Sales_Amount_INR", ascending=False))