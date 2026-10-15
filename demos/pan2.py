# Import the pandas library for working with tabular data.
import pandas

# Create a dictionary representing a small dataset with names and marks.
data = {
    "Name": ["John", "Arif", "Jasmin","Rohan"],
    "Marks": [67, 79, 45, 35]
}

# Convert the dictionary into a pandas DataFrame so we can analyze it easily.
data_frame = pandas.DataFrame(data)

# Select and display students whose marks are below 70.
print(data_frame[data_frame["Marks"] < 70])

# Add a True/False column using 40 as the passing-mark threshold.
data_frame["Passed"] = data_frame["Marks"] >= 40

# Display the full table, including the newly calculated pass status.
print(data_frame)
