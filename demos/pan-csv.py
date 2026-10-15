import pandas as pd

# Load the sales data from the CSV file into a DataFrame.
sales_data = pd.read_csv("sample_sales_data.csv")

# Create a DataFrame from the loaded data for tabular operations.
df = pd.DataFrame(sales_data)

# Print the full table to the console.
print(df)
