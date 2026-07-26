# Python Programming – Lesson 3 Notes

## Topic: Conditional Statements (if, if-else, if-elif-else)

---

# Learning Objectives

By the end of this lesson, you will be able to:

* Understand decision-making in Python.
* Use `if`, `if-else`, and `if-elif-else` statements.
* Compare values using comparison operators.
* Use logical operators (`and`, `or`, `not`).
* Write programs that make decisions based on user input.

---

# What are Conditional Statements?

Conditional statements allow a program to make decisions.

Instead of executing every line of code, the program checks a condition and executes only the appropriate block.

### Real-Life Example

Suppose a student scores 75 marks.

If the marks are greater than or equal to 40, the student **passes**.

Otherwise, the student **fails**.

---

# Comparison Operators

| Operator | Meaning                  | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal to                 | a == b  |
| !=       | Not Equal to             | a != b  |
| >        | Greater than             | a > b   |
| <        | Less than                | a < b   |
| >=       | Greater than or Equal to | a >= b  |
| <=       | Less than or Equal to    | a <= b  |

---

# The if Statement

The `if` statement executes a block of code only if the condition is true.

### Syntax

```python
if condition:
    statements
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```
You are eligible to vote.
```

---

# The if-else Statement

When the condition is false, the `else` block executes.

### Syntax

```python
if condition:
    statements
else:
    statements
```

### Example

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

### Output

```
Fail
```

---

# Program: Even or Odd Number

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

---

# Program: Positive or Negative Number

```python
number = int(input("Enter a number: "))

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")
```

---

# The if-elif-else Statement

Use `elif` when there are multiple conditions.

### Syntax

```python
if condition1:
    statements
elif condition2:
    statements
else:
    statements
```

---

# Program: Grade Calculator

```python
marks = int(input("Enter Marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Grade D")
```

---

# Program: Largest of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest Number =", a)
else:
    print("Largest Number =", b)
```

---

# Program: Largest of Three Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest Number =", a)
elif b >= a and b >= c:
    print("Largest Number =", b)
else:
    print("Largest Number =", c)
```

---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| and      | Both conditions must be true        |
| or       | At least one condition must be true |
| not      | Reverses the result                 |

---

# Example: Using `and`

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
else:
    print("Not eligible")
```

---

# Example: Using `or`

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Holiday")
else:
    print("Working Day")
```

---

# Example: Using `not`

```python
logged_in = False

if not logged_in:
    print("Please login.")
```

---

# Nested if Statement

An `if` statement inside another `if` statement is called a nested `if`.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Not Eligible")
```

---

# Common Mistakes

### Using = Instead of ==

Incorrect

```python
if marks = 40:
    print("Pass")
```

Correct

```python
if marks == 40:
    print("Pass")
```

---

### Incorrect Indentation

Incorrect

```python
if marks >= 40:
print("Pass")
```

Correct

```python
if marks >= 40:
    print("Pass")
```

Python uses indentation to identify blocks of code.

---

# Practice Programs

Write programs to:

1. Check whether a number is positive or negative.
2. Check whether a number is even or odd.
3. Find the largest of two numbers.
4. Find the largest of three numbers.
5. Check whether a student has passed or failed.
6. Display grades based on marks.
7. Check whether a person is eligible to vote.
8. Check whether a year entered by the user is a leap year. *(Hint: A leap year is divisible by 4 and not by 100, unless it is also divisible by 400.)*

---

# Quick Quiz

1. Which statement is used for decision-making in Python?
2. What is the difference between `=` and `==`?
3. When do we use `elif`?
4. What does the `and` operator do?
5. What does the `or` operator do?
6. What is a nested `if` statement?

---

# Summary

In this lesson, you learned:

* Comparison operators
* `if` statement
* `if-else` statement
* `if-elif-else` statement
* Logical operators (`and`, `or`, `not`)
* Nested `if`
* Decision-making programs

---

# Key Takeaway

> **Conditional statements allow your program to think and make decisions. They enable different actions to be performed depending on the values provided by the user, making your programs interactive and intelligent.**
