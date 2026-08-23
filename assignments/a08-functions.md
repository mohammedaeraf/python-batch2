# 🧪 Lab Assignment 08 – Functions in Python

## 📘 Instructions

1. Write each program in a separate Python file.
2. Use **functions** for the main task in every question.
3. Use meaningful function and variable names.
4. Use parameters wherever required.
5. Use `return` when the function needs to send a result back.
6. Test your functions with different values.
7. Avoid using concepts that have not yet been taught.

---

## 1️⃣ Calculate the Area of a Circle ⭐

Create a function called:

```python
calculate_area(radius)
```

The function should calculate and **return** the area of a circle.

### Formula

```text
Area = π × radius × radius
```

You may use:

```python
pi = 3.14
```

### Example

```text
Enter radius: 5

Area = 78.5
```

**Hint:**

```python
def calculate_area(radius):
    # calculate area
    # return area
```

---

## 2️⃣ Check Eligibility to Vote ⭐⭐

Create a function called:

```python
check_voting_eligibility(age)
```

The function should return:

```text
"Eligible to Vote"
```

if the age is **18 or above**, otherwise return:

```text
"Not Eligible to Vote"
```

### Example

```text
Enter age: 20

Eligible to Vote
```

**Hint:** Use `if-else` inside the function.

---

## 3️⃣ Calculate Total, Average and Result ⭐⭐

Create a function:

```python
calculate_result(marks1, marks2, marks3)
```

The function should:

1. Calculate the total marks.
2. Calculate the average.
3. Determine whether the student has passed.

### Condition

```text
Average >= 40 → Pass
Average < 40  → Fail
```

### Example

```text
Enter English Marks: 75
Enter Maths Marks: 80
Enter Science Marks: 65

Total = 220
Average = 73.33
Result = Pass
```

**Hint:** The function can return more than one value.

For example:

```python
return total, average, result
```

---

## 4️⃣ Find the Sum of Numbers ⭐⭐⭐

Create a function:

```python
calculate_sum(n)
```

The function should calculate the sum of all numbers from `1` to `n` using a **loop**.

### Example

```text
Enter n: 10

Sum = 55
```

Because:

```text
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
```

**Hint:**

```python
total = 0

for i in range(1, n + 1):
    total = total + i
```

The function should **return** the total.

---

## 5️⃣ Simple Calculator Using Functions ⭐⭐⭐

Create four separate functions:

```python
add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
```

Each function should return the appropriate result.

The main program should ask the user for:

* First number
* Second number

Then display the results.

### Example

```text
Enter first number: 20
Enter second number: 5

Addition = 25
Subtraction = 15
Multiplication = 100
Division = 4.0
```

**Hint:**

```python
def add(a, b):
    return a + b
```

Create similar functions for the other operations.

---

# ⭐ Bonus Question – Number Analyzer

Create a function:

```python
analyze_number(number)
```

The function should determine whether the number is:

* Positive or Negative
* Even or Odd

### Example

```text
Enter a number: 25

Positive
Odd
```

### Another Example

```text
Enter a number: -8

Negative
Even
```

**Hint:**

Use:

```python
if number > 0:
```

and:

```python
if number % 2 == 0:
```

The function should perform the analysis and display the results.

---

# 🎯 Learning Outcomes

After completing this assignment, students should be able to:

* Define functions using `def`.
* Call functions.
* Pass arguments to functions.
* Use parameters.
* Use `if-else` inside functions.
* Use loops inside functions.
* Return calculated values.
* Use multiple parameters.
* Create multiple functions for different tasks.
* Break a larger program into smaller reusable functions.

### ⭐ Concepts Practiced

```text
Functions
   ↓
Parameters
   ↓
Arguments
   ↓
if-else
   ↓
Loops
   ↓
return
```

This assignment progresses from **simple functions → functions with conditions → functions with calculations → functions with loops → multiple cooperating functions**.
