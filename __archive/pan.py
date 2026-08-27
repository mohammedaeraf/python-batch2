import pandas 

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"],
    "Marks": [85, 92, 78, 88, 69]
}

df = pandas.DataFrame(data)

# print(df)
# print(df["Name"])
# print(df["Marks"])
df.head()
# df.info()
df.describe()
df.shape

df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].sum()

df[df["Marks"] >= 80]

df.sort_values("Marks")