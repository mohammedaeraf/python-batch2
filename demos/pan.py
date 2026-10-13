# Import the pandas library for working with tabular data.
import pandas

# Create a dictionary representing a small dataset with names and marks.
data = {
    "Name": ["John", "Arif", "Jasmin"],
    "Marks": [67, 79, 45]
}

# Convert the dictionary into a pandas DataFrame so we can analyze it easily.
data_frame = pandas.DataFrame(data)

# Display the original data and basic statistics.
print(data_frame)
print("Sum = ", data_frame["Marks"].sum())
print(data_frame.info())

# Sort the rows by marks in ascending order to see the lowest scores first.
df_sorted = data_frame.sort_values("Marks")

# Print the sorted data and a few summary views.
print(df_sorted)
print(df_sorted.head())
print(df_sorted.describe())
print("Shape = ", df_sorted.shape)
