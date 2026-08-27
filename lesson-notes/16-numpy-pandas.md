# 🐍 Python Data Analytics – Lesson Notes

## NumPy & Pandas

These notes are designed as an **introductory lesson after completing the Python Programming course**. The objective is not to teach every feature, but to help students understand **why these libraries are used and how Python can be applied to real-world data**.

---

# 1. What is Data Analytics?

**Data Analytics** is the process of examining data to find useful information, patterns, and insights.

For example, imagine we have sales data:

| Product  | Sales | Price |
| -------- | ----: | ----: |
| Laptop   |    25 | 55000 |
| Mouse    |    80 |   800 |
| Keyboard |    60 |  1500 |
| Monitor  |    35 | 12000 |

We may want to answer:

* Which product sold the most?
* What is the average sales?
* Which product is the most expensive?
* Which products have sales greater than 30?

Python libraries make these tasks much easier.

---

# 2. Important Python Libraries for Data Analytics

We will mainly encounter:

```text
Python Data Analytics
        │
        ├── NumPy
        │     ↓
        │   Numerical Data
        │
        ├── Pandas
        │     ↓
        │   Tables / Data Analysis
        │
        ├── Matplotlib
        │     ↓
        │   Charts
        │
        └── Seaborn
              ↓
          Visualization
```

In this lesson, we focus on:

> **NumPy + Pandas**

---

# 3. Installing NumPy and Pandas

Since these are external libraries, they need to be installed before we can use them.

## Step 1 – Open VS Code Terminal

In VS Code:

**Terminal → New Terminal**

You can also use:

```text
Ctrl + `
```

---

## Step 2 – Install NumPy

Run:

```bash
pip install numpy
```

NumPy's official installation documentation lists `pip install numpy` as an installation method. ([NumPy][1])

---

## Step 3 – Install Pandas

Run:

```bash
pip install pandas
```

Pandas officially supports installation through pip from PyPI. ([Pandas][2])

### Or install both together

You can simply run:

```bash
pip install numpy pandas
```

---

# 4. Verify Installation

Create a file:

```text
test_libraries.py
```

Write:

```python
import numpy
import pandas

print("NumPy version =", numpy.__version__)
print("Pandas version =", pandas.__version__)
```

Run the program.

If the installation is successful, you should see version numbers.

---

## Recommended Import Style

You will usually see:

```python
import numpy as np
import pandas as pd
```

Here:

```text
np → short name for NumPy
pd → short name for Pandas
```

These are conventional aliases and are very commonly used in Python data-analysis code.

---

# PART 1 – NumPy

# 5. What is NumPy?

**NumPy** stands for **Numerical Python**.

It is designed primarily for working with numerical data and arrays.

Instead of working only with ordinary Python Lists:

```python
marks = [75, 80, 65, 90, 85]
```

we can create a NumPy array:

```python
import numpy as np

marks = np.array([75, 80, 65, 90, 85])

print(marks)
```

Output:

```text
[75 80 65 90 85]
```

---

# 6. Why NumPy?

Python Lists are useful, but NumPy provides specialized tools for numerical calculations.

For example:

```python
import numpy as np

marks = np.array([75, 80, 65, 90, 85])

print("Average =", np.mean(marks))
print("Highest =", np.max(marks))
print("Lowest =", np.min(marks))
```

Output:

```text
Average = 79.0
Highest = 90
Lowest = 65
```

---

# 7. NumPy Array

An **array** is a collection of values that NumPy can process efficiently.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

We can access an element just like a List:

```python
print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

---

# 8. NumPy Mathematical Operations

One useful feature is that we can perform calculations on an entire array.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers * 2)
```

Output:

```text
[ 20  40  60  80 100]
```

Similarly:

```python
print(numbers + 5)
```

Output:

```text
[15 25 35 45 55]
```

This is one reason NumPy is useful for numerical data.

---

# 9. Important NumPy Functions

For this introductory course, you only need a few functions initially.

| Function     | Purpose                      |
| ------------ | ---------------------------- |
| `np.array()` | Create an array              |
| `np.mean()`  | Calculate average            |
| `np.sum()`   | Calculate total              |
| `np.max()`   | Find maximum                 |
| `np.min()`   | Find minimum                 |
| `np.std()`   | Calculate standard deviation |

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Total =", np.sum(numbers))
print("Average =", np.mean(numbers))
print("Maximum =", np.max(numbers))
print("Minimum =", np.min(numbers))
```

Output:

```text
Total = 150
Average = 30.0
Maximum = 50
Minimum = 10
```

---

# 10. NumPy – Practical Example

### Student Marks

```python
import numpy as np

marks = np.array([75, 82, 91, 68, 84])

print("Marks =", marks)
print("Total =", np.sum(marks))
print("Average =", np.mean(marks))
print("Highest =", np.max(marks))
print("Lowest =", np.min(marks))
```

This is a good first demonstration because you already know how to calculate total, average, highest and lowest using Python.

Now you can see how a library simplifies the work.

---

# 11. NumPy vs Python List

### Python List

```python
marks = [75, 82, 91, 68, 84]
```

### NumPy Array

```python
marks = np.array([75, 82, 91, 68, 84])
```

The List is still useful.

NumPy becomes particularly valuable when working with **large amounts of numerical data and mathematical operations**.

---

# PART 2 – Pandas

# 12. What is Pandas?

**Pandas** is a Python library designed for working with **tabular and structured data**.

A typical table might look like:

| Name   | Age | Marks |
| ------ | --: | ----: |
| Ahmed  |  20 |    85 |
| Sara   |  21 |    92 |
| Rahul  |  19 |    78 |
| Fatima |  20 |    88 |

Pandas allows us to represent this table as a **DataFrame**.

Pandas describes a DataFrame as its main data structure for working with tabular data. ([Pandas][3])

---

# 13. Import Pandas

```python
import pandas as pd
```

---

# 14. Creating a DataFrame

We can create a DataFrame from a Dictionary.

```python
import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
     Name  Marks
0   Ahmed     85
1    Sara     92
2   Rahul     78
3  Fatima     88
```

---

# 15. Understanding the DataFrame

A DataFrame looks similar to an Excel spreadsheet.

```text
        Name       Marks
Index
  0     Ahmed        85
  1     Sara         92
  2     Rahul        78
  3     Fatima       88
```

Important terms:

### DataFrame

The complete table.

### Column

For example:

```python
df["Marks"]
```

### Row

A single record.

### Index

The row numbers:

```text
0
1
2
3
```

---

# 16. Selecting a Column

Suppose:

```python
df = pd.DataFrame(data)
```

We can select the `Marks` column:

```python
print(df["Marks"])
```

Output:

```text
0    85
1    92
2    78
3    88
```

We can also calculate:

```python
print(df["Marks"].mean())
```

Output:

```text
85.75
```

---

# 17. Basic DataFrame Information

Pandas provides useful methods for quickly understanding a dataset.

### `head()`

```python
print(df.head())
```

Displays the first few rows.

---

### `info()`

```python
print(df.info())
```

Provides information about:

* Columns
* Data types
* Number of entries

---

### `describe()`

```python
print(df.describe())
```

Provides statistical information about numerical columns.

---

### `shape`

```python
print(df.shape)
```

For example:

```text
(4, 2)
```

means:

```text
4 rows
2 columns
```

---

# 18. Basic Data Analysis

Consider:

```python
import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"],
    "Marks": [85, 92, 78, 88, 69]
}

df = pd.DataFrame(data)
```

### Average

```python
print(df["Marks"].mean())
```

### Highest

```python
print(df["Marks"].max())
```

### Lowest

```python
print(df["Marks"].min())
```

### Total

```python
print(df["Marks"].sum())
```

---

# 19. Filtering Data ⭐

One of the most useful features of Pandas is filtering.

Suppose we want students who scored **80 or more**:

```python
high_marks = df[df["Marks"] >= 80]

print(high_marks)
```

Output:

```text
     Name  Marks
0   Ahmed     85
1    Sara     92
3  Fatima     88
```

This is similar to applying a filter in Excel.

---

# 20. Another Filtering Example

Find students who scored below 80:

```python
print(df[df["Marks"] < 80])
```

Output:

```text
     Name  Marks
2   Rahul     78
4  Zeeshan     69
```

---

# 21. Adding a New Column

We can create a new column.

```python
df["Passed"] = df["Marks"] >= 40

print(df)
```

Output:

```text
      Name  Marks  Passed
0    Ahmed     85    True
1     Sara     92    True
2    Rahul     78    True
3   Fatima     88    True
4  Zeeshan     69    True
```

This demonstrates how Pandas can transform data.

---

# 22. Practical Example – Student Analysis

Let's put the concepts together.

```python
import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"],
    "Marks": [85, 92, 78, 88, 69]
}

df = pd.DataFrame(data)

print("Student Data")
print(df)

print("\nAverage Marks =", df["Marks"].mean())
print("Highest Marks =", df["Marks"].max())
print("Lowest Marks =", df["Marks"].min())

print("\nStudents scoring 80 or above:")
print(df[df["Marks"] >= 80])
```

This is already a small **Data Analytics program**.

---

# 23. Pandas with More Columns

Let's make the data more realistic.

```python
import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"],
    "Age": [20, 21, 19, 20, 22],
    "Course": ["Python", "Python", "Python", "Python", "Python"],
    "Marks": [85, 92, 78, 88, 69]
}

df = pd.DataFrame(data)

print(df)
```

Now we have:

| Name    | Age | Course | Marks |
| ------- | --: | ------ | ----: |
| Ahmed   |  20 | Python |    85 |
| Sara    |  21 | Python |    92 |
| Rahul   |  19 | Python |    78 |
| Fatima  |  20 | Python |    88 |
| Zeeshan |  22 | Python |    69 |

---

# 24. Selecting Multiple Columns

We can select more than one column:

```python
print(df[["Name", "Marks"]])
```

Output:

```text
      Name  Marks
0    Ahmed     85
1     Sara     92
2    Rahul     78
3   Fatima     88
4  Zeeshan     69
```

---

# 25. Sorting Data

Suppose we want to sort students by marks.

```python
sorted_df = df.sort_values("Marks")

print(sorted_df)
```

For highest marks first:

```python
sorted_df = df.sort_values("Marks", ascending=False)

print(sorted_df)
```

This is a very useful real-world data-analysis operation.

---

# 26. Reading Data from a CSV File ⭐

One of the biggest advantages of Pandas is that it can work with files containing tabular data.

Suppose we have:

```text
students.csv
```

containing:

```text
Name,Age,Marks
Ahmed,20,85
Sara,21,92
Rahul,19,78
Fatima,20,88
```

We can load it using:

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

Now the CSV data becomes a Pandas DataFrame.

This is where Data Analytics becomes much more realistic.

---

# 27. The Data Analytics Workflow

Students should understand this workflow:

```text
CSV / Excel / Database
        ↓
      Pandas
        ↓
     DataFrame
        ↓
   Explore Data
        ↓
 Filter / Clean
        ↓
    Analyze
        ↓
 Visualize
        ↓
    Insights
```

For example:

```python
df = pd.read_csv("sales.csv")
```

Then:

```python
df.head()
```

Then:

```python
df.describe()
```

Then:

```python
df[df["Sales"] > 50]
```

Then eventually:

```text
Create Charts
```

---

# 28. NumPy + Pandas Together

These libraries are often used together.

```python
import numpy as np
import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima"],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

average = np.mean(df["Marks"])

print("Average =", average)
```

However, Pandas itself already provides:

```python
df["Marks"].mean()
```

So students should not think they must use NumPy for every Pandas calculation.

---

# 29. NumPy vs Pandas

This is the most important comparison.

| NumPy                                 | Pandas                                 |
| ------------------------------------- | -------------------------------------- |
| Numerical computing                   | Data analysis                          |
| Arrays                                | DataFrames / Series                    |
| Excellent for mathematical operations | Excellent for tabular data             |
| Fast numerical calculations           | Filtering, sorting, grouping, cleaning |
| `np.mean()`                           | `df["Marks"].mean()`                   |

### Simple way to remember

> **NumPy → Numbers**

> **Pandas → Tables**

---

# 30. What Should Students Learn First?

For a beginner Data Analytics course, I recommend this progression:

```text
Python
  ↓
NumPy Basics
  ↓
Pandas Basics
  ↓
Data Cleaning
  ↓
Data Analysis
  ↓
Matplotlib
  ↓
Seaborn
```

---

# 🧪 Classroom Mini Exercise

Use Dataset below:

```python
import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Sales": [25, 80, 60, 35, 20],
    "Price": [55000, 800, 1500, 12000, 7000]
}

df = pd.DataFrame(data)

print(df)
```

Perform these tasks.

### 1. Display the first few records

```python
df.head()
```

### 2. Find average sales

```python
df["Sales"].mean()
```

### 3. Find the highest sales

```python
df["Sales"].max()
```

### 4. Display products with sales above 30

```python
df[df["Sales"] > 30]
```

### 5. Sort products by sales

```python
df.sort_values("Sales", ascending=False)
```

This is how you perform your **actual data analysis**.

---

# 📌 Quick Reference

## NumPy

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

np.sum(numbers)
np.mean(numbers)
np.max(numbers)
np.min(numbers)
```

## Pandas

```python
import pandas as pd

df = pd.DataFrame(data)

df.head()
df.info()
df.describe()
df.shape

df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].sum()

df[df["Marks"] >= 80]

df.sort_values("Marks")
```

## CSV

```python
df = pd.read_csv("data.csv")
```

---

# 🎯 Final Takeaway

You should leave this lesson understanding **three things**:

### 1. NumPy

> Used mainly for **numerical calculations and arrays**.

### 2. Pandas

> Used mainly for **working with tables and analyzing data**.

### 3. Data Analytics

> Use Python libraries to turn **raw data → useful information → insights**.

