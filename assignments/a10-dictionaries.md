# 🧪 Lab Assignment 07 – Dictionaries in Python

## 📘 Instructions

1. Write each program in a separate Python file.
2. Use **Dictionaries** in all programs.
3. Use loops and conditional statements wherever required.
4. Use meaningful keys such as `"name"`, `"price"`, `"marks"`, etc.
5. Display clear and meaningful output.

---

# 1️⃣ Student Information

Create a Dictionary containing the following information about a student:

* Name
* Age
* Course
* City

Display each value separately.

### Example Dictionary

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python",
    "city": "Mangalore"
}
```

### Expected Output

```text
Name = Ahmed
Age = 20
Course = Python
City = Mangalore
```

**Hint:** Access the values using their keys.

```python
student["name"]
```

---

# 2️⃣ Product Bill Calculator

Create a Dictionary containing:

* Product Name
* Price
* Quantity

Calculate the total amount.

### Formula

```text
Total = Price × Quantity
```

### Example Dictionary

```python
product = {
    "name": "Laptop",
    "price": 45000,
    "quantity": 2
}
```

### Expected Output

```text
Product = Laptop
Price = 45000
Quantity = 2
Total Amount = 90000
```

---

# 3️⃣ Student Result Calculator

Create a Dictionary containing a student's name and marks in three subjects.

### Example

```python
student = {
    "name": "Sara",
    "english": 75,
    "maths": 85,
    "science": 80
}
```

Calculate:

* Total Marks
* Average Marks
* Result

### Condition

```text
Average >= 40 → Pass
Average < 40  → Fail
```

### Expected Output

```text
Student = Sara
Total Marks = 240
Average Marks = 80.0
Result = Pass
```

**Hint:** Combine **Dictionary + Calculation + if-else**.

---

# 4️⃣ Create an Employee Dictionary Using User Input

Create an empty Dictionary:

```python
employee = {}
```

Accept the following information from the user:

* Employee Name
* Department
* Salary
* City

Store the entered values in the Dictionary.

### Sample Output

```text
Enter Employee Name: Ahmed
Enter Department: IT
Enter Salary: 45000
Enter City: Dubai

Employee Details

Name = Ahmed
Department = IT
Salary = 45000
City = Dubai
```

**Hint:**

```python
employee["name"] = input("Enter Employee Name: ")
```

Use a loop with `items()` to display the final Dictionary.

---

# 5️⃣ Student List Using Dictionaries

Create a **List containing three Dictionaries**.

Each Dictionary should contain:

* Student Name
* Marks

### Example

```python
students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 35},
    {"name": "Rahul", "marks": 72}
]
```

Use a loop to display each student's name, marks, and result.

### Condition

```text
Marks >= 40 → Pass
Marks < 40  → Fail
```

### Expected Output

```text
Ahmed - 85 - Pass
Sara - 35 - Fail
Rahul - 72 - Pass
```

**Hint:** This problem combines:

```text
List
  +
Dictionary
  +
Loop
  +
Conditional Statement
```

---

# ⭐ Bonus Question – Shopping Cart

Create a List containing product Dictionaries.

### Example

```python
products = [
    {"name": "Laptop", "price": 45000, "quantity": 1},
    {"name": "Mouse", "price": 500, "quantity": 2},
    {"name": "Keyboard", "price": 1200, "quantity": 1}
]
```

Use a loop to calculate the total for each product.

### Formula

```text
Product Total = Price × Quantity
```

Also calculate the **Grand Total** of the entire shopping cart.

### Expected Output

```text
Laptop = 45000
Mouse = 1000
Keyboard = 1200

Grand Total = 47200
```

**Hint:**

Start with:

```python
grand_total = 0
```

Inside the loop:

```text
Product Total = Price × Quantity

Grand Total = Grand Total + Product Total
```

---

# 🎯 Learning Outcomes

After completing this lab, students should be able to:

* Create Dictionaries.
* Access values using keys.
* Add values to Dictionaries.
* Accept user input into a Dictionary.
* Perform calculations using Dictionary values.
* Loop through Dictionaries using `items()`.
* Store Dictionaries inside Lists.
* Combine Lists, Dictionaries, loops, and conditional statements.
* Represent practical data such as students, employees, products, and shopping carts using Dictionaries.
