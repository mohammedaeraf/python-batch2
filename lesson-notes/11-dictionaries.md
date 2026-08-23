# Python Programming – Lesson 10 Notes

# Topic: Dictionaries in Python

---

## Learning Objectives

By the end of this lesson, you will be able to:

* Understand what a Dictionary is.
* Understand **keys and values**.
* Create and display Dictionaries.
* Access and modify values.
* Add and remove items.
* Loop through Dictionaries.
* Check whether a key exists.
* Use common Dictionary methods.
* Create Dictionaries representing real-world data.

---

# 1. What is a Dictionary?

A **Dictionary** stores data in the form of:

```text
Key : Value
```

For example, consider information about a student:

```text
Name    → Ahmed
Age     → 20
Course  → Python
Marks   → 85
```

Instead of storing these values separately, we can create a Dictionary.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print(student)
```

### Output

```text
{'name': 'Ahmed', 'age': 20, 'course': 'Python', 'marks': 85}
```

---

# 2. Key-Value Pairs

A Dictionary contains **keys** and **values**.

Consider:

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}
```

Here:

| Key      | Value  |
| -------- | ------ |
| `name`   | Ahmed  |
| `age`    | 20     |
| `course` | Python |

We can think of a Dictionary as:

```text
Key        Value
 ↓           ↓

"name"  :  "Ahmed"
"age"   :  20
"course":  "Python"
```

---

# 3. Creating a Dictionary

Dictionaries are created using **curly brackets `{ }`**.

```python
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2025
}

print(car)
```

---

# 4. Dictionary Values Can Have Different Data Types

```python
product = {
    "name": "Laptop",
    "price": 55000,
    "rating": 4.5,
    "available": True
}

print(product)
```

The values can contain:

* Strings
* Integers
* Decimal numbers
* Boolean values
* Lists
* Tuples
* Other Dictionaries

---

# 5. Accessing Dictionary Values

Unlike Lists and Tuples, we don't normally access Dictionary values using numeric indexes.

We use the **key**.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

print(student["name"])
print(student["course"])
```

### Output

```text
Ahmed
Python
```

---

# 6. Accessing Values Using get()

Another way to access a value is using `get()`.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

print(student.get("name"))
print(student.get("age"))
```

### Output

```text
Ahmed
20
```

---

# 7. Why Use get()?

Consider:

```python
student = {
    "name": "Ahmed",
    "age": 20
}

print(student["marks"])
```

Since `"marks"` does not exist, Python generates an error.

But:

```python
print(student.get("marks"))
```

returns:

```text
None
```

without crashing the program.

---

# 8. Modifying a Dictionary Value

Dictionaries are **mutable**, which means their values can be changed.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

student["age"] = 21

print(student)
```

The age is now changed from `20` to `21`.

---

# 9. Adding a New Item

A new key-value pair can be added easily.

```python
student = {
    "name": "Ahmed",
    "age": 20
}

student["course"] = "Python"

print(student)
```

### Output

```text
{'name': 'Ahmed', 'age': 20, 'course': 'Python'}
```

---

# 10. Practical Example – Product

```python
product = {
    "name": "Laptop",
    "price": 55000
}

product["brand"] = "Dell"
product["stock"] = 10

print(product)
```

The Dictionary now contains four pieces of information about the product.

---

# 11. Removing an Item Using pop()

Use `pop()` to remove an item using its key.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

student.pop("age")

print(student)
```

### Output

```text
{'name': 'Ahmed', 'course': 'Python'}
```

---

# 12. Removing Using del

The `del` keyword can also remove an item.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

del student["age"]

print(student)
```

---

# 13. Finding the Number of Items

Use `len()`.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

print(len(student))
```

### Output

```text
3
```

The Dictionary contains three key-value pairs.

---

# 14. Checking Whether a Key Exists

Use the `in` operator.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

if "course" in student:
    print("Course information is available")
else:
    print("Course information is not available")
```

---

# 15. Getting All Keys

Use the `keys()` method.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

print(student.keys())
```

You can also loop through the keys:

```python
for key in student.keys():
    print(key)
```

### Output

```text
name
age
course
```

---

# 16. Getting All Values

Use `values()`.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

for value in student.values():
    print(value)
```

### Output

```text
Ahmed
20
Python
```

---

# 17. Getting Keys and Values Together

Use `items()`.

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

for key, value in student.items():
    print(key, "=", value)
```

### Output

```text
name = Ahmed
age = 20
course = Python
```

This is one of the most useful ways to loop through a Dictionary.

---

# 18. Looping Through a Dictionary

If we write:

```python
for x in student:
    print(x)
```

Python loops through the **keys**.

For example:

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

for x in student:
    print(x)
```

### Output

```text
name
age
course
```

---

# 19. Display Keys and Their Values

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}

for key in student:
    print(key, "=", student[key])
```

### Output

```text
name = Ahmed
age = 20
course = Python
```

---

# 20. Useful Dictionary Methods

| Method     | Purpose             |
| ---------- | ------------------- |
| `get()`    | Get a value         |
| `keys()`   | Get all keys        |
| `values()` | Get all values      |
| `items()`  | Get keys and values |
| `pop()`    | Remove an item      |
| `update()` | Add/update items    |
| `clear()`  | Remove all items    |

---

# 21. Using update()

`update()` can be used to modify existing values.

```python
student = {
    "name": "Ahmed",
    "age": 20
}

student.update({"age": 21})

print(student)
```

It can also add new values:

```python
student.update({"course": "Python"})
```

---

# 22. Practical Program – Student Information

```python
student = {
    "name": "Ahmed",
    "english": 75,
    "maths": 85,
    "science": 80
}

total = student["english"] + student["maths"] + student["science"]

average = total / 3

print("Student =", student["name"])
print("Total =", total)
print("Average =", average)
```

### Output

```text
Student = Ahmed
Total = 240
Average = 80.0
```

This demonstrates how Dictionaries can represent real-world objects.

---

# 23. Practical Program – Product Information

```python
product = {
    "name": "Laptop",
    "price": 55000,
    "quantity": 2
}

total = product["price"] * product["quantity"]

print("Product =", product["name"])
print("Price =", product["price"])
print("Quantity =", product["quantity"])
print("Total =", total)
```

### Output

```text
Product = Laptop
Price = 55000
Quantity = 2
Total = 110000
```

---

# 24. Accept User Input into a Dictionary

We can also create Dictionary values using user input.

```python
student = {}

student["name"] = input("Enter Name: ")
student["age"] = int(input("Enter Age: "))
student["course"] = input("Enter Course: ")

print(student)
```

### Sample Output

```text
Enter Name: Ahmed
Enter Age: 20
Enter Course: Python

{'name': 'Ahmed', 'age': 20, 'course': 'Python'}
```

---

# 25. Practical Program – Employee Details

```python
employee = {}

employee["name"] = input("Enter Employee Name: ")
employee["salary"] = int(input("Enter Salary: "))
employee["department"] = input("Enter Department: ")

print("\nEmployee Details")

for key, value in employee.items():
    print(key, "=", value)
```

---

# 26. Dictionary Containing a List

A Dictionary value can also be a List.

```python
student = {
    "name": "Ahmed",
    "subjects": ["Python", "HTML", "CSS"]
}

print(student["name"])
print(student["subjects"])
```

### Output

```text
Ahmed
['Python', 'HTML', 'CSS']
```

We can access an individual subject:

```python
print(student["subjects"][0])
```

### Output

```text
Python
```

---

# 27. Loop Through a List Inside a Dictionary

```python
student = {
    "name": "Ahmed",
    "subjects": ["Python", "HTML", "CSS"]
}

print("Student:", student["name"])

for subject in student["subjects"]:
    print(subject)
```

---

# 28. List of Dictionaries

This is an important real-world concept.

Suppose we have several students.

```python
students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Rahul", "marks": 78}
]
```

Each student is represented by a Dictionary.

The Dictionaries are stored inside a List.

---

# 29. Loop Through a List of Dictionaries

```python
students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Rahul", "marks": 78}
]

for student in students:
    print(student["name"], "-", student["marks"])
```

### Output

```text
Ahmed - 85
Sara - 92
Rahul - 78
```

This pattern is extremely common in real-world Python applications.

---

# 30. Dictionary + Loop + Conditional Statement

```python
students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 35},
    {"name": "Rahul", "marks": 78}
]

for student in students:

    if student["marks"] >= 40:
        print(student["name"], "- Pass")
    else:
        print(student["name"], "- Fail")
```

### Output

```text
Ahmed - Pass
Sara - Fail
Rahul - Pass
```

This combines:

```text
Dictionary
     +
List
     +
Loop
     +
Conditional Statement
```

---

# 31. Why are Dictionaries Important?

Dictionaries are used extensively in real-world programming.

For example, information about a product might look like:

```python
product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "stock": 20
}
```

This is much easier to understand than:

```python
product = [101, "Laptop", 55000, 20]
```

With the List, we need to remember:

```text
0 → ID
1 → Name
2 → Price
3 → Stock
```

With a Dictionary:

```text
"id"
"name"
"price"
"stock"
```

make the data self-explanatory.

---

# 32. Dictionaries and JSON

Students will frequently encounter data that looks like this when working with APIs and web applications:

```text
{
    "name": "Ahmed",
    "age": 20,
    "course": "Python"
}
```

This resembles a Python Dictionary.

It is one reason understanding Dictionaries is very important before learning:

* APIs
* JSON
* Web Development
* Data Processing

---

# 33. List vs Tuple vs Set vs Dictionary

| Feature        | List  | Tuple | Set   | Dictionary    |
| -------------- | ----- | ----- | ----- | ------------- |
| Syntax         | `[ ]` | `( )` | `{ }` | `{key:value}` |
| Ordered        | Yes   | Yes   | No    | Yes           |
| Indexing       | Yes   | Yes   | No    | By Key        |
| Duplicates     | Yes   | Yes   | No    | Keys: No      |
| Mutable        | Yes   | No    | Yes   | Yes           |
| Key-Value Data | No    | No    | No    | ✅ Yes         |

---

# Common Mistake 1 – Accessing Using Numeric Index

Incorrect:

```python
student = {
    "name": "Ahmed",
    "age": 20
}

print(student[0])
```

Correct:

```python
print(student["name"])
```

Dictionaries are accessed using **keys**.

---

# Common Mistake 2 – Accessing a Key That Doesn't Exist

```python
student = {
    "name": "Ahmed"
}

print(student["marks"])
```

This produces an error.

A safer approach is:

```python
print(student.get("marks"))
```

---

# Common Mistake 3 – Duplicate Keys

Avoid:

```python
student = {
    "name": "Ahmed",
    "name": "Rahul"
}
```

Dictionary keys must be unique.

The later value will replace the earlier value.

---

# Practice Programs

## 1. Student Details

Create a Dictionary containing:

* Name
* Age
* Course
* City

Display all values.

---

## 2. Product Details

Create a Dictionary containing:

* Product Name
* Price
* Quantity

Calculate:

```text
Total = Price × Quantity
```

Display the product details and total amount.

---

## 3. Employee Information

Accept employee details from the user:

* Name
* Department
* Salary

Store them in a Dictionary and display them.

---

## 4. Student Result

Create:

```python
student = {
    "name": "Ahmed",
    "english": 75,
    "maths": 85,
    "science": 80
}
```

Calculate:

* Total
* Average
* Pass / Fail

---

## 5. Student List

Create a List containing three student Dictionaries.

Each student should have:

```text
Name
Marks
```

Use a loop to display each student's name and marks.

---

# Quick Quiz

1. What is a Dictionary?
2. What is a key-value pair?
3. Which brackets are used to create a Dictionary?
4. How do we access a Dictionary value?
5. What is the difference between `student["name"]` and `student.get("name")`?
6. Can Dictionary values be modified?
7. How do you add a new key-value pair?
8. What does `keys()` return?
9. What does `values()` return?
10. What does `items()` return?
11. Which method removes an item?
12. Can a Dictionary contain a List?
13. Can a List contain Dictionaries?
14. Why are Dictionaries useful for real-world data?

---

# Summary

In this lesson, you learned:

* Creating Dictionaries
* Keys and values
* Accessing values
* `get()`
* Adding and modifying items
* Removing items
* `keys()`
* `values()`
* `items()`
* Looping through Dictionaries
* User input with Dictionaries
* Dictionaries containing Lists
* Lists containing Dictionaries
* Combining Dictionaries with loops and conditions
* Real-world uses of Dictionaries

---

# Key Takeaway

> **A Dictionary stores information as key-value pairs. Instead of remembering numeric positions, we use meaningful keys such as `"name"`, `"price"`, or `"marks"` to access data. This makes Dictionaries one of the most useful data structures in practical Python programming.**
