# Python – Lists vs Tuples

## 1. Introduction

Both **Lists** and **Tuples** are used to store multiple values in a single variable.

The main difference is:

> **Lists can be changed, while Tuples cannot be changed.**

---

## 2. Basic Syntax

### List

```python
students = ["Ahmed", "Sara", "Rahul"]
```

Lists use **square brackets `[ ]`**.

### Tuple

```python
students = ("Ahmed", "Sara", "Rahul")
```

Tuples use **round brackets `( )`**.

---

## 3. Main Difference – Mutability

### List can be modified

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

### Tuple cannot be modified

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This produces an error because Tuples are **immutable**.

---

## 4. Common Features

Both Lists and Tuples:

* Store multiple values
* Maintain order
* Allow duplicate values
* Support indexing
* Support negative indexing
* Support slicing
* Can be used with `for` loops
* Can contain different data types
* Support `len()`
* Support the `in` operator

Example:

```python
numbers = (10, 20, 30, 40)

print(numbers[1])
print(numbers[1:3])

for number in numbers:
    print(number)
```

---

## 5. Comparison Table

| Feature              | List  | Tuple |
| -------------------- | ----- | ----- |
| Syntax               | `[ ]` | `( )` |
| Ordered              | ✅     | ✅     |
| Duplicates           | ✅     | ✅     |
| Indexing             | ✅     | ✅     |
| Slicing              | ✅     | ✅     |
| Looping              | ✅     | ✅     |
| Mutable              | ✅     | ❌     |
| Can add/remove items | ✅     | ❌     |
| `append()`           | ✅     | ❌     |
| `remove()`           | ✅     | ❌     |
| `count()`            | ✅     | ✅     |
| `index()`            | ✅     | ✅     |

---

## 6. When Should I Use a List?

Use a **List** when the data may change.

### Examples

```python
shopping_cart = ["Laptop", "Mouse"]
```

Items can be added or removed.

```python
shopping_cart.append("Keyboard")
```

Other examples:

* Shopping cart
* To-do list
* Student marks
* List of products
* List of employees

---

## 7. When Should I Use a Tuple?

Use a **Tuple** when the values represent a **fixed collection**.

### Coordinates

```python
point = (10, 20)
```

### RGB Color

```python
red = (255, 0, 0)
```

### Date

```python
date = (25, 8, 2026)
```

### Days of the Week

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)
```

---

## 8. Simple Decision Rule

Ask yourself:

> **"Will the data need to change?"**

```text
             Will data change?
                    │
          ┌─────────┴─────────┐
          │                   │
         YES                  NO
          ↓                   ↓
        LIST                TUPLE
```

### Examples

```text
Shopping Cart → List
Student Marks → List
To-Do List    → List

Coordinates   → Tuple
RGB Color     → Tuple
Date          → Tuple
Days          → Tuple
```

---

## 9. Important Point

A Tuple is **not better than a List**.

They are designed for different purposes.

> **List → Collection that can change**
> **Tuple → Fixed collection of related values**

### Quick Example

```python
# List – can change
marks = [75, 80, 85]
marks[0] = 90

# Tuple – cannot change
point = (10, 20)
# point[0] = 50  # Error
```

---

## 🎯 Key Takeaway

**Remember:**

> 📝 **List = Mutable**
> 📦 **Tuple = Immutable**

If you remember this distinction, you can make the correct choice between Lists and Tuples in most beginner-level situations.
