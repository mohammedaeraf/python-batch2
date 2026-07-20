# Python Programming – Lesson 1 Notes

## Topic: Introduction to Python

---

# What is Python?

Python is a **high-level, interpreted, and easy-to-learn programming language** created by **Guido van Rossum** and released in **1991**.

Python is one of the most popular programming languages because its syntax is simple and easy to understand, making it an excellent choice for beginners as well as professional software developers.

---

# Features of Python

* Easy to Learn
* Simple and Readable Syntax
* Free and Open Source
* Cross-Platform (Windows, Linux, macOS)
* Large Standard Library
* Supports Multiple Programming Styles
* Used in Many Industries

---

# Applications of Python

Python is widely used in:

* Web Development
* Data Science
* Artificial Intelligence (AI)
* Machine Learning (ML)
* Automation and Scripting
* Desktop Applications
* Cyber Security
* Game Development
* Internet of Things (IoT)

---

# Companies Using Python

Some well-known companies that use Python include:

* Google
* Netflix
* Instagram
* Spotify
* Dropbox
* NASA
* YouTube

---

# Writing Your First Python Program

```python
print("Hello World")
```

### Output

```
Hello World
```

### Explanation

* `print()` is a built-in Python function.
* It is used to display output on the screen.
* Text enclosed in quotation marks (`" "`) is called a **string**.

---

# Printing Multiple Lines

```python
print("Welcome to Python")
print("My name is Ahmed")
print("I love programming")
```

### Output

```
Welcome to Python
My name is Ahmed
I love programming
```

Each `print()` statement displays its output on a new line.

---

# Variables

A **variable** is a named location in memory used to store data.

### Example

```python
name = "Ahmed"

print(name)
```

### Output

```
Ahmed
```

---

# Multiple Variables

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

# Printing Variables with Text

```python
name = "Ahmed"

print("Hello", name)
```

### Output

```
Hello Ahmed
```

---

# Performing Calculations

```python
a = 10
b = 20

print(a + b)
```

### Output

```
30
```

Python can perform various mathematical operations such as:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)

---

# Simple Calculator Program

```python
x = 25
y = 5

print("Addition =", x + y)
print("Subtraction =", x - y)
print("Multiplication =", x * y)
print("Division =", x / y)
```

### Output

```
Addition = 30
Subtraction = 20
Multiplication = 125
Division = 5.0
```

---

# Taking Input from the User

```python
name = input("Enter your name: ")

print("Welcome", name)
```

### Sample Output

```
Enter your name: Ahmed
Welcome Ahmed
```

The `input()` function allows the program to accept data from the user.

---

# Accepting Numbers as Input

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

### Sample Output

```
Enter first number: 10
Enter second number: 20
Sum = 30
```

### Why `int()`?

The `input()` function always returns text (a string). The `int()` function converts that text into an integer so that mathematical calculations can be performed.

---

# Common Beginner Mistakes

### Missing Quotes

Incorrect

```python
print(Hello)
```

Correct

```python
print("Hello")
```

---

### Incorrect Function Name

Incorrect

```python
Print("Hello")
```

Correct

```python
print("Hello")
```

Python is **case-sensitive**, so `print` and `Print` are different.

---

# Important Terms

| Term            | Meaning                                       |
| --------------- | --------------------------------------------- |
| Program         | A set of instructions for the computer        |
| Python          | A programming language                        |
| Function        | A reusable block of code that performs a task |
| `print()`       | Displays output on the screen                 |
| `input()`       | Accepts input from the user                   |
| Variable        | Stores data in memory                         |
| String          | Text enclosed within quotes                   |
| Integer (`int`) | Whole numbers                                 |

---

# Summary

In this lesson, you learned:

* What Python is
* Features and applications of Python
* How to write and run your first Python program
* The `print()` function
* Variables
* Arithmetic operations
* Taking user input using `input()`
* Converting text to numbers using `int()`

---

# Practice Exercises

Write Python programs to:

1. Display your name.
2. Display your city.
3. Display your school or college name.
4. Add two numbers.
5. Multiply two numbers.
6. Display your name and age together.
7. Accept your name using `input()` and greet the user.
8. Accept two numbers from the user and display their sum.

---

# Key Takeaway

> **Programming is learned by writing programs—not just by reading them. Practice every example and modify the values to understand how Python works.**
