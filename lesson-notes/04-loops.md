# Python Programming – Lesson 4 Notes

# Topic: Loops in Python (`for` Loop and `while` Loop)

---

# Learning Objectives

By the end of this lesson, you will be able to:

- Understand why loops are used.
- Use the `for` loop.
- Use the `while` loop.
- Generate sequences using the `range()` function.
- Write programs using loops.
- Understand infinite loops and how to avoid them.

---

# What is a Loop?

A **loop** is used to execute the same block of code multiple times without writing it repeatedly.

### Without a Loop

```python
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
print("Welcome")
```

This approach is repetitive.

### Using a Loop

```python
for i in range(5):
    print("Welcome")
```

Both programs produce the same output, but the second program is much shorter and easier to maintain.

---

# The `for` Loop

The `for` loop is used when we know how many times we want to repeat a task.

## Syntax

```python
for variable in range(start, stop):
    statements
```

---

# Understanding `range()`

The `range()` function generates a sequence of numbers.

| Statement       | Output     |
| --------------- | ---------- |
| `range(5)`      | 0 1 2 3 4  |
| `range(1,6)`    | 1 2 3 4 5  |
| `range(2,11,2)` | 2 4 6 8 10 |

---

# Program 1 – Print Numbers from 1 to 10

```python
for i in range(1, 11):
    print(i)
```

### Output

```text
1
2
3
4
5
6
7
8
9
10
```

---

# Program 2 – Print Even Numbers

```python
for i in range(2, 21, 2):
    print(i)
```

### Output

```text
2
4
6
8
10
12
14
16
18
20
```

---

# Program 3 – Print Odd Numbers

```python
for i in range(1, 20, 2):
    print(i)
```

### Output

```text
1
3
5
7
9
11
13
15
17
19
```

---

# Program 4 – Multiplication Table

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

### Sample Output

```text
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

# Program 5 – Sum of Numbers from 1 to 10

```python
total = 0

for i in range(1, 11):
    total = total + i

print("Sum =", total)
```

### Output

```text
Sum = 55
```

---

# Program 6 – Countdown

```python
for i in range(10, 0, -1):
    print(i)

print("Blast Off!")
```

### Output

```text
10
9
8
7
6
5
4
3
2
1
Blast Off!
```

---

# The `while` Loop

A `while` loop executes as long as a condition is **True**.

## Syntax

```python
while condition:
    statements
```

---

# Program 7 – Print Numbers from 1 to 10

```python
i = 1

while i <= 10:
    print(i)
    i = i + 1
```

### Output

```text
1
2
3
4
5
6
7
8
9
10
```

---

# Program 8 – Multiplication Table Using `while`

```python
number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i = i + 1
```

---

# Program 9 – Sum of First 100 Numbers

```python
i = 1
total = 0

while i <= 100:
    total = total + i
    i = i + 1

print("Sum =", total)
```

---

# Program 10 – Display a Name Five Times

```python
name = input("Enter your name: ")

for i in range(5):
    print(name)
```

---

# Difference Between `for` and `while`

| `for` Loop                                  | `while` Loop                                    |
| ------------------------------------------- | ----------------------------------------------- |
| Used when the number of iterations is known | Used when the number of iterations is not known |
| Uses `range()` frequently                   | Uses a condition                                |
| Easier to write for fixed repetitions       | More flexible for condition-based repetition    |

---

# Infinite Loop

An infinite loop never ends because its condition is always true.

### Example

```python
while True:
    print("Hello")
```

**Press `Ctrl + C` in the terminal to stop an infinite loop.**

---

# Common Mistakes

## Forgetting to Update the Loop Variable

Incorrect

```python
i = 1

while i <= 5:
    print(i)
```

This creates an infinite loop because `i` never changes.

Correct

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

---

## Incorrect Indentation

Incorrect

```python
for i in range(5):
print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

# Practice Programs

Write Python programs to:

1. Print numbers from **1 to 20**.
2. Print numbers from **20 to 1**.
3. Print all even numbers from **1 to 50**.
4. Print all odd numbers from **1 to 50**.
5. Display the multiplication table of a given number.
6. Find the sum of numbers from **1 to 50**.
7. Display your name **10 times**.
8. Print the square of numbers from **1 to 10**.
9. Print the cube of numbers from **1 to 10**.
10. Count from **100 to 1** using a `while` loop.

---

# Quick Quiz

1. What is a loop?
2. Which loop is best when the number of repetitions is known?
3. Which function generates a sequence of numbers?
4. What is the output of `range(5)`?
5. What causes an infinite loop?
6. What is the difference between `for` and `while` loops?

---

# Summary

In this lesson, you learned:

- The purpose of loops
- `for` loop
- `while` loop
- The `range()` function
- Multiplication tables using loops
- Summation using loops
- Infinite loops
- Common programming mistakes

---

# Key Takeaway

> **Loops eliminate repetitive code by allowing a block of statements to execute multiple times. The `for` loop is ideal for a known number of iterations, while the `while` loop is best when repetition depends on a condition.**
