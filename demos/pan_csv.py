import pandas as pd

sales_data = pd.read_csv("sample_sales_data.csv")

df = pd.DataFrame(sales_data)

print(df)
