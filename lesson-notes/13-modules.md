# 🐍 Python Lesson Notes: Modules & `import`

## 1. Learning Objectives

By the end of this lesson, students will be able to:

* Understand what a Python module is.
* Understand why modules are useful.
* Import built-in Python modules.
* Use functions from a module.
* Import specific functions.
* Use aliases with `as`.
* Create and import their own module.
* Understand the difference between a Python file and a module.

---

# 2. What is a Module?

A **module** is a Python file containing code that can be reused in another Python program.

A module can contain:

* Functions
* Variables
* Classes
* Other Python code

For example, suppose we create a file:

```text
calculator.py
```

containing:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

We can use these functions in another Python program.

---

# 3. Why Do We Need Modules?

Imagine writing a large Python program containing:

```text
5000 lines of code
```

Keeping everything in one file can become difficult to manage.

Instead, we can divide the program into smaller files:

```text
Project
│
├── main.py
├── calculator.py
├── student.py
└── utility.py
```

Each file can contain code related to a particular task.

### Benefits of Modules

* **Code reuse**
* **Better organization**
* **Easier maintenance**
* **Smaller programs**
* **Avoid repeating code**

---

# 4. Built-in Modules

Python comes with many modules that we can use.

Some commonly used modules are:

| Module       | Purpose                             |
| ------------ | ----------------------------------- |
| `math`       | Mathematical operations             |
| `random`     | Random numbers and selections       |
| `datetime`   | Dates and times                     |
| `os`         | Operating-system related operations |
| `statistics` | Statistical calculations            |

Today we will mainly work with:

```text
math
random
datetime
```

---

# 5. Importing a Module

The basic syntax is:

```python
import module_name
```

For example:

```python
import math
```

We can then use functions from the module.

---

# 6. Using the `math` Module

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

Here:

```text
math → module
sqrt → function
25   → argument
```

The dot `.` is used to access something inside a module.

```python
math.sqrt()
```

---

# 7. More Examples from `math`

```python
import math

print(math.sqrt(64))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pow(2, 3))
```

Output:

```text
8.0
5
4
8.0
```

### Common `math` Functions

| Function            | Purpose     |
| ------------------- | ----------- |
| `math.sqrt(x)`      | Square root |
| `math.ceil(x)`      | Round up    |
| `math.floor(x)`     | Round down  |
| `math.pow(x, y)`    | Power       |
| `math.factorial(x)` | Factorial   |

---

# 8. Constants in a Module

Modules can also contain constants.

For example:

```python
import math

print(math.pi)
```

Output:

```text
3.141592653589793
```

We can use it in calculations:

```python
import math

radius = 5

area = math.pi * radius * radius

print("Area =", area)
```

Output:

```text
Area = 78.53981633974483
```

---

# 9. Practical Example – Circle Calculator

```python
import math

radius = float(input("Enter radius: "))

area = math.pi * radius * radius

print("Area =", area)
```

This is better than manually writing:

```python
pi = 3.14
```

because Python's `math` module provides a more precise value of π.

---

# 10. Importing Specific Functions

Instead of importing the entire module:

```python
import math
```

we can import a specific function:

```python
from math import sqrt
```

Now we can write:

```python
print(sqrt(25))
```

instead of:

```python
print(math.sqrt(25))
```

---

# 11. Import Multiple Functions

We can import multiple functions:

```python
from math import sqrt, ceil, floor

print(sqrt(25))
print(ceil(4.2))
print(floor(4.8))
```

---

# 12. Using an Alias

An **alias** gives another name to a module.

Syntax:

```python
import module_name as alias
```

Example:

```python
import math as m

print(m.sqrt(25))
print(m.pi)
```

Here:

```text
math → m
```

So instead of:

```python
math.sqrt()
```

we can use:

```python
m.sqrt()
```

---

# 13. Why Use an Alias?

Aliases can make code shorter.

For example:

```python
import math as m

radius = 5

area = m.pi * radius * radius

print(area)
```

However, for beginners, it is usually clearer to use:

```python
import math
```

unless there is a good reason to use an alias.

---

# 14. The `random` Module

The `random` module is used to generate random values.

```python
import random

number = random.randint(1, 10)

print(number)
```

This generates a random integer between `1` and `10`.

Each time the program runs, the result may be different.

Example:

```text
7
```

Another run:

```text
3
```

---

# 15. Random Number Game

```python
import random

number = random.randint(1, 10)

print("Random Number =", number)
```

This is a simple way to demonstrate why modules are useful.

Python already provides functionality for generating random numbers—we don't have to write the algorithm ourselves.

---

# 16. Random Choice

The `choice()` function can randomly select an item from a List.

```python
import random

fruits = ["Apple", "Mango", "Banana", "Orange"]

fruit = random.choice(fruits)

print("Selected Fruit =", fruit)
```

Possible output:

```text
Selected Fruit = Mango
```

Another run might produce:

```text
Selected Fruit = Orange
```

---

# 17. Practical Example – Dice Simulator

A dice has numbers from 1 to 6.

```python
import random

dice = random.randint(1, 6)

print("You rolled:", dice)
```

### Simulating multiple rolls

```python
import random

for i in range(5):

    dice = random.randint(1, 6)

    print("Roll", i + 1, "=", dice)
```

---

# 18. The `datetime` Module

The `datetime` module is used to work with dates and times.

```python
import datetime

today = datetime.date.today()

print(today)
```

Possible output:

```text
2026-08-26
```

The output depends on the current date.

---

# 19. Getting Current Date and Time

```python
import datetime

now = datetime.datetime.now()

print(now)
```

Possible output:

```text
2026-08-26 17:30:45.123456
```

This gives the current date and time.

---

# 20. Practical Example – Display Today's Date

```python
import datetime

today = datetime.date.today()

print("Today's Date =", today)
```

---

# 21. Creating Your Own Module ⭐

One of the most important concepts in this lesson is creating a **custom module**.

Create a file called:

```text
calculator.py
```

Put this code inside it:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
```

This file is now our module.

---

# 22. Using Our Own Module

Create another file:

```text
main.py
```

Keep both files in the same folder:

```text
Python Project
│
├── calculator.py
└── main.py
```

In `main.py`:

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
```

Output:

```text
15
5
50
```

---

# 23. Understanding What Happened

We created:

```text
calculator.py
```

with reusable functions.

Then:

```python
import calculator
```

makes those functions available in `main.py`.

We access them using:

```python
calculator.add()
calculator.subtract()
calculator.multiply()
```

This is the basic idea of **code reuse through modules**.

---

# 24. Importing Specific Functions from Our Module

Instead of:

```python
import calculator
```

we can write:

```python
from calculator import add

print(add(10, 5))
```

We imported only the `add()` function.

---

# 25. Importing Multiple Functions

```python
from calculator import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

---

# 26. A More Practical Custom Module

Create:

```text
student.py
```

```python
def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)
```

Then create:

```text
main.py
```

```python
import student

marks = [75, 80, 85, 90, 70]

total = student.calculate_total(marks)
average = student.calculate_average(marks)

print("Total =", total)
print("Average =", average)
```

Output:

```text
Total = 400
Average = 80.0
```

This demonstrates how modules can contain **reusable functions related to a particular task**.

---

# 27. Module vs Function

Students sometimes confuse these.

### Function

A function performs a particular task.

```python
def add(a, b):
    return a + b
```

### Module

A module is a Python file that can contain multiple functions.

```text
calculator.py
```

could contain:

```python
def add():
    ...


def subtract():
    ...


def multiply():
    ...
```

So:

```text
Module
   ↓
Contains functions
   ↓
Functions perform tasks
```

---

# 28. Module vs Library

At beginner level, you can think of it this way:

```text
Module → A Python file containing reusable code
Library → Collection of reusable modules/code
```

For example, Python provides many standard modules that are part of its standard library.

---

# 29. Common Import Patterns

### Import entire module

```python
import math

math.sqrt(25)
```

### Import specific function

```python
from math import sqrt

sqrt(25)
```

### Import with alias

```python
import math as m

m.sqrt(25)
```

---

# 30. Common Mistake – Forgetting `import`

This will not work:

```python
print(math.sqrt(25))
```

if we haven't imported `math`.

We need:

```python
import math

print(math.sqrt(25))
```

---

# 31. Common Mistake – Wrong Module Name

If we write:

```python
import maths
```

instead of:

```python
import math
```

Python will report that the module cannot be found.

Module names must be correct.

---

# 32. Common Mistake – File Name Conflicts

Avoid naming your own files after standard modules.

For example, don't create:

```text
random.py
```

if you intend to use:

```python
import random
```

Similarly, avoid names such as:

```text
math.py
datetime.py
random.py
```

for your own programs.

---

# 33. Practical Demo – Random Password Characters

A simple demonstration of `random.choice()`:

```python
import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(5):

    character = random.choice(characters)

    print(character)
```

This demonstrates:

* Module
* `import`
* String
* Loop
* Random selection

---

# 34. Practical Demo – Simple Number Guessing Game

This is an excellent classroom demonstration.

```python
import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct!")
else:
    print("Wrong!")
    print("The number was", secret_number)
```

This combines concepts students already know:

```text
import
  +
random
  +
input
  +
if-else
```

---

# 35. Practical Demo – Random Student Selection

```python
import random

students = [
    "Ahmed",
    "Sara",
    "Rahul",
    "Fatima",
    "Zeeshan"
]

selected_student = random.choice(students)

print("Student selected:", selected_student)
```

This is particularly relatable in a classroom.

---

# 36. Practice Exercises

### Exercise 1 – Square Root

Use the `math` module to find the square root of a number entered by the user.

Example:

```text
Enter number: 81
Square Root = 9.0
```

---

### Exercise 2 – Circle Area

Use `math.pi` to calculate the area of a circle.

```text
Enter radius: 5
Area = 78.53981633974483
```

---

### Exercise 3 – Random Number

Generate a random number between `1` and `100`.

```text
Random Number = 57
```

---

### Exercise 4 – Random Student

Create a List of 10 students and randomly select one student.

---

### Exercise 5 – Current Date

Use the `datetime` module to display today's date.

---

# ⭐ Challenge – Create Your Own Module

Create a file called:

```text
calculator.py
```

Add these functions:

```python
add()
subtract()
multiply()
divide()
```

Then create:

```text
main.py
```

Import your module and create a calculator program.

### Expected Structure

```text
Python Project
│
├── calculator.py
└── main.py
```

### Goal

Students should understand:

```text
calculator.py
       ↓
Reusable functions
       ↓
     import
       ↓
    main.py
       ↓
   Use functions
```

---

# 📝 Quick Reference

### Import a module

```python
import math
```

### Use something from the module

```python
math.sqrt(25)
```

### Import a specific function

```python
from math import sqrt

sqrt(25)
```

### Import with an alias

```python
import math as m

m.sqrt(25)
```

### Import your own module

```python
import calculator

calculator.add(10, 5)
```

---

# 🎯 Key Takeaways

Remember these points:

1. **A module is a Python file containing reusable code.**
2. Use `import` to use a module.
3. Python provides many built-in modules such as `math`, `random`, and `datetime`.
4. Use the **dot `.` operator** to access functions or values inside a module.

```python
math.sqrt(25)
```

5. You can import specific functions:

```python
from math import sqrt
```

6. You can create your **own modules** and reuse them in other programs.
7. Modules help make programs **organized, reusable, and easier to maintain**.

> **Think of a module as a toolbox: instead of building every tool yourself, you import the toolbox and use the tools you need.**
