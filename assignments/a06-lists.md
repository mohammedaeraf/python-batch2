# 🧪 Lab Assignment 05 – Lists in Python

## 📘 Instructions

1. Write each program in a separate Python file.
2. Use **Lists** in all programs.
3. Use loops and conditional statements wherever required.
4. Display clear and meaningful output.
5. Test your programs with different values.

---

## 1️⃣ Display All Elements Using a Loop

Create a list containing the names of **5 students** and display each student name using a `for` loop.

### Example

```python
students = ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"]
```

### Expected Output

```text
Ahmed
Sara
Rahul
Fatima
Zeeshan
```

---

## 2️⃣ Calculate Total and Average Marks

Create a list containing marks of **5 subjects**.

Calculate and display:

- Total Marks
- Average Marks

### Example

```python
marks = [75, 82, 91, 68, 84]
```

**Hint:**

```text
Average = Total / Number of Subjects
```

### Expected Output

```text
Total Marks = 400
Average Marks = 80.0
```

---

## 3️⃣ Count Even and Odd Numbers

Create a list containing **10 numbers**.

Use a loop and conditional statement to count how many numbers are:

- Even
- Odd

### Example

```python
numbers = [12, 17, 20, 25, 32, 41, 50, 63, 70, 81]
```

**Hint:**

```python
if number % 2 == 0:
```

### Expected Output

```text
Even Numbers = 5
Odd Numbers = 5
```

---

## 4️⃣ Find the Largest and Smallest Number

Create a list of numbers and display the **largest** and **smallest** values.

### Example

```python
numbers = [45, 12, 78, 34, 91, 23, 67]
```

### Expected Output

```text
Largest Number = 91
Smallest Number = 12
```

**Hint:** You may use:

```python
max(numbers)
min(numbers)
```

### ⭐ Challenge

Try solving the same problem **without using `max()` and `min()`**, using a loop instead.

---

## 5️⃣ Search for an Item in a List

Create a list of fruits:

```python
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
```

Ask the user to enter a fruit name.

Check whether the fruit is available in the list.

### Sample Output 1

```text
Enter Fruit: Mango

Mango is available.
```

### Sample Output 2

```text
Enter Fruit: Pineapple

Pineapple is not available.
```

**Hint:** Use the `in` operator with an `if-else` statement.

---

# ⭐ Bonus Question – Separate Even and Odd Numbers

Create a list:

```python
numbers = [11, 22, 35, 40, 53, 64, 77, 80]
```

Create two empty lists:

```python
even_numbers = []
odd_numbers = []
```

Use a loop to check every number and add it to the appropriate list.

### Expected Output

```text
Original List = [11, 22, 35, 40, 53, 64, 77, 80]

Even Numbers = [22, 40, 64, 80]
Odd Numbers = [11, 35, 53, 77]
```

**Hint:** Use:

```python
append()
```

to add elements to the new lists.

---

## 🎯 Learning Outcomes

After completing this lab, students should be able to:

- Create and access Python lists.
- Iterate through lists using loops.
- Combine lists with conditional statements.
- Perform calculations on list elements.
- Search for values in lists.
- Use `min()`, `max()`, and `append()`.
- Create new lists based on conditions.
