# 📊 Python Data Analytics – Lesson Notes

## Data Visualization with Matplotlib & Seaborn

**Duration:** 30 minutes
**Prerequisite:** Python Basics, Lists, Dictionaries, Functions, NumPy & Pandas

### Learning Objective

By the end of this lesson, students should be able to:

* Understand why data visualization is useful.
* Create basic charts using **Matplotlib**.
* Create simple charts using **Seaborn**.
* Add titles and labels.
* Understand when to use a bar chart vs. line chart.
* Create a simple chart from a Pandas DataFrame.

---

# 1. What is Data Visualization?

**Data Visualization** means representing data using charts and graphs.

Instead of looking at:

```text
January   120
February  150
March     180
April     160
May       220
```

we can visualize the same information as a chart.

### Why?

Charts make it easier to identify:

* Trends
* Comparisons
* Patterns
* Highest and lowest values
* Changes over time

> **Data → Chart → Insight**

---

# 2. Libraries Used

We will use:

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

### Matplotlib

Used for creating many types of charts and giving detailed control over them.

### Seaborn

Built on Matplotlib and provides a convenient interface for attractive statistical visualizations.

---

# 3. Installing the Libraries

Open the **VS Code Terminal** and run:

```bash
pip install matplotlib seaborn
```

You can verify the installation:

```python
import matplotlib
import seaborn

print("Matplotlib =", matplotlib.__version__)
print("Seaborn =", seaborn.__version__)
```

---

# 4. Matplotlib – First Chart

Let's start with a simple example.

```python
import matplotlib.pyplot as plt

students = ["Ahmed", "Sara", "Rahul", "Fatima"]
marks = [85, 92, 78, 88]

plt.bar(students, marks)

plt.show()
```

This creates a **bar chart**.

---

# 5. Understanding the Code

```python
plt.bar(students, marks)
```

means:

```text
students → X-axis
marks    → Y-axis
```

And:

```python
plt.show()
```

displays the chart.

---

# 6. Adding a Title

```python
plt.bar(students, marks)

plt.title("Student Marks")

plt.show()
```

The chart now has the title:

```text
Student Marks
```

---

# 7. Adding Axis Labels

```python
plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()
```

Now the chart clearly explains what each axis represents.

---

# 8. Complete Bar Chart

```python
import matplotlib.pyplot as plt

students = ["Ahmed", "Sara", "Rahul", "Fatima"]
marks = [85, 92, 78, 88]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()
```

### When should we use a Bar Chart?

Use a **bar chart to compare different categories**.

Examples:

```text
Students vs Marks
Products vs Sales
Cities vs Population
Departments vs Employees
```

---

# 9. Line Chart

A **line chart** is particularly useful for showing changes or trends over time.

Example:

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 160, 220]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

---

# 10. Adding Markers

We can make individual data points easier to see:

```python
plt.plot(months, sales, marker="o")
```

Complete example:

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 160, 220]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

---

# 11. Bar Chart vs Line Chart ⭐

This is an important concept.

| Chart            | Best Used For                                        |
| ---------------- | ---------------------------------------------------- |
| **Bar Chart**    | Comparing categories                                 |
| **Line Chart**   | Showing trends over time                             |
| **Pie Chart**    | Showing parts of a whole                             |
| **Scatter Plot** | Showing relationship between two numerical variables |

### Remember

> **Bar → Compare**

> **Line → Trend**

---

# 12. Pie Chart

A pie chart shows how a total is divided among categories.

Example:

```python
import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
sales = [25, 80, 60, 35]

plt.pie(sales, labels=products)

plt.title("Product Sales")

plt.show()
```

This helps us see the relative contribution of each product.

---

# 13. Seaborn

Now let's introduce **Seaborn**.

```python
import seaborn as sns
```

Seaborn works particularly well with Pandas DataFrames.

---

# 14. Creating a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"],
    "Marks": [85, 92, 78, 88, 69]
}

df = pd.DataFrame(data)

print(df)
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

# 15. Seaborn Bar Chart

We can visualize this DataFrame using:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x="Name", y="Marks", data=df)

plt.title("Student Marks")

plt.show()
```

Here:

```text
x = Name
y = Marks
data = df
```

Seaborn automatically works with the DataFrame's columns.

---

# 16. A More Realistic Dataset

Let's use a small sales dataset.

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

---

# 17. Analyze Before Visualizing

First calculate some basic information:

```python
print("Average Sales =", df["Sales"].mean())
print("Highest Sales =", df["Sales"].max())
print("Lowest Sales =", df["Sales"].min())
```

Then visualize:

```python
import matplotlib.pyplot as plt

plt.bar(df["Product"], df["Sales"])

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()
```

This demonstrates an important Data Analytics principle:

> **Don't create charts blindly. First understand the data.**

---

# 18. Finding Insights from a Chart

Suppose the chart shows:

```text
Laptop     25
Mouse      80
Keyboard   60
Monitor    35
Printer    20
```

We can conclude:

* Mouse has the highest sales.
* Printer has the lowest sales.
* Keyboard is the second-highest selling product.

This is an **insight**.

### Data Analytics is not just creating charts.

The goal is:

> **Use data to answer questions and make decisions.**

---

# 19. Filtering + Visualization

Pandas and Matplotlib can work together.

Suppose we want products with sales greater than 30:

```python
filtered_df = df[df["Sales"] > 30]

print(filtered_df)
```

Then visualize only those products:

```python
plt.bar(
    filtered_df["Product"],
    filtered_df["Sales"]
)

plt.title("Products with Sales Above 30")

plt.show()
```

This demonstrates:

```text
Pandas
  ↓
Filter Data
  ↓
Matplotlib
  ↓
Visualize
```

---

# 20. Scatter Plot – Introduction

A **scatter plot** can help us investigate whether two numerical variables are related.

For example:

```text
Price vs Sales
```

Using our DataFrame:

```python
plt.scatter(df["Price"], df["Sales"])

plt.title("Price vs Sales")
plt.xlabel("Price")
plt.ylabel("Sales")

plt.show()
```

Students don't need to study statistical correlation yet.

Simply explain:

> A scatter plot helps us visually examine the relationship between two numerical variables.

---

# 21. Seaborn Scatter Plot

The same data can be visualized with Seaborn:

```python
sns.scatterplot(
    x="Price",
    y="Sales",
    data=df
)

plt.title("Price vs Sales")

plt.show()
```

---

# 22. Complete Mini Data Analytics Demo ⭐

This would be an excellent **final classroom demonstration**.

```python
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
```

This single program demonstrates:

```text
Pandas
  ↓
DataFrame
  ↓
Data Analysis
  ↓
Seaborn
  ↓
Visualization
```

---

# 23. Common Plot Functions

### Bar Chart

```python
plt.bar(x, y)
```

### Line Chart

```python
plt.plot(x, y)
```

### Pie Chart

```python
plt.pie(values, labels=labels)
```

### Scatter Plot

```python
plt.scatter(x, y)
```

---

# 24. Common Chart Customization

### Title

```python
plt.title("My Chart")
```

### X-axis label

```python
plt.xlabel("X Axis")
```

### Y-axis label

```python
plt.ylabel("Y Axis")
```

### Display

```python
plt.show()
```

---

# 25. Important Seaborn Functions

For beginners, introduce just these:

```python
sns.barplot()
```

```python
sns.lineplot()
```

```python
sns.scatterplot()
```

Later, students can learn:

```python
sns.histplot()
sns.boxplot()
sns.heatmap()
```

---

# 26. Recommended Classroom Demonstration

For your **30-minute session**, I suggest this flow:

### 0–5 min

Explain:

**What is Data Visualization?**

Show the same data as:

```text
Numbers → Chart
```

### 5–12 min

Teach **Matplotlib Bar Chart**.

Students create:

```python
plt.bar()
```

with title and labels.

### 12–17 min

Teach **Line Chart**.

Explain:

> Bar = comparison
> Line = trend

### 17–22 min

Introduce **Pandas + Seaborn**.

Create a DataFrame and use:

```python
sns.barplot()
```

### 22–27 min

Show **Filtering + Visualization**.

```python
df[df["Sales"] > 30]
```

followed by a chart.

### 27–30 min

Give students a mini challenge.

---

# 🧪 Mini Lab Exercise

Use:

```python
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 180, 140, 200, 220]
}

df = pd.DataFrame(data)
```

Ask students to:

### 1. Display the DataFrame.

### 2. Find average sales.

```python
df["Sales"].mean()
```

### 3. Find the highest sales.

```python
df["Sales"].max()
```

### 4. Create a line chart showing monthly sales.

### 5. Add:

* Chart title
* X-axis label
* Y-axis label

### ⭐ Challenge

Find months where sales are greater than `160`:

```python
df[df["Sales"] > 160]
```

Then create a chart using only those months.

---

# 📌 Quick Reference

## Import

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Matplotlib

```python
plt.bar(x, y)

plt.plot(x, y)

plt.scatter(x, y)

plt.pie(values, labels=labels)

plt.title("Title")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

## Seaborn

```python
sns.barplot(x="Column1", y="Column2", data=df)

sns.lineplot(x="Column1", y="Column2", data=df)

sns.scatterplot(x="Column1", y="Column2", data=df)
```

---

# 🎯 Final Concept

Students should understand the relationship between the libraries:

```text
             RAW DATA
                 ↓
              Pandas
                 ↓
             DataFrame
                 ↓
        ┌────────┴────────┐
        ↓                 ↓
     ANALYSIS         VISUALIZATION
        ↓                 ↓
     Pandas        Matplotlib / Seaborn
        │                 │
        └────────┬────────┘
                 ↓
              INSIGHTS
```

### The most important takeaway:

> **Pandas helps us work with and analyze data.**

> **Matplotlib and Seaborn help us visualize that data.**

> **The ultimate goal is to discover insights from the data.**
