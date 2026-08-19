# Python Tutorial Notes: List Slicing

## 1. Introduction

**List slicing** is used to extract a portion of a list.

Instead of accessing elements one at a time:

```python
numbers[2]
numbers[3]
numbers[4]
```

we can retrieve multiple elements using slicing:

```python
numbers[2:5]
```

### Basic Syntax

```python
list[start:end]
```

The important rule is:

> **Start index is included, end index is excluded.**

---

# 2. Understanding List Indexes

Consider:

```python
numbers = [10, 20, 30, 40, 50, 60]
```

The indexes are:

```text
Positive Index:
          0    1    2    3    4    5
          ↓    ↓    ↓    ↓    ↓    ↓
List:    10   20   30   40   50   60

Negative Index:
         -6   -5   -4   -3   -2   -1
          ↓    ↓    ↓    ↓    ↓    ↓
List:    10   20   30   40   50   60
```

---

# 3. Basic Slicing

```python
numbers = [10, 20, 30, 40, 50, 60]

result = numbers[1:4]

print(result)
```

### Output

```text
[20, 30, 40]
```

Why?

```text
numbers[1:4]

Index:     0    1    2    3    4    5
           ↓    ↓    ↓    ↓
List:     10   20   30   40   50   60
                └────────┘
```

Indexes `1`, `2`, and `3` are selected.

Index `4` is **not included**.

---

# 4. Slicing from the Beginning

We can omit the starting index.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])
```

### Output

```text
[10, 20, 30]
```

This means:

```python
numbers[0:3]
```

So:

```text
[:3] → Start from the beginning and stop before index 3
```

---

# 5. Slicing to the End

We can omit the ending index.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[3:])
```

### Output

```text
[40, 50, 60]
```

This means:

```text
[3:] → Start at index 3 and continue to the end
```

---

# 6. Copying a List Using Slicing

A useful application of slicing is creating a copy of a list.

```python
numbers = [10, 20, 30, 40, 50]

copy_numbers = numbers[:]

print("Original =", numbers)
print("Copy =", copy_numbers)
```

### Output

```text
Original = [10, 20, 30, 40, 50]
Copy = [10, 20, 30, 40, 50]
```

---

# 7. Slicing with Negative Indexes

Negative indexes count from the end.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[-3:])
```

### Output

```text
[40, 50, 60]
```

This means:

> Get the last 3 elements.

Another example:

```python
print(numbers[-5:-2])
```

Output:

```text
[20, 30, 40]
```

---

# 8. List Slicing with Step

So far we have used:

```python
list[start:end]
```

We can also specify a **step**.

### Syntax

```python
list[start:end:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:6:2])
```

Output:

```text
[10, 30, 50]
```

It selects:

```text
Index 0 → 10
Index 2 → 30
Index 4 → 50
```

So `2` means:

> Take every second element.

---

# 9. Alternate Elements

We don't need to specify the start and end.

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[::2])
```

Output:

```text
[10, 30, 50, 70]
```

Here:

```text
::2
```

means:

> Start from the beginning, go to the end, taking every second element.

---

# 10. Taking Every Third Element

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(numbers[::3])
```

Output:

```text
[10, 40, 70]
```

---

# 11. Reverse a List Using Slicing

One of the most useful examples:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

The `-1` step means:

> Move backwards one element at a time.

---

# 12. Reverse a List – Another Example

```python
names = ["Ahmed", "Sara", "Rahul", "Fatima"]

print(names[::-1])
```

Output:

```text
['Fatima', 'Rahul', 'Sara', 'Ahmed']
```

---

# 13. Combining Start, End and Step

Consider:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

Now:

```python
print(numbers[1:7:2])
```

Output:

```text
[20, 40, 60]
```

Explanation:

```text
Start = index 1
End   = index 7
Step  = 2
```

Selected indexes:

```text
1 → 20
3 → 40
5 → 60
```

Index `7` is not included.

---

# 14. Slicing Does Not Change the Original List

This is important.

```python
numbers = [10, 20, 30, 40, 50]

result = numbers[1:4]

print("Original =", numbers)
print("Sliced =", result)
```

Output:

```text
Original = [10, 20, 30, 40, 50]
Sliced = [20, 30, 40]
```

The original list remains unchanged.

---

# 15. Practical Example – Student Marks

```python
marks = [75, 82, 91, 68, 84, 95, 77]

print("All Marks =", marks)

print("First 3 Marks =", marks[:3])

print("Last 3 Marks =", marks[-3:])

print("Alternate Marks =", marks[::2])

print("Reverse Marks =", marks[::-1])
```

### Output

```text
All Marks = [75, 82, 91, 68, 84, 95, 77]
First 3 Marks = [75, 82, 91]
Last 3 Marks = [84, 95, 77]
Alternate Marks = [75, 91, 84, 77]
Reverse Marks = [77, 95, 84, 68, 91, 82, 75]
```

---

# 16. Practical Example – Months

```python
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

print("First Quarter =", months[:3])
print("Second Quarter =", months[3:6])
print("Third Quarter =", months[6:9])
print("Fourth Quarter =", months[9:])
```

### Output

```text
First Quarter = ['January', 'February', 'March']
Second Quarter = ['April', 'May', 'June']
Third Quarter = ['July', 'August', 'September']
Fourth Quarter = ['October', 'November', 'December']
```

This is a good example to demonstrate how slicing can be useful in **real-world data**.

---

# 17. Slicing vs Indexing

Students often confuse these two.

### Indexing

```python
numbers[2]
```

Returns **one element**:

```text
30
```

### Slicing

```python
numbers[2:5]
```

Returns **multiple elements**:

```text
[30, 40, 50]
```

| Operation | Example        | Result         |
| --------- | -------------- | -------------- |
| Indexing  | `numbers[2]`   | `30`           |
| Slicing   | `numbers[2:5]` | `[30, 40, 50]` |

---

# 18. Common Slicing Patterns

For:

```python
numbers = [10, 20, 30, 40, 50, 60]
```

| Expression      | Meaning           | Result                     |
| --------------- | ----------------- | -------------------------- |
| `numbers[:3]`   | First 3           | `[10, 20, 30]`             |
| `numbers[3:]`   | From index 3      | `[40, 50, 60]`             |
| `numbers[1:4]`  | Index 1 to 3      | `[20, 30, 40]`             |
| `numbers[-3:]`  | Last 3            | `[40, 50, 60]`             |
| `numbers[::2]`  | Every 2nd element | `[10, 30, 50]`             |
| `numbers[::-1]` | Reverse           | `[60, 50, 40, 30, 20, 10]` |

---

# 19. Classroom Demo Program

This is a good program to demonstrate the complete concept:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Original List =", numbers)

print("First 3 =", numbers[:3])

print("Last 3 =", numbers[-3:])

print("Middle Elements =", numbers[2:6])

print("Alternate Elements =", numbers[::2])

print("Reverse =", numbers[::-1])
```

### Ask Students

Before running the program, ask them to **predict the output** of each statement.

This makes slicing much easier for beginners to understand.

---

# 🧩 Practice Exercises

### Exercise 1

Given:

```python
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
```

Display:

1. First 4 elements
2. Last 4 elements
3. Elements from index 2 to 5
4. Every alternate element
5. Reverse of the list

---

### Exercise 2

Given:

```python
names = ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan", "Aisha"]
```

Use slicing to display:

```text
First two names
Last two names
Names from index 1 to 4
Reverse order
```

---

### ⭐ Challenge

Given:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

Use **only slicing** to produce:

```text
[100, 80, 60, 40, 20]
```

**Hint:** You need to think about both the **starting position** and a **negative step**.

---

# 🎯 Key Takeaways

Remember the basic syntax:

```python
list[start:end:step]
```

The three most important rules are:

### Rule 1

**Start is included.**

```python
numbers[2:5]
```

starts at index `2`.

### Rule 2

**End is excluded.**

```python
numbers[2:5]
```

stops before index `5`.

### Rule 3

**Step controls movement.**

```python
numbers[::2]
```

takes alternate elements.

```python
numbers[::-1]
```

reverses the list.

> **List slicing is a powerful way to extract, skip, copy, and reverse elements without using a loop.**
