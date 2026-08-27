# 🐍 Python Tuples – Quick Reference

### 1. What is a Tuple?

A **Tuple** is a collection used to store multiple values in a single variable.

```python
student = ("Ahmed", 20, "Python")
```

Tuples use **round brackets `( )`**.

---

### 2. Tuple vs List ⭐

| List                     | Tuple                             |
| ------------------------ | --------------------------------- |
| `[ ]`                    | `( )`                             |
| **Mutable**              | **Immutable**                     |
| Can be modified          | Cannot be modified                |
| Use when data may change | Use when data should remain fixed |

**Remember:**

> **List → Can Change**
> **Tuple → Cannot Change**

---

### 3. Creating a Tuple

```python
numbers = (10, 20, 30, 40)
```

Tuples can contain different data types:

```python
student = ("Ahmed", 20, 85.5)
```

---

### 4. Accessing Elements

Tuples use indexing, starting from `0`.

```python
student = ("Ahmed", 20, "Python")

print(student[0])   # Ahmed
print(student[1])   # 20
```

---

### 5. Tuple Cannot Be Modified ⭐

```python
numbers = (10, 20, 30)

numbers[0] = 100    # ❌ Error
```

Tuples are **immutable**.

If you need to add, remove, or change elements, use a **List**.

---

### 6. Looping Through a Tuple

```python
days = ("Monday", "Tuesday", "Wednesday")

for day in days:
    print(day)
```

---

### 7. Useful Functions / Methods

```python
numbers = (10, 20, 10, 30)

print(len(numbers))       # Number of elements
print(numbers.count(10))  # Number of occurrences
print(numbers.index(30))  # Position of 30
```

---

### Practical Uses of Tuples

Use Tuples for **fixed groups of related values**:

```python
point = (10, 20)          # Coordinates

rgb = (255, 0, 0)         # Color

date = (25, 8, 2026)      # Date

days = ("Mon", "Tue", "Wed")  # Fixed values
```

---

## 🎯 Golden Rule

```text
        Does the data need to change?
                  │
          ┌───────┴───────┐
         YES              NO
          ↓                ↓
        LIST             TUPLE
```

> **LIST = Mutable**
> **TUPLE = Immutable**
