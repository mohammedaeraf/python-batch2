# 🐍 Python Lesson Notes: Exception Handling

## 1. Learning Objectives

By the end of this lesson, students will be able to:

* Understand what an **exception** is.
* Recognize common Python errors.
* Use `try` and `except`.
* Handle specific exceptions.
* Use `else` and `finally`.
* Prevent programs from crashing because of common user input errors.
* Create simple practical programs using Exception Handling.

---

# 2. What is an Exception?

An **exception** is an error that occurs while a program is running.

For example:

```python
number = int(input("Enter a number: "))
print(number)
```

If the user enters:

```text
abc
```

Python cannot convert `"abc"` into an integer and produces an error.

```text
ValueError
```

Without Exception Handling, the program stops.

---

# 3. Why Do We Need Exception Handling?

Consider this program:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a / b

print("Result =", result)
```

If the user enters:

```text
Enter first number: 20
Enter second number: 0
```

Python produces:

```text
ZeroDivisionError
```

and the program stops.

Exception Handling allows us to **handle the problem gracefully**.

Instead of:

```text
Program crashes ❌
```

we can display:

```text
Cannot divide by zero.
```

and continue the program.

---

# 4. Basic `try-except`

The basic syntax is:

```python
try:
    # Code that might cause an error

except:
    # Code to handle the error
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print("Number =", number)

except:
    print("Invalid input.")
```

If the user enters:

```text
25
```

Output:

```text
Number = 25
```

If the user enters:

```text
abc
```

Output:

```text
Invalid input.
```

---

# 5. Understanding the Flow

```text
             try
              ↓
        Run the code
              ↓
       ┌──────┴──────┐
       │             │
     No Error      Error
       │             │
       ↓             ↓
    Continue       except
                     ↓
               Handle Error
```

---

# 6. Example – Division

```python
try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except:

    print("Something went wrong.")
```

If the user enters:

```text
20
5
```

Output:

```text
Result = 4.0
```

If the user enters `0` as the second number, the `except` block runs.

---

# 7. Specific Exceptions ⭐

Instead of using a general `except`, it is better to specify what type of error we expect.

For example:

```python
try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Please enter a valid number.")
```

`ValueError` occurs when a value has the correct general type expected by an operation but an inappropriate value is supplied—for example, trying to convert `"hello"` to an integer.

---

# 8. `ValueError`

A common example:

```python
try:

    age = int(input("Enter your age: "))

    print("Age =", age)

except ValueError:

    print("Please enter a number.")
```

### Input

```text
Enter your age: twenty
```

### Output

```text
Please enter a number.
```

---

# 9. `ZeroDivisionError`

Consider:

```python
try:

    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

Input:

```text
Enter number: 20
Enter divisor: 0
```

Output:

```text
Cannot divide by zero.
```

---

# 10. Handling Multiple Exceptions

A program can have more than one possible error.

```python
try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result =", result)

except ValueError:

    print("Please enter numbers only.")

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

Now the program handles two different problems.

---

# 11. Why Specific Exceptions Are Better

Compare:

```python
except:
    print("Something went wrong.")
```

with:

```python
except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

The second approach is better because the user receives a **meaningful message**.

> Handle different errors differently whenever possible.

---

# 12. `else` with Exception Handling

Python also provides an `else` block.

The `else` block runs **only when no exception occurs**.

### Syntax

```python
try:
    # Possible error

except:
    # Error occurred

else:
    # No error
```

Example:

```python
try:

    number = int(input("Enter a number: "))

except ValueError:

    print("Invalid number.")

else:

    print("You entered:", number)
```

---

# 13. Understanding `try-except-else`

```text
           try
            ↓
      Error occurred?
       /          \
     YES           NO
      ↓             ↓
   except         else
      ↓             ↓
 Handle error   Continue normally
```

---

# 14. `finally`

The `finally` block runs **whether an exception occurs or not**.

### Syntax

```python
try:
    # Code

except:
    # Handle error

finally:
    # Always runs
```

Example:

```python
try:

    number = int(input("Enter a number: "))

    print("Number =", number)

except ValueError:

    print("Invalid input.")

finally:

    print("Program completed.")
```

If there is an error:

```text
Invalid input.
Program completed.
```

If there is no error:

```text
Number = 25
Program completed.
```

---

# 15. Why Use `finally`?

`finally` is commonly used for **cleanup operations**.

For example:

* Closing files
* Closing database connections
* Releasing resources

Example:

```python
try:
    file = open("students.txt", "r")
    print(file.read())

finally:
    file.close()
```

However, when using:

```python
with open(...) as file:
```

Python handles closing the file automatically, so a separate `finally` is usually unnecessary for that particular case.

---

# 16. Practical Example – Safe Calculator

```python
try:

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = number1 + number2

    elif operation == "-":
        result = number1 - number2

    elif operation == "*":
        result = number1 * number2

    elif operation == "/":
        result = number1 / number2

    else:
        result = None
        print("Invalid operation.")

    if result is not None:
        print("Result =", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

This combines concepts students already know:

```text
Input
  +
if-elif-else
  +
Exception Handling
```

---

# 17. Practical Example – Safe Number Input

Suppose we want the user to enter a number.

```python
try:

    number = int(input("Enter a number: "))

    print("Square =", number * number)

except ValueError:

    print("Invalid input. Please enter an integer.")
```

This is a very common real-world use of Exception Handling.

---

# 18. Repeatedly Asking Until Valid Input

We can combine Exception Handling with a loop.

```python
while True:

    try:

        number = int(input("Enter a number: "))

        print("You entered:", number)

        break

    except ValueError:

        print("Invalid input. Try again.")
```

### Example

```text
Enter a number: abc
Invalid input. Try again.

Enter a number: hello
Invalid input. Try again.

Enter a number: 25
You entered: 25
```

This is an excellent practical example for students.

---

# 19. Handling List Index Errors

Consider:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

There is no index `5`.

Python produces:

```text
IndexError
```

We can handle it:

```python
numbers = [10, 20, 30]

try:

    index = int(input("Enter index: "))

    print(numbers[index])

except IndexError:

    print("Invalid index.")

except ValueError:

    print("Please enter a number.")
```

---

# 20. Handling a Missing File

This is especially relevant because students have already learned **File Handling**.

```python
try:

    with open("students.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:

    print("The file does not exist.")
```

This is a very practical combination of:

```text
File Handling
      +
Exception Handling
```

---

# 21. Common Python Exceptions

Students don't need to memorize every exception, but these are useful to know:

| Exception           | Common Cause                 |
| ------------------- | ---------------------------- |
| `ValueError`        | Invalid value conversion     |
| `ZeroDivisionError` | Dividing by zero             |
| `IndexError`        | Invalid List index           |
| `KeyError`          | Dictionary key doesn't exist |
| `FileNotFoundError` | File doesn't exist           |
| `TypeError`         | Incompatible data types      |
| `NameError`         | Variable doesn't exist       |

---

# 22. `KeyError` Example

Consider:

```python
student = {
    "name": "Ahmed",
    "marks": 85
}

print(student["age"])
```

There is no `"age"` key.

This produces a `KeyError`.

We can handle it:

```python
student = {
    "name": "Ahmed",
    "marks": 85
}

try:

    print(student["age"])

except KeyError:

    print("Age information is not available.")
```

---

# 23. `TypeError` Example

Consider:

```python
number = 10
name = "Ahmed"

print(number + name)
```

Python cannot add an integer and a String.

This produces a `TypeError`.

We can handle it:

```python
try:

    number = 10
    name = "Ahmed"

    print(number + name)

except TypeError:

    print("These values cannot be added.")
```

---

# 24. `NameError` Example

```python
try:

    print(student_name)

except NameError:

    print("The variable does not exist.")
```

This happens when Python cannot find the variable being referenced.

---

# 25. Catching Multiple Exceptions Together

Sometimes different errors can be handled with the same message.

We can write:

```python
try:

    number = int(input("Enter number: "))

except (ValueError, TypeError):

    print("Invalid input.")
```

For beginners, however, handling specific exceptions separately is usually clearer.

---

# 26. Avoid Using a Bare `except` Everywhere

You may see:

```python
try:
    # code

except:
    print("Error")
```

This catches almost everything, which can hide problems you didn't expect.

Prefer:

```python
except ValueError:
```

or:

```python
except ZeroDivisionError:
```

when you know what can go wrong.

### Good Practice

> **Catch the specific exception you expect.**

---

# 27. Exception Handling Does Not Fix the Problem

This is an important concept.

Exception Handling does **not** magically fix an error.

For example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")
```

The invalid input is still invalid.

The program simply **handles the situation gracefully** instead of crashing.

---

# 28. Exception Handling vs `if-else`

Students may ask:

> "Why not just use `if-else`?"

Use `if-else` when you can **predictably check a condition**.

Example:

```python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

Use Exception Handling when an operation may **raise an error**.

Example:

```python
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Please enter a valid age.")
```

They solve different kinds of problems.

---

# 29. Complete Structure

Students should understand this pattern:

```python
try:

    # Code that may cause an exception

except SomeException:

    # Handle the exception

else:

    # Runs if there was no exception

finally:

    # Always runs
```

Not every program needs all four parts.

The most common beginner pattern is:

```python
try:

    # Risky code

except SomeException:

    # Handle error
```

---

# 30. Practical Program – Student Marks

Let's combine several concepts.

```python
try:

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("\nStudent =", name)
    print("Marks =", marks)
    print("Result =", result)

except ValueError:

    print("Please enter valid marks.")
```

This protects the program if the user enters:

```text
Enter marks: eighty
```

---

# 31. Practical Program – File Handling + Exception Handling

```python
try:

    with open("students.txt", "r") as file:

        for student in file:
            print(student.strip())

except FileNotFoundError:

    print("students.txt was not found.")
```

This is a particularly important example because it connects the **previous lesson** with today's lesson.

---

# 32. Practical Program – Search Student in File

```python
try:

    search_name = input("Enter student name: ")

    found = False

    with open("students.txt", "r") as file:

        for name in file:

            if name.strip() == search_name:
                found = True
                break

    if found:
        print("Student found.")
    else:
        print("Student not found.")

except FileNotFoundError:

    print("Student file does not exist.")
```

Now students are combining:

```text
File Handling
+
Loops
+
if-else
+
Strings
+
Exception Handling
```

---

# 33. Practice Exercises

## Exercise 1 – Safe Division

Write a program that asks for two numbers and divides them.

Handle:

* Invalid number input
* Division by zero

Expected messages:

```text
Please enter valid numbers.
```

or:

```text
Cannot divide by zero.
```

---

## Exercise 2 – Safe Integer Input

Ask the user to enter an integer.

If the user enters invalid data, display:

```text
Invalid input. Please enter an integer.
```

Keep asking until a valid integer is entered.

---

## Exercise 3 – List Index

Create:

```python
numbers = [10, 20, 30, 40, 50]
```

Ask the user for an index and display the corresponding value.

Handle:

* Invalid index
* Non-numeric input

---

## Exercise 4 – Dictionary Key

Create:

```python
student = {
    "name": "Ahmed",
    "marks": 85,
    "course": "Python"
}
```

Ask the user for a key and display its value.

Handle `KeyError` if the key doesn't exist.

---

## Exercise 5 – Read a File

Ask the user for a filename.

Try to open and display the file.

If the file doesn't exist, display:

```text
File not found.
```

---

# ⭐ Challenge – Robust Calculator

Create a calculator that:

1. Accepts two numbers.
2. Accepts an operator.
3. Performs `+`, `-`, `*`, `/`.
4. Handles invalid number input.
5. Handles division by zero.
6. Handles an invalid operator.

Example:

```text
Enter first number: 20
Enter second number: 0
Enter operator: /

Cannot divide by zero.
```

---

# 📝 Quick Reference

### Basic

```python
try:
    # risky code

except:
    # handle error
```

### Specific exception

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")
```

### Multiple exceptions

```python
try:
    # code

except ValueError:
    # handle ValueError

except ZeroDivisionError:
    # handle ZeroDivisionError
```

### With `else`

```python
try:
    # code

except ValueError:
    # error

else:
    # no error
```

### With `finally`

```python
try:
    # code

except:
    # error

finally:
    # always executes
```

---

# 🎯 Key Takeaways

Remember these points:

1. **An exception is an error that occurs while a program is running.**
2. `try` contains code that might cause an exception.
3. `except` handles the exception.
4. Prefer **specific exceptions** such as `ValueError` and `ZeroDivisionError`.
5. `else` runs when there is **no exception**.
6. `finally` runs **whether an exception occurs or not**.
7. Exception Handling prevents programs from terminating unexpectedly.
8. It is especially useful when working with **user input, files, Lists, Dictionaries, and external resources**.

### ⭐ Simple Mental Model

```text
             TRY
              ↓
       Something goes wrong?
          /          \
        NO            YES
        ↓              ↓
    Continue        EXCEPT
                       ↓
                  Handle Error
```

> **Exception Handling makes programs more reliable by allowing them to respond gracefully when unexpected situations occur.**
