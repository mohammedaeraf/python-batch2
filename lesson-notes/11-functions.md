# Python Lesson Notes – Functions

## Topic: Functions in Python

### Learning Objectives

By the end of this lesson, students will be able to:

- Understand what a function is.
- Create and call functions.
- Pass arguments to functions.
- Use multiple parameters.
- Return values from functions.
- Understand the difference between `print()` and `return`.
- Use default arguments.
- Apply functions to practical problems.

---

# 1. What is a Function?

A **function** is a reusable block of code designed to perform a specific task.

For example, instead of writing the same code repeatedly:

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

we can create a function:

```python
def welcome():
    print("Welcome to Python")
```

Then call it whenever required:

```python
welcome()
welcome()
welcome()
```

### Key Idea

> **Write once, use many times.**

---

# 2. Why Do We Need Functions?

Consider this program:

```python
print("Welcome Ahmed")
print("Welcome Sara")
print("Welcome Rahul")
```

If we need to welcome 100 students, writing the same code repeatedly is inefficient.

Functions allow us to create reusable code.

Functions provide:

- Code reusability
- Better organization
- Less repetition
- Easier debugging
- Easier maintenance

---

# 3. Creating a Function

The basic syntax is:

```python
def function_name():
    # statements
```

Example:

```python
def greet():
    print("Hello!")
```

However, defining a function does **not** execute it.

We need to **call** the function.

```python
greet()
```

### Complete Program

```python
def greet():
    print("Hello!")

greet()
```

### Output

```text
Hello!
```

---

# 4. Understanding `def`

The keyword:

```python
def
```

means that we are **defining a function**.

For example:

```python
def greet():
```

means:

> Create a function called `greet`.

---

# 5. Function with Multiple Statements

A function can contain multiple statements.

```python
def student_details():
    print("Name: Ahmed")
    print("Age: 20")
    print("Course: Python")

student_details()
```

### Output

```text
Name: Ahmed
Age: 20
Course: Python
```

---

# 6. Calling a Function Multiple Times

```python
def welcome():
    print("Welcome to Python Programming")

welcome()
welcome()
welcome()
```

### Output

```text
Welcome to Python Programming
Welcome to Python Programming
Welcome to Python Programming
```

---

# 7. Function with a Parameter

A function can receive information from outside.

```python
def greet(name):
    print("Hello", name)
```

Now we can provide a name:

```python
greet("Ahmed")
greet("Sara")
greet("Rahul")
```

### Output

```text
Hello Ahmed
Hello Sara
Hello Rahul
```

Here:

```text
name
```

is called a **parameter**.

And:

```text
"Ahmed"
"Sara"
"Rahul"
```

are called **arguments**.

---

# 8. Parameter vs Argument

Consider:

```python
def greet(name):
    print("Hello", name)

greet("Ahmed")
```

### Parameter

```python
name
```

The variable defined inside the function.

### Argument

```python
"Ahmed"
```

The actual value passed to the function.

---

# 9. Function with Two Parameters

```python
def add(a, b):
    print("Sum =", a + b)

add(10, 20)
```

### Output

```text
Sum = 30
```

We can call it with different values:

```python
add(100, 50)
add(25, 75)
```

---

# 10. Practical Example – Calculate Area

Create a function to calculate the area of a rectangle.

### Formula

```text
Area = Length × Breadth
```

```python
def calculate_area(length, breadth):
    area = length * breadth
    print("Area =", area)

calculate_area(10, 5)
```

### Output

```text
Area = 50
```

---

# 11. Function with User Input

We can take input outside the function and pass it to the function.

```python
def calculate_area(length, breadth):
    area = length * breadth
    print("Area =", area)


length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

calculate_area(length, breadth)
```

### Sample Output

```text
Enter length: 10
Enter breadth: 5
Area = 50
```

---

# 12. Functions with Different Data Types

Parameters can contain different types of data.

```python
def student_info(name, age, course):
    print("Name =", name)
    print("Age =", age)
    print("Course =", course)

student_info("Ahmed", 20, "Python")
```

---

# 13. Returning a Value

One of the most important concepts in Functions is `return`.

Consider:

```python
def add(a, b):
    return a + b
```

The function calculates the result and **returns** it.

We can store the result:

```python
result = add(10, 20)

print("Result =", result)
```

### Output

```text
Result = 30
```

---

# 14. `print()` vs `return`

This is an important distinction.

### Using print()

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

The function displays the result.

### Using return

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The function sends the result back to the calling code.

### Simple Difference

| `print()`                              | `return`                        |
| -------------------------------------- | ------------------------------- |
| Displays something                     | Sends a value back              |
| Mainly for output                      | Useful for further calculations |
| Doesn't give the result back for reuse | Result can be stored and reused |

---

# 15. Why is `return` Useful?

Suppose:

```python
def add(a, b):
    return a + b
```

We can now use the result in another calculation:

```python
result = add(10, 20)

print("Result =", result)
print("Result × 2 =", result * 2)
```

### Output

```text
Result = 30
Result × 2 = 60
```

---

# 16. Function to Calculate Square

```python
def square(number):
    return number * number

result = square(7)

print("Square =", result)
```

### Output

```text
Square = 49
```

---

# 17. Function to Check Even or Odd

```python
def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))

result = check_even_odd(number)

print(number, "is", result)
```

### Sample Output

```text
Enter a number: 15
15 is Odd
```

This example combines:

**Function + Parameter + if-else + return**

---

# 18. Function to Find Greatest of Two Numbers

```python
def greatest(a, b):

    if a > b:
        return a
    else:
        return b


result = greatest(25, 40)

print("Greatest =", result)
```

### Output

```text
Greatest = 40
```

---

# 19. Function to Find Greatest of Three Numbers

```python
def greatest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


result = greatest(25, 40, 30)

print("Greatest =", result)
```

### Output

```text
Greatest = 40
```

---

# 20. Function with a Loop

Functions can contain loops.

Example: display numbers from 1 to 10.

```python
def display_numbers():

    for i in range(1, 11):
        print(i)


display_numbers()
```

---

# 21. Function to Calculate Total

```python
def calculate_total():

    total = 0

    for i in range(1, 6):
        number = int(input("Enter number: "))
        total = total + number

    print("Total =", total)


calculate_total()
```

This demonstrates:

**Function + Loop + User Input**

---

# 22. Function with Loop and Parameter

We can make the previous program more flexible.

```python
def display_numbers(n):

    for i in range(1, n + 1):
        print(i)


display_numbers(5)
```

### Output

```text
1
2
3
4
5
```

We can also use:

```python
display_numbers(10)
```

---

# 23. Function to Calculate Factorial

The factorial of a number is:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Program:

```python
def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


number = int(input("Enter a number: "))

answer = factorial(number)

print("Factorial =", answer)
```

### Sample Output

```text
Enter a number: 5
Factorial = 120
```

---

# 24. Default Parameter

We can provide a default value for a parameter.

```python
def greet(name="Student"):
    print("Hello", name)
```

Calling without an argument:

```python
greet()
```

Output:

```text
Hello Student
```

Calling with an argument:

```python
greet("Ahmed")
```

Output:

```text
Hello Ahmed
```

---

# 25. Multiple Parameters with Default Values

```python
def student_info(name, course="Python"):

    print("Name =", name)
    print("Course =", course)


student_info("Ahmed")
```

Output:

```text
Name = Ahmed
Course = Python
```

We can also provide the course:

```python
student_info("Sara", "Java")
```

---

# 26. Keyword Arguments

Instead of relying on the order of arguments, we can specify parameter names.

```python
def student_info(name, age, course):

    print("Name =", name)
    print("Age =", age)
    print("Course =", course)


student_info(
    course="Python",
    name="Ahmed",
    age=20
)
```

The order doesn't matter when using keyword arguments.

---

# 27. Function Calling Another Function

Functions can call other functions.

```python
def add(a, b):
    return a + b


def display_result():
    result = add(10, 20)
    print("Result =", result)


display_result()
```

---

# 28. Practical Example – Simple Calculator

Let's create separate functions for different operations.

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


x = 20
y = 5

print("Addition =", add(x, y))
print("Subtraction =", subtract(x, y))
print("Multiplication =", multiply(x, y))
print("Division =", divide(x, y))
```

### Output

```text
Addition = 25
Subtraction = 15
Multiplication = 100
Division = 4.0
```

This demonstrates an important advantage of functions:

> **A large program can be divided into small, manageable tasks.**

---

# 29. Local Variables

Variables created inside a function are generally available only inside that function.

```python
def calculate():

    number = 10

    print(number)


calculate()
```

Here `number` belongs to the function.

---

# 30. Function Scope – Simple Example

```python
def test():

    message = "Hello"

    print(message)


test()
```

The variable `message` is created inside `test()`.

Students do not need to go deeply into scope at this stage. The important idea is:

> Variables created inside a function are normally local to that function.

---

# 31. A Function Does Not Run Automatically

Consider:

```python
def greet():
    print("Hello")
```

Nothing is displayed yet.

We must call:

```python
greet()
```

Therefore:

```text
Define Function
       ↓
Call Function
       ↓
Function Executes
```

---

# 32. Anatomy of a Function

Consider:

```python
def add(a, b):
    return a + b
```

| Part     | Meaning                 |
| -------- | ----------------------- |
| `def`    | Defines a function      |
| `add`    | Function name           |
| `a, b`   | Parameters              |
| `:`      | Start of function block |
| `return` | Sends result back       |
| `a + b`  | Value being returned    |

---

# 33. Recommended Naming

Use descriptive function names.

Good:

```python
calculate_area()
find_greatest()
calculate_total()
check_even_odd()
display_student()
```

Avoid:

```python
abc()
x()
fun1()
test()
```

Good names make programs easier to understand.

---

# 34. Complete Example – Student Result Function

```python
def calculate_result(marks):

    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, average, result


marks = [75, 80, 65, 90, 70]

total, average, result = calculate_result(marks)

print("Total =", total)
print("Average =", average)
print("Result =", result)
```

This example combines several concepts:

```text
List
  ↓
Function
  ↓
Calculation
  ↓
if-else
  ↓
return
```

---

# 35. Functions – Important Concepts

Students should remember these five concepts:

### 1. Define

```python
def greet():
```

### 2. Call

```python
greet()
```

### 3. Pass Arguments

```python
greet("Ahmed")
```

### 4. Return a Value

```python
return result
```

### 5. Reuse

```python
greet("Ahmed")
greet("Sara")
greet("Rahul")
```

---

# Practice Programs

### Exercise 1 – Greeting Function

Create a function called `welcome()` that displays:

```text
Welcome to Python Programming
```

Call the function three times.

---

### Exercise 2 – Square Function

Create a function:

```python
square(number)
```

that returns the square of a number.

**Formula:**

```text
Square = number × number
```

---

### Exercise 3 – Rectangle Area

Create a function:

```python
calculate_area(length, breadth)
```

that returns the area.

**Formula:**

```text
Area = Length × Breadth
```

---

### Exercise 4 – Temperature Conversion

Create a function that accepts temperature in Celsius and returns Fahrenheit.

**Formula:**

```text
Fahrenheit = (Celsius × 9/5) + 32
```

---

### Exercise 5 – Discount Calculator

Create a function that accepts:

- Price
- Discount percentage

and returns the final price.

**Formula:**

```text
Discount = Price × Discount Percentage / 100

Final Price = Price - Discount
```

---

# Quick Quiz

1. What is a function?
2. Which keyword is used to define a function?
3. What is the difference between a parameter and an argument?
4. How do you call a function?
5. What does `return` do?
6. What is the difference between `print()` and `return`?
7. Can a function have multiple parameters?
8. Can a function contain a loop?
9. What is a default parameter?
10. Why are functions useful?

---

# Summary

In this lesson, you learned:

- What functions are
- Why functions are useful
- Creating functions using `def`
- Calling functions
- Parameters and arguments
- Multiple parameters
- Returning values
- `print()` vs `return`
- Default parameters
- Keyword arguments
- Functions with loops
- Functions with conditions
- Functions calling other functions
- Building a simple calculator using functions

## Key Takeaway

> **Functions allow us to divide a program into small, reusable blocks of code.**

A useful mental model for students is:

```text
Function = Reusable Task
```

For example:

```text
calculate_area()  → calculates area
calculate_total() → calculates total
check_result()    → checks result
greet()           → displays greeting
```

Once students understand this concept, they are ready to start writing **larger programs by breaking them into smaller functions**.
