# 🧪 Python Lab Assignment

## If-Else, Loops & Nested Loops

### Instructions

1. Write each program in a separate Python file.
2. Use meaningful variable names.
3. Use proper indentation.
4. Accept user input wherever required.
5. Use only concepts covered so far.
6. **Attempt any 5 questions.**
7. Bonus question is optional.

---

### 1️⃣ Cinema Ticket Price Calculator ⭐

Write a program that asks the user for:

- Age
- Number of tickets

Calculate the ticket price based on age:

| Age          | Ticket Price |
| ------------ | -----------: |
| Below 5      |         Free |
| 5–12         |         ₹100 |
| 13–59        |         ₹200 |
| 60 and above |         ₹120 |

Calculate and display the **total ticket cost**.

**Example:**

```text
Enter age: 25
Enter number of tickets: 3

Ticket Price = ₹200
Total Cost = ₹600
```

**Hint:** Use `if-elif-else`.

---

### 2️⃣ Sum of Numbers Divisible by 3 ⭐⭐

Write a program to accept a number `n` and find the **sum of all numbers from 1 to n that are divisible by 3**.

**Example:**

```text
Enter n: 15

Numbers: 3 6 9 12 15
Sum = 45
```

**Hint:**

Use a `for` loop and:

```python
if number % 3 == 0:
```

---

### Question 3 – Number Analysis ⭐⭐

Write a program that accepts **10 numbers** from the user.

For each number, display whether it is:

- Positive
- Negative
- Zero

At the end, display the total count of positive, negative, and zero values.

### Example

```text
Enter number 1: 10
Positive

Enter number 2: -5
Negative

...

Positive Numbers = 6
Negative Numbers = 3
Zeros = 1
```

**Hint:** Use a `for` loop and `if-elif-else`.

---

### 4️⃣ Find the First Divisible Number ⭐⭐⭐

Ask the user to enter two numbers:

- Starting number
- Ending number

Find and display the **first number in that range that is divisible by both 4 and 6**.

**Example:**

```text
Enter starting number: 10
Enter ending number: 100

First number divisible by both 4 and 6 = 12
```

**Hint:**

A number divisible by both must satisfy:

```python
number % 4 == 0 and number % 6 == 0
```

Once you find the first one, stop the loop using `break`.

---

### 5️⃣ Number Triangle ⭐⭐⭐

Write a program using **nested loops** to display the following pattern:

```text
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

Ask the user for the number of rows.

**Example:**

```text
Enter number of rows: 4

1 2 3 4
1 2 3
1 2
1
```

**Hint:**

- Outer loop → controls rows.
- Inner loop → prints numbers.
- The number of values printed decreases with every row.

---

# ⭐ Bonus – ATM PIN Attempts ⭐⭐⭐⭐

Write a program that asks the user to enter a 4-digit PIN.

The correct PIN is:

```text
1234
```

Allow the user a maximum of **3 attempts**.

### If the PIN is correct:

```text
Access Granted
```

### If the PIN is incorrect:

```text
Incorrect PIN
Attempts remaining: 2
```

After three incorrect attempts:

```text
Account Locked
```

**Hint:**

Use a loop to control the three attempts and an `if-else` statement to check the PIN.

---

### 🎯 Concepts Covered

| Question | Main Concept                   |
| -------- | ------------------------------ |
| 1        | `if-elif-else` + calculations  |
| 2        | Loop + condition + accumulator |
| 3        | Loop + reverse `range()`       |
| 4        | Loop + `and` + `break`         |
| 5        | Nested loops + pattern         |
| 6        | Nested loops + coordinates     |
| Bonus    | Loop + `if-else` + `break`     |

This set gives students **new problem-solving scenarios** rather than repeating the standard examples they've already practiced.
