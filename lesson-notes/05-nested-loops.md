# Python Programming – Lesson 5 Notes

# Topic: Nested Loops in Python

---

# Learning Objectives

By the end of this lesson, you will be able to:

- Understand what a nested loop is.
- Use a `for` loop inside another `for` loop.
- Understand how outer and inner loops work.
- Generate number grids.
- Generate star patterns.
- Create multiplication tables using nested loops.

---

# What is a Nested Loop?

A **nested loop** is a loop placed inside another loop.

The loop outside is called the **outer loop**.

The loop inside is called the **inner loop**.

### Basic Structure

```python
for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)
```

Here:

- `i` belongs to the outer loop.
- `j` belongs to the inner loop.
- For every single iteration of the outer loop, the inner loop completes all its iterations.

---

# Example 1 – Understanding Outer and Inner Loops

```python
for i in range(1, 4):

    print("Outer Loop:", i)

    for j in range(1, 4):
        print("   Inner Loop:", j)
```

### Output

```text
Outer Loop: 1
   Inner Loop: 1
   Inner Loop: 2
   Inner Loop: 3

Outer Loop: 2
   Inner Loop: 1
   Inner Loop: 2
   Inner Loop: 3

Outer Loop: 3
   Inner Loop: 1
   Inner Loop: 2
   Inner Loop: 3
```

### Understanding the Execution

When `i = 1`, the inner loop runs completely:

```text
j = 1
j = 2
j = 3
```

Then `i` becomes `2`, and the inner loop again starts from the beginning.

---

# Example 2 – Display Values of i and j

```python
for i in range(1, 4):

    for j in range(1, 4):
        print("i =", i, "j =", j)
```

### Output

```text
i = 1 j = 1
i = 1 j = 2
i = 1 j = 3
i = 2 j = 1
i = 2 j = 2
i = 2 j = 3
i = 3 j = 1
i = 3 j = 2
i = 3 j = 3
```

This is one of the best programs for understanding how nested loops actually execute.

---

# Using `end` with print()

Normally, `print()` moves to the next line.

Example:

```python
print("*")
print("*")
print("*")
```

Output:

```text
*
*
*
```

We can prevent this by using:

```python
print("*", end=" ")
```

This keeps the next output on the **same line**.

---

# Example 3 – Print Stars in One Row

```python
for i in range(5):
    print("*", end=" ")
```

### Output

```text
* * * * *
```

---

# Example 4 – Create a Square Pattern

Now let's combine two loops.

```python
for i in range(5):

    for j in range(5):
        print("*", end=" ")

    print()
```

### Output

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

### How Does It Work?

The **outer loop** controls the rows.

The **inner loop** controls the columns.

```text
Outer Loop → Rows
Inner Loop → Columns
```

The statement:

```python
print()
```

moves the cursor to the next line after completing each row.

---

# Example 5 – Rectangle Pattern

```python
for i in range(3):

    for j in range(6):
        print("*", end=" ")

    print()
```

### Output

```text
* * * * * *
* * * * * *
* * * * * *
```

Here:

- Outer loop runs **3 times** → 3 rows.
- Inner loop runs **6 times** → 6 columns.

---

# Example 6 – Number Grid

```python
for i in range(1, 5):

    for j in range(1, 6):
        print(j, end=" ")

    print()
```

### Output

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

---

# Example 7 – Repeating Row Numbers

Change `j` to `i` in the `print()` statement.

```python
for i in range(1, 5):

    for j in range(1, 6):
        print(i, end=" ")

    print()
```

### Output

```text
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
```

Notice how a small change produces a completely different pattern.

---

# Example 8 – Increasing Star Pattern

```python
for i in range(1, 6):

    for j in range(i):
        print("*", end=" ")

    print()
```

### Output

```text
*
* *
* * *
* * * *
* * * * *
```

### Explanation

The inner loop depends on the value of `i`.

When:

```text
i = 1 → print 1 star
i = 2 → print 2 stars
i = 3 → print 3 stars
i = 4 → print 4 stars
i = 5 → print 5 stars
```

---

# Example 9 – Increasing Number Pattern

```python
for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()
```

### Output

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

# Example 10 – Repeating Number Triangle

```python
for i in range(1, 6):

    for j in range(i):
        print(i, end=" ")

    print()
```

### Output

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

# Example 11 – Reverse Star Pattern

```python
for i in range(5, 0, -1):

    for j in range(i):
        print("*", end=" ")

    print()
```

### Output

```text
* * * * *
* * * *
* * *
* *
*
```

---

# Example 12 – Multiplication Tables from 1 to 5

Nested loops can also be used for calculations.

```python
for i in range(1, 6):

    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()
```

### Partial Output

```text
Table of 1
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10

Table of 2
2 x 1 = 2
2 x 2 = 4
...
2 x 10 = 20
```

The outer loop decides **which table** to display.

The inner loop generates the numbers from **1 to 10**.

---

# Example 13 – Multiplication Grid

```python
for i in range(1, 6):

    for j in range(1, 6):
        print(i * j, end="\t")

    print()
```

### Output

```text
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
```

`\t` inserts a tab and helps align the numbers.

---

# Example 14 – Nested Loop with Conditional Statement

We can also place an `if` statement inside nested loops.

```python
for i in range(1, 6):

    for j in range(1, 6):

        if i == j:
            print("*", end=" ")
        else:
            print("-", end=" ")

    print()
```

### Output

```text
* - - - -
- * - - -
- - * - -
- - - * -
- - - - *
```

This example combines three concepts:

```text
Loops
   +
Nested Loops
   +
Conditional Statements
```

---

# Nested `while` Loops

Nested loops can also be created using `while`.

### Example

```python
i = 1

while i <= 3:

    j = 1

    while j <= 3:
        print(i, j)
        j = j + 1

    i = i + 1
```

### Output

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

For beginners, `for` loops are usually easier for learning nested loops.

---

# Important Concept – Number of Executions

Consider:

```python
for i in range(5):

    for j in range(4):
        print("*")
```

The outer loop runs:

```text
5 times
```

The inner loop runs:

```text
4 times for every outer loop
```

Therefore:

```text
Total executions = 5 × 4 = 20
```

This is an important concept when understanding nested loops.

---

# Common Mistake 1 – Incorrect Indentation

Incorrect:

```python
for i in range(5):

for j in range(5):
    print("*")
```

Correct:

```python
for i in range(5):

    for j in range(5):
        print("*")
```

The inner loop must be indented.

---

# Common Mistake 2 – Forgetting `end`

If you write:

```python
for i in range(3):

    for j in range(3):
        print("*")
```

You will get:

```text
*
*
*
*
*
*
*
*
*
```

Instead use:

```python
print("*", end=" ")
```

to display stars on the same line.

---

# Common Mistake 3 – Forgetting `print()`

For patterns, we usually need:

```python
print()
```

after the inner loop.

Example:

```python
for i in range(5):

    for j in range(5):
        print("*", end=" ")

    print()
```

The final `print()` moves the output to the next row.

---

# Practice Programs

Write Python programs to generate the following patterns.

### Program 1

```text
* * * *
* * * *
* * * *
* * * *
```

---

### Program 2

```text
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

---

### Program 3

```text
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

---

### Program 4

```text
*
* *
* * *
* * * *
* * * * *
```

---

### Program 5

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### Program 6

```text
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
```

---

# Quick Quiz

1. What is a nested loop?
2. What is the outer loop?
3. What is the inner loop?
4. Which loop normally controls rows in a pattern?
5. Which loop normally controls columns?
6. What is the purpose of `end=" "`?
7. Why do we use an empty `print()` after the inner loop?
8. If the outer loop executes 5 times and the inner loop executes 10 times, how many times does the inner statement execute?

**Answer:** 50 times.

---

# Summary

In this lesson, you learned:

- Nested loops
- Outer and inner loops
- Nested `for` loops
- Nested `while` loops
- Using `end` with `print()`
- Creating rows and columns
- Star patterns
- Number patterns
- Multiplication tables
- Combining nested loops with conditional statements

---

# Key Takeaway

> **A nested loop is simply a loop inside another loop. The outer loop usually controls the rows, while the inner loop controls what happens within each row.**

The best way to understand nested loops is to **trace the values of `i` and `j` and practice creating patterns.**
