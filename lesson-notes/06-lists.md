# Python Programming – Lesson 6 Notes

# Topic: Lists in Python

---

## Learning Objectives

By the end of this lesson, you will be able to:

* Understand what a list is.
* Create and display lists.
* Access list elements using indexes.
* Modify list elements.
* Add and remove elements.
* Find the length of a list.
* Loop through a list.
* Perform simple calculations using lists.

---

# What is a List?

A **list** is used to store multiple values in a single variable.

Instead of creating separate variables:

```python id="vmsb59"
student1 = "Ahmed"
student2 = "Fatima"
student3 = "Rahul"
student4 = "Sara"
```

We can store all the names in one list:

```python id="vvabxo"
students = ["Ahmed", "Fatima", "Rahul", "Sara"]

print(students)
```

### Output

```text id="em2en4"
['Ahmed', 'Fatima', 'Rahul', 'Sara']
```

Lists are created using **square brackets `[ ]`**.

---

# Creating Lists

### List of Names

```python id="cq43nb"
students = ["Ahmed", "Fatima", "Rahul", "Sara"]

print(students)
```

### List of Numbers

```python id="v43zqy"
marks = [78, 85, 92, 67, 88]

print(marks)
```

### List of Fruits

```python id="8mqynw"
fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits)
```

---

# List Index

Every element in a list has a position called an **index**.

Python indexing starts from **0**.

Consider:

```python id="v69ppr"
fruits = ["Apple", "Mango", "Banana", "Orange"]
```

The indexes are:

```text id="a78i91"
Index       0        1         2         3
            ↓        ↓         ↓         ↓
        ["Apple", "Mango", "Banana", "Orange"]
```

Therefore:

```text id="4r0b3m"
fruits[0] → Apple
fruits[1] → Mango
fruits[2] → Banana
fruits[3] → Orange
```

---

# Accessing List Elements

```python id="c24ggf"
fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[3])
```

### Output

```text id="1o0pof"
Apple
Mango
Orange
```

---

# Negative Indexing

Python also supports negative indexes.

```text id="a3dk99"
["Apple", "Mango", "Banana", "Orange"]
    -4       -3        -2        -1
```

Example:

```python id="11pry9"
fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits[-1])
print(fruits[-2])
```

### Output

```text id="ec9vb4"
Orange
Banana
```

`-1` refers to the **last element**.

---

# Changing an Element

Lists are **mutable**, which means their values can be changed.

```python id="bm3evc"
fruits = ["Apple", "Mango", "Banana"]

fruits[1] = "Orange"

print(fruits)
```

### Output

```text id="yv9h2r"
['Apple', 'Orange', 'Banana']
```

---

# Adding an Element – `append()`

The `append()` method adds an element to the **end of the list**.

```python id="19c0cr"
students = ["Ahmed", "Fatima", "Rahul"]

students.append("Sara")

print(students)
```

### Output

```text id="1mk6ke"
['Ahmed', 'Fatima', 'Rahul', 'Sara']
```

---

# Adding an Element at a Specific Position – `insert()`

Use `insert()` to add an element at a particular index.

```python id="9u2ljh"
fruits = ["Apple", "Banana", "Orange"]

fruits.insert(1, "Mango")

print(fruits)
```

### Output

```text id="tjsd7d"
['Apple', 'Mango', 'Banana', 'Orange']
```

Here:

```text id="s2d5t4"
1 → Index
"Mango" → Value
```

---

# Removing an Element – `remove()`

```python id="1h1k72"
fruits = ["Apple", "Mango", "Banana", "Orange"]

fruits.remove("Banana")

print(fruits)
```

### Output

```text id="cmmpw9"
['Apple', 'Mango', 'Orange']
```

---

# Removing Using `pop()`

`pop()` removes an element using its index.

```python id="o0jhlp"
fruits = ["Apple", "Mango", "Banana", "Orange"]

fruits.pop(1)

print(fruits)
```

### Output

```text id="msp1ss"
['Apple', 'Banana', 'Orange']
```

Without an index, `pop()` removes the last element:

```python id="3j1y4b"
fruits.pop()
```

---

# Finding the Length of a List

Use `len()` to find the number of elements.

```python id="0vz1m6"
students = ["Ahmed", "Fatima", "Rahul", "Sara"]

print(len(students))
```

### Output

```text id="2jhb64"
4
```

---

# Checking Whether an Element Exists

Use the `in` operator.

```python id="lnk5nl"
fruits = ["Apple", "Mango", "Banana"]

if "Mango" in fruits:
    print("Mango is available")
else:
    print("Mango is not available")
```

### Output

```text id="xxm6nv"
Mango is available
```

This combines **Lists + Conditional Statements**.

---

# Looping Through a List

One of the most common operations is processing every element of a list.

```python id="o90p68"
students = ["Ahmed", "Fatima", "Rahul", "Sara"]

for student in students:
    print(student)
```

### Output

```text id="klvp55"
Ahmed
Fatima
Rahul
Sara
```

This combines **Lists + Loops**.

---

# Looping Through Numbers

```python id="ckk0ja"
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

---

# Program – Display Even Numbers from a List

```python id="ot7wg7"
numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:

    if number % 2 == 0:
        print(number)
```

### Output

```text id="fbzvcs"
10
20
30
40
```

This program combines three concepts:

```text id="btdgn4"
Lists
  +
Loops
  +
Conditional Statements
```

---

# Program – Calculate Total

```python id="fxd2bs"
marks = [78, 85, 92, 67, 88]

total = 0

for mark in marks:
    total = total + mark

print("Total =", total)
```

### Output

```text id="f49jry"
Total = 410
```

---

# Program – Calculate Total and Average

```python id="37vzvs"
marks = [78, 85, 92, 67, 88]

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Total =", total)
print("Average =", average)
```

### Output

```text id="dmrb5q"
Total = 410
Average = 82.0
```

---

# Using `sum()`

Python provides a simpler way to calculate the total.

```python id="9n97k8"
marks = [78, 85, 92, 67, 88]

total = sum(marks)

print("Total =", total)
```

For beginners, it is useful to first understand the **loop-based solution** before using `sum()`.

---

# Finding the Largest Number

Python provides the `max()` function.

```python id="u7vzml"
numbers = [25, 67, 12, 89, 34]

largest = max(numbers)

print("Largest =", largest)
```

### Output

```text id="kz1tkp"
Largest = 89
```

---

# Finding the Smallest Number

Use `min()`.

```python id="mzhd12"
numbers = [25, 67, 12, 89, 34]

smallest = min(numbers)

print("Smallest =", smallest)
```

### Output

```text id="a9oh35"
Smallest = 12
```

---

# Sorting a List

Use `sort()` to arrange values in ascending order.

```python id="2wlj3p"
numbers = [40, 10, 50, 20, 30]

numbers.sort()

print(numbers)
```

### Output

```text id="32dxm3"
[10, 20, 30, 40, 50]
```

---

# Reverse Sorting

```python id="eudovg"
numbers = [40, 10, 50, 20, 30]

numbers.sort(reverse=True)

print(numbers)
```

### Output

```text id="v37zrd"
[50, 40, 30, 20, 10]
```

---

# List Slicing

We can extract part of a list using slicing.

```python id="5kfw6u"
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

### Output

```text id="tptp21"
[20, 30, 40]
```

Remember:

```text id="bn69p5"
[start : stop]
```

The `stop` index is **not included**.

---

# Useful List Operations

| Operation     | Purpose                   |
| ------------- | ------------------------- |
| `list[index]` | Access an element         |
| `append()`    | Add to end                |
| `insert()`    | Add at a position         |
| `remove()`    | Remove by value           |
| `pop()`       | Remove by index           |
| `len()`       | Number of elements        |
| `sum()`       | Total of numeric elements |
| `max()`       | Largest value             |
| `min()`       | Smallest value            |
| `sort()`      | Sort elements             |

---

# Common Mistake – Index Out of Range

Consider:

```python id="znm1h1"
fruits = ["Apple", "Mango", "Banana"]

print(fruits[3])
```

This produces an error because the available indexes are:

```text id="m1f4gi"
0
1
2
```

The last valid index is:

```text id="yk7awz"
len(fruits) - 1
```

---

# Common Mistake – Wrong Index

Remember:

```text id="waf0lu"
First Element → Index 0

NOT

First Element → Index 1
```

Python uses **zero-based indexing**.

---

# Practice Programs

### 1. Student Names

Create a list containing five student names and display each name using a loop.

---

### 2. Even Numbers

Given:

```python id="0fydnl"
numbers = [12, 17, 20, 25, 32, 41, 50]
```

Display only the even numbers.

---

### 3. Total Marks

Given:

```python id="qbmudl"
marks = [75, 82, 91, 68, 88]
```

Calculate and display the total marks.

---

### 4. Total and Average

Calculate the total and average of:

```python id="f4mglr"
marks = [80, 75, 90, 85, 70]
```

---

### 5. Search for a Fruit

Create a list of fruits and ask the user to enter a fruit name.

Display whether the fruit exists in the list.

---

### 6. Largest and Smallest

Given:

```python id="4w6stp"
numbers = [45, 12, 78, 34, 91, 23]
```

Display the largest and smallest numbers.

---

# Quick Quiz

1. What is a list?
2. Which brackets are used to create a list?
3. What is the index of the first element?
4. What does index `-1` represent?
5. Which method adds an element to the end?
6. What is the difference between `append()` and `insert()`?
7. Which method removes an element by value?
8. What does `len()` return?
9. How can we process every element using a loop?
10. Are Python lists mutable?

---

# Summary

In this lesson, you learned:

* Creating lists
* Accessing elements
* Positive and negative indexing
* Modifying elements
* `append()`
* `insert()`
* `remove()`
* `pop()`
* `len()`
* Looping through lists
* Searching lists
* Calculating total and average
* Finding maximum and minimum values
* Sorting lists
* List slicing

---

# Key Takeaway

> **A list allows us to store and process multiple values using a single variable. When lists are combined with loops and conditional statements, we can efficiently work with large collections of data.**

