# Python Programming – Lesson 8 Notes

# Topic: Tuples in Python

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand what a Tuple is.
- Create and display Tuples.
- Access Tuple elements using indexes.
- Use negative indexing.
- Slice Tuples.
- Loop through a Tuple.
- Use common Tuple methods.
- Understand Tuple packing and unpacking.
- Understand the difference between Lists and Tuples.

---

# 1. What is a Tuple?

A **Tuple** is used to store multiple values in a single variable.

A Tuple is similar to a List, but there is one important difference:

> **Lists can be modified, but Tuples cannot be modified after they are created.**

Tuples are created using **round brackets `( )`**.

### Example

```python id="c7lg57"
fruits = ("Apple", "Mango", "Banana", "Orange")

print(fruits)
```

### Output

```text id="7vyu9j"
('Apple', 'Mango', 'Banana', 'Orange')
```

---

# 2. List vs Tuple

### List

```python id="w32n9i"
fruits = ["Apple", "Mango", "Banana"]
```

Uses:

```text id="0sc0i4"
[ ]
```

### Tuple

```python id="lhtbpm"
fruits = ("Apple", "Mango", "Banana")
```

Uses:

```text id="e3s3gn"
( )
```

---

# 3. Creating Tuples

### Tuple of Strings

```python id="v3oskw"
cities = ("Mumbai", "Dubai", "London", "Singapore")

print(cities)
```

### Tuple of Numbers

```python id="m0qyyb"
marks = (78, 85, 92, 67, 88)

print(marks)
```

### Tuple with Different Data Types

```python id="c3hp3p"
student = ("Ahmed", 20, 85.5, True)

print(student)
```

A Tuple can contain different types of data.

---

# 4. Accessing Tuple Elements

Like Lists and Strings, Tuple indexing starts from **0**.

```python id="2x0tmv"
fruits = ("Apple", "Mango", "Banana", "Orange")

print(fruits[0])
print(fruits[1])
print(fruits[3])
```

### Output

```text id="e3lgcr"
Apple
Mango
Orange
```

---

# 5. Understanding Tuple Indexes

Consider:

```python id="sg8mmz"
fruits = ("Apple", "Mango", "Banana", "Orange")
```

Indexes:

```text id="42v93j"
Index       0        1         2         3
            ↓        ↓         ↓         ↓
        ("Apple", "Mango", "Banana", "Orange")
```

---

# 6. Negative Indexing

Tuples also support negative indexes.

```text id="g5hm30"
("Apple", "Mango", "Banana", "Orange")

   -4       -3        -2        -1
```

Example:

```python id="5jydvp"
fruits = ("Apple", "Mango", "Banana", "Orange")

print(fruits[-1])
print(fruits[-2])
```

### Output

```text id="o5e5qw"
Orange
Banana
```

---

# 7. Finding the Length of a Tuple

Use `len()`.

```python id="tgz4pf"
fruits = ("Apple", "Mango", "Banana", "Orange")

print(len(fruits))
```

### Output

```text id="hox36i"
4
```

---

# 8. Tuple Slicing

Just like Lists and Strings, Tuples support slicing.

```python id="kmltsn"
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

### Output

```text id="jyr0s2"
(20, 30, 40)
```

Remember:

```text id="h6b3kz"
[start : stop]
```

The `stop` index is not included.

---

# 9. Slicing from the Beginning

```python id="quywpv"
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
```

### Output

```text id="z5q7av"
(10, 20, 30)
```

---

# 10. Slicing Until the End

```python id="vy7fmx"
numbers = (10, 20, 30, 40, 50)

print(numbers[2:])
```

### Output

```text id="41gkkx"
(30, 40, 50)
```

---

# 11. Looping Through a Tuple

We can use a `for` loop to process every element.

```python id="mcbm9d"
fruits = ("Apple", "Mango", "Banana", "Orange")

for fruit in fruits:
    print(fruit)
```

### Output

```text id="bz83hd"
Apple
Mango
Banana
Orange
```

---

# 12. Checking Whether an Element Exists

Use the `in` operator.

```python id="s7du9c"
fruits = ("Apple", "Mango", "Banana")

if "Mango" in fruits:
    print("Mango is available")
else:
    print("Mango is not available")
```

---

# 13. Tuples are Immutable

This is the most important property of a Tuple.

**Immutable** means that the values cannot be changed after the Tuple is created.

Consider:

```python id="tx30tq"
fruits = ("Apple", "Mango", "Banana")

fruits[0] = "Orange"
```

This will produce an error.

We cannot directly:

- Change elements
- Add elements
- Remove elements

from a Tuple.

---

# 14. Why Use a Tuple?

If Tuples cannot be modified, why do we need them?

Tuples are useful when data **should not change**.

Examples:

### Days of the Week

```python id="c58f4r"
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)
```

### Months

```python id="bn2f75"
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
)
```

### Coordinates

```python id="7zpmr9"
location = (12.5, 74.8)
```

These are examples of data that we generally do not want to modify accidentally.

---

# 15. Creating a Tuple with One Element

Be careful when creating a Tuple containing only one element.

Incorrect:

```python id="etj6zk"
numbers = (10)

print(type(numbers))
```

Python treats this as an integer.

Correct:

```python id="5b10by"
numbers = (10,)

print(type(numbers))
```

The comma is important.

---

# 16. Tuple Packing

Storing multiple values inside a Tuple is called **Tuple Packing**.

```python id="3bzc5e"
student = ("Ahmed", 20, "Python")

print(student)
```

Here three values are packed into one Tuple.

---

# 17. Tuple Unpacking

We can also extract Tuple values into separate variables.

```python id="f4p03p"
student = ("Ahmed", 20, "Python")

name, age, course = student

print(name)
print(age)
print(course)
```

### Output

```text id="12w0hz"
Ahmed
20
Python
```

This is called **Tuple Unpacking**.

---

# 18. Practical Example – Student Details

```python id="ttc9up"
student = ("Ahmed", 20, 85)

name, age, marks = student

print("Name =", name)
print("Age =", age)
print("Marks =", marks)
```

### Output

```text id="d03ifd"
Name = Ahmed
Age = 20
Marks = 85
```

---

# 19. count() Method

The `count()` method tells us how many times a value occurs.

```python id="4vff49"
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))
```

### Output

```text id="akffpr"
3
```

---

# 20. index() Method

The `index()` method finds the position of an element.

```python id="04cxqe"
fruits = ("Apple", "Mango", "Banana", "Orange")

print(fruits.index("Banana"))
```

### Output

```text id="2u7hmj"
2
```

---

# 21. Useful Functions with Tuples

Functions learned with Lists can also be used with Tuples.

### len()

```python id="rrikfk"
numbers = (10, 20, 30, 40)

print(len(numbers))
```

### max()

```python id="vh07z4"
numbers = (10, 50, 20, 80, 30)

print(max(numbers))
```

### min()

```python id="b2qcsn"
print(min(numbers))
```

### sum()

```python id="62t1ip"
print(sum(numbers))
```

---

# 22. Program – Total and Average

```python id="cszkt9"
marks = (75, 80, 90, 85, 70)

total = sum(marks)
average = total / len(marks)

print("Total =", total)
print("Average =", average)
```

### Output

```text id="f5v5rl"
Total = 400
Average = 80.0
```

---

# 23. Program – Display Even Numbers

```python id="jpn5di"
numbers = (10, 15, 20, 25, 30, 35, 40)

for number in numbers:

    if number % 2 == 0:
        print(number)
```

### Output

```text id="6t8e83"
10
20
30
40
```

This combines:

```text id="zk9ufx"
Tuple
  +
Loop
  +
Conditional Statement
```

---

# 24. Convert Tuple to List

Sometimes we may need to modify Tuple data.

We can temporarily convert it into a List.

```python id="lylffh"
fruits = ("Apple", "Mango", "Banana")

fruits_list = list(fruits)

fruits_list.append("Orange")

print(fruits_list)
```

### Output

```text id="a3b43c"
['Apple', 'Mango', 'Banana', 'Orange']
```

---

# 25. Convert List to Tuple

We can convert it back using `tuple()`.

```python id="h28bs7"
fruits_list = ["Apple", "Mango", "Banana"]

fruits = tuple(fruits_list)

print(fruits)
```

### Output

```text id="nm75qu"
('Apple', 'Mango', 'Banana')
```

---

# Lists vs Tuples

| Feature           | List   | Tuple |
| ----------------- | ------ | ----- |
| Brackets          | `[ ]`  | `( )` |
| Ordered           | Yes    | Yes   |
| Indexing          | Yes    | Yes   |
| Negative Indexing | Yes    | Yes   |
| Slicing           | Yes    | Yes   |
| Loops             | Yes    | Yes   |
| Duplicate Values  | Yes    | Yes   |
| Can be Modified   | ✅ Yes | ❌ No |
| `append()`        | ✅ Yes | ❌ No |
| `remove()`        | ✅ Yes | ❌ No |

---

# List Example

```python id="5v4mhs"
students = ["Ahmed", "Sara", "Ali"]

students.append("Fatima")

print(students)
```

---

# Tuple Example

```python id="if3y4b"
students = ("Ahmed", "Sara", "Ali")

print(students)
```

The Tuple should be used when the values are intended to remain unchanged.

---

# Common Mistake – Trying to Modify a Tuple

Incorrect:

```python id="1qh49a"
numbers = (10, 20, 30)

numbers[0] = 100
```

Tuples are immutable.

---

# Common Mistake – Single Element Tuple

Incorrect:

```python id="1f6a94"
student = ("Ahmed")
```

Correct:

```python id="uynz24"
student = ("Ahmed",)
```

The comma creates the single-element Tuple.

---

# Practice Programs

## 1. Student Names

Create a Tuple containing five student names and display each name using a loop.

---

## 2. Total and Average

Create a Tuple containing marks of five subjects.

Display:

- Total
- Average

---

## 3. Largest and Smallest

Given:

```python id="ub10f8"
numbers = (45, 12, 78, 34, 91, 23)
```

Display the largest and smallest values.

---

## 4. Count an Element

Given:

```python id="7bfgyq"
numbers = (10, 20, 10, 30, 10, 40)
```

Find how many times `10` occurs.

---

## 5. Tuple Unpacking

Create:

```python id="5u7trq"
student = ("Ahmed", 20, "Python")
```

Unpack the Tuple and display:

```text id="3dnx8e"
Name = Ahmed
Age = 20
Course = Python
```

---

# Quick Quiz

1. What is a Tuple?
2. Which brackets are generally used for Tuples?
3. What is the index of the first Tuple element?
4. What does `-1` represent?
5. Can Tuple elements be modified?
6. What does immutable mean?
7. Which method counts occurrences of a value?
8. Which method finds the position of an element?
9. What is Tuple packing?
10. What is Tuple unpacking?
11. How do you create a single-element Tuple?
12. What is the main difference between a List and a Tuple?

---

# Summary

In this lesson, you learned:

- Creating Tuples
- Accessing Tuple elements
- Positive and negative indexing
- Tuple slicing
- Looping through Tuples
- Checking elements using `in`
- Tuple immutability
- Single-element Tuples
- Tuple packing
- Tuple unpacking
- `count()` and `index()`
- `len()`, `sum()`, `max()`, and `min()`
- Converting between Lists and Tuples
- Difference between Lists and Tuples

---

# Key Takeaway

> **A Tuple is an ordered collection similar to a List, but its elements cannot be changed after creation. Use Lists when data needs to change and Tuples when the data should remain fixed.**
