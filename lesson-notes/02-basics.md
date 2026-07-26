# Python Programming – Lesson 2 Notes

## Topic: Variables, Data Types, Operators and User Input

---

# Learning Objectives

By the end of this lesson, you will be able to:

* Understand variables.
* Store different types of data.
* Use arithmetic operators.
* Accept input from the user.
* Perform simple calculations.

---

# What is a Variable?

A **variable** is a named memory location used to store data.

Think of a variable as a **container** that stores information.

### Example

```python
name = "Ahmed"
age = 20

print(name)
print(age)
```

### Output

```
Ahmed
20
```

---

# Variable Naming Rules

✅ Variable names can contain:

* Letters
* Numbers
* Underscore (_)

❌ Variable names cannot:

* Start with a number
* Contain spaces
* Use special characters like @, #, $, %

### Valid Examples

```python
student_name = "Ali"
age = 18
marks1 = 95
```

### Invalid Examples

```python
1name = "Ali"
student name = "Ali"
my-name = "Ali"
```

---

# Data Types

Python stores different kinds of data.

| Data Type | Description     | Example  |
| --------- | --------------- | -------- |
| int       | Whole Numbers   | 25       |
| float     | Decimal Numbers | 18.5     |
| str       | Text            | "Python" |
| bool      | True or False   | True     |

### Example

```python
name = "Ahmed"
age = 20
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)
```

---

# Finding the Data Type

Use the **type()** function.

### Example

```python
name = "Ahmed"
age = 20

print(type(name))
print(type(age))
```

### Output

```
<class 'str'>
<class 'int'>
```

---

# Arithmetic Operators

| Operator | Meaning             | Example |
| -------- | ------------------- | ------- |
| +        | Addition            | 10 + 5  |
| -        | Subtraction         | 10 - 5  |
| *        | Multiplication      | 10 * 5  |
| /        | Division            | 10 / 5  |
| %        | Modulus (Remainder) | 10 % 3  |
| //       | Floor Division      | 10 // 3 |
| **       | Exponent (Power)    | 2 ** 3  |

---

# Example Program

```python
a = 15
b = 4

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Remainder =", a % b)
print("Floor Division =", a // b)
print("Power =", a ** b)
```

---

# User Input

The **input()** function accepts information from the keyboard.

### Example

```python
name = input("Enter your name: ")

print("Welcome", name)
```

---

# Why Do We Use int()?

The **input()** function always returns a **string**.

To perform mathematical calculations, convert the input into an integer.

### Example

```python
age = int(input("Enter your age: "))

print(age)
```

---

# Calculator Program

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
```

---

# Area of a Rectangle

Formula:

```
Area = Length × Width
```

### Program

```python
length = int(input("Enter length: "))
width = int(input("Enter width: "))

area = length * width

print("Area =", area)
```

---

# Perimeter of a Rectangle

Formula:

```
Perimeter = 2 × (Length + Width)
```

### Program

```python
length = int(input("Enter length: "))
width = int(input("Enter width: "))

perimeter = 2 * (length + width)

print("Perimeter =", perimeter)
```

---

# Swapping Two Variables

```python
a = 10
b = 20

print("Before Swapping")
print(a)
print(b)

temp = a
a = b
b = temp

print("After Swapping")
print(a)
print(b)
```

---

# Common Mistakes

### Forgetting int()

Incorrect

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

Input

```
10
20
```

Output

```
1020
```

---

Correct

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

Output

```
30
```

---

# Practice Programs

Write programs to:

1. Display your name, age, and city.
2. Add two numbers entered by the user.
3. Find the area of a rectangle.
4. Find the perimeter of a rectangle.
5. Find the square of a number.
6. Find the cube of a number.
7. Swap two numbers using a third variable.
8. Display the data type of different variables.

---

# Summary

In this lesson, you learned:

* Variables
* Variable naming rules
* Data types
* The `type()` function
* Arithmetic operators
* User input using `input()`
* Type conversion using `int()`
* Simple mathematical programs

---

# Key Takeaway

> **Variables store information, operators perform calculations, and `input()` allows your programs to interact with users. These three concepts form the foundation of almost every Python program you will write.**
