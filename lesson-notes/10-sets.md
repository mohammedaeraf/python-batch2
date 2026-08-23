# Python Programming – Lesson 9 Notes

# Topic: Sets in Python

---

## Learning Objectives

By the end of this lesson, you will be able to:

* Understand what a Set is.
* Create and display Sets.
* Understand why Sets do not allow duplicate values.
* Add and remove elements.
* Loop through a Set.
* Check whether an element exists.
* Perform Union, Intersection, and Difference operations.
* Understand the difference between Lists, Tuples, and Sets.

---

# 1. What is a Set?

A **Set** is a collection used to store multiple values in a single variable.

Sets are created using **curly brackets `{ }`**.

### Example

```python id="4epm9i"
fruits = {"Apple", "Mango", "Banana", "Orange"}

print(fruits)
```

### Possible Output

```text id="ciz3i9"
{'Mango', 'Apple', 'Orange', 'Banana'}
```

You may notice that the order of elements can be different.

This is because Sets are **unordered**.

---

# 2. Creating Sets

### Set of Strings

```python id="qhp9xv"
students = {"Ahmed", "Sara", "Rahul", "Fatima"}

print(students)
```

### Set of Numbers

```python id="umfry7"
numbers = {10, 20, 30, 40, 50}

print(numbers)
```

---

# 3. Sets Do Not Allow Duplicates

This is one of the most important features of Sets.

```python id="tz0bce"
numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
```

### Output

```text id="zfcf30"
{10, 20, 30, 40}
```

Although `10` and `20` were entered twice, they appear only once.

> **A Set stores only unique values.**

---

# 4. Practical Example – Remove Duplicates

Suppose we have a List:

```python id="yzkrvk"
numbers = [10, 20, 10, 30, 20, 40, 30]

print(numbers)
```

Output:

```text id="1scblc"
[10, 20, 10, 30, 20, 40, 30]
```

Convert the List to a Set:

```python id="2skwsb"
numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = set(numbers)

print(unique_numbers)
```

### Output

```text id="v3ubq9"
{10, 20, 30, 40}
```

This is a very common use of Sets.

---

# 5. Sets are Unordered

Sets do not maintain elements by position like Lists and Tuples.

Therefore, we should not rely on the displayed order of a Set.

```python id="rjmgl9"
fruits = {"Apple", "Mango", "Banana"}

print(fruits)
```

The order may differ when the program runs.

---

# 6. Sets Do Not Support Indexing

With a List, we can write:

```python id="dqdgzg"
fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])
```

But this does **not** work with Sets:

```python id="odjn4v"
fruits = {"Apple", "Mango", "Banana"}

print(fruits[0])
```

This will produce an error.

Sets do not support:

* Indexing
* Negative indexing
* Slicing

---

# 7. Looping Through a Set

Although Sets do not support indexing, we can loop through them.

```python id="it9q2q"
fruits = {"Apple", "Mango", "Banana", "Orange"}

for fruit in fruits:
    print(fruit)
```

Remember that the order may vary.

---

# 8. Finding the Length of a Set

Use `len()`.

```python id="4pm0um"
fruits = {"Apple", "Mango", "Banana", "Orange"}

print(len(fruits))
```

### Output

```text id="0ejowz"
4
```

---

# 9. Check Whether an Element Exists

Use the `in` operator.

```python id="psl0pm"
fruits = {"Apple", "Mango", "Banana"}

if "Mango" in fruits:
    print("Mango is available")
else:
    print("Mango is not available")
```

### Output

```text id="q5pjhz"
Mango is available
```

---

# 10. Adding an Element – add()

Use the `add()` method to add one element.

```python id="99chpx"
fruits = {"Apple", "Mango", "Banana"}

fruits.add("Orange")

print(fruits)
```

`Orange` is now added to the Set.

---

# 11. Adding Multiple Elements – update()

Use `update()` to add multiple values.

```python id="v67xai"
fruits = {"Apple", "Mango"}

fruits.update(["Banana", "Orange", "Grapes"])

print(fruits)
```

---

# 12. Removing an Element – remove()

```python id="db5rj6"
fruits = {"Apple", "Mango", "Banana"}

fruits.remove("Mango")

print(fruits)
```

### Important

If the value does not exist, `remove()` produces an error.

For example:

```python id="8b7c64"
fruits.remove("Grapes")
```

will produce an error if `"Grapes"` is not present.

---

# 13. Removing Using discard()

`discard()` also removes an element.

```python id="ir8rmu"
fruits = {"Apple", "Mango", "Banana"}

fruits.discard("Mango")

print(fruits)
```

The difference is that `discard()` does **not produce an error** if the element does not exist.

```python id="v6c94l"
fruits.discard("Grapes")
```

This is safe even if `"Grapes"` is not present.

---

# 14. remove() vs discard()

| Method      | Element Exists | Element Doesn't Exist |
| ----------- | -------------- | --------------------- |
| `remove()`  | Removes it     | Error                 |
| `discard()` | Removes it     | No Error              |

---

# 15. Empty Set

Be careful when creating an empty Set.

This:

```python id="8wpjtv"
numbers = {}
```

does **not** create an empty Set.

It creates an empty Dictionary.

To create an empty Set:

```python id="o4jtc6"
numbers = set()

print(numbers)
```

---

# 16. Set Operations

One of the most powerful features of Sets is the ability to perform mathematical Set operations.

The three most important operations for beginners are:

1. Union
2. Intersection
3. Difference

---

# 17. Union

**Union** combines all unique elements from two Sets.

Consider:

```python id="5oyvcu"
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Use:

```python id="ucjibk"
result = a.union(b)

print(result)
```

### Output

```text id="vfgv12"
{1, 2, 3, 4, 5, 6}
```

Another way:

```python id="sf3v8o"
result = a | b
```

The `|` symbol represents Union.

---

# 18. Intersection

**Intersection** returns the values that exist in **both Sets**.

```python id="q9tqmd"
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)

print(result)
```

### Output

```text id="0hwxkf"
{3, 4}
```

Another way:

```python id="e0fh4f"
result = a & b
```

The `&` symbol represents Intersection.

---

# 19. Difference

**Difference** returns elements that exist in the first Set but not in the second Set.

```python id="82e2yb"
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.difference(b)

print(result)
```

### Output

```text id="t3i5ao"
{1, 2}
```

Another way:

```python id="4grqrf"
result = a - b
```

---

# 20. Understanding Difference

Consider:

```python id="7nx1qa"
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Then:

```text id="yicb6f"
A - B = {1, 2}

B - A = {5, 6}
```

Therefore, the order matters when performing Difference.

---

# 21. Symmetric Difference

Symmetric Difference returns elements that are in either Set but **not in both**.

```python id="12dqma"
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.symmetric_difference(b)

print(result)
```

### Output

```text id="0j2ny9"
{1, 2, 5, 6}
```

Another way:

```python id="7un8pd"
result = a ^ b
```

---

# 22. Set Operations Summary

Given:

```python id="z71e8d"
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

| Operation                    | Result               |
| ---------------------------- | -------------------- |
| Union `a \| b`               | `{1, 2, 3, 4, 5, 6}` |
| Intersection `a & b`         | `{3, 4}`             |
| Difference `a - b`           | `{1, 2}`             |
| Difference `b - a`           | `{5, 6}`             |
| Symmetric Difference `a ^ b` | `{1, 2, 5, 6}`       |

---

# 23. Practical Example – Students in Two Courses

Suppose:

```python id="ws8tl5"
python_students = {"Ahmed", "Sara", "Ali", "Fatima"}

web_students = {"Ali", "Fatima", "Rahul", "Zeeshan"}
```

### Students Enrolled in Either Course

```python id="tj97yj"
print(python_students | web_students)
```

### Students Enrolled in Both Courses

```python id="5ls99g"
print(python_students & web_students)
```

### Students Only in Python

```python id="1cmnd8"
print(python_students - web_students)
```

This demonstrates a real-world use of Sets.

---

# 24. Program – Find Common Numbers

```python id="c06r9d"
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2

print("Common Numbers =", common)
```

### Output

```text id="d9z85x"
Common Numbers = {30, 40}
```

---

# 25. Program – Remove Duplicate Names

```python id="28t1y8"
students = [
    "Ahmed",
    "Sara",
    "Ali",
    "Ahmed",
    "Fatima",
    "Sara"
]

unique_students = set(students)

print(unique_students)
```

Duplicate names are automatically removed.

---

# 26. Useful Set Methods

| Method                   | Purpose                     |
| ------------------------ | --------------------------- |
| `add()`                  | Add one element             |
| `update()`               | Add multiple elements       |
| `remove()`               | Remove an element           |
| `discard()`              | Safely remove an element    |
| `union()`                | Combine Sets                |
| `intersection()`         | Find common elements        |
| `difference()`           | Find different elements     |
| `symmetric_difference()` | Elements not common to both |
| `clear()`                | Remove all elements         |

---

# 27. Lists vs Tuples vs Sets

| Feature    | List  | Tuple | Set   |
| ---------- | ----- | ----- | ----- |
| Syntax     | `[ ]` | `( )` | `{ }` |
| Ordered    | Yes   | Yes   | No    |
| Indexing   | Yes   | Yes   | No    |
| Slicing    | Yes   | Yes   | No    |
| Duplicates | Yes   | Yes   | No    |
| Mutable    | Yes   | No    | Yes   |
| Loops      | Yes   | Yes   | Yes   |

---

# 28. When Should We Use a Set?

Sets are particularly useful when:

### You Need Unique Values

```python id="q28y82"
numbers = [10, 20, 10, 30, 20]

unique = set(numbers)
```

### You Need to Find Common Values

```python id="4xq6mw"
a = {10, 20, 30}
b = {20, 30, 40}

print(a & b)
```

### You Need to Compare Groups

For example:

* Students enrolled in two courses
* Products available in two stores
* Common skills between employees
* Unique visitor IDs
* Common subjects between courses

---

# Common Mistakes

## Trying to Access a Set Using an Index

Incorrect:

```python id="mngmyw"
fruits = {"Apple", "Mango", "Banana"}

print(fruits[0])
```

Sets do not support indexing.

---

## Expecting Duplicate Values

```python id="8jyjbd"
numbers = {10, 10, 20, 20, 30}

print(numbers)
```

Output:

```text id="r62w6v"
{10, 20, 30}
```

Duplicates are automatically removed.

---

## Creating an Empty Set Incorrectly

Incorrect:

```python id="b4skjg"
myset = {}
```

Correct:

```python id="3dw2xs"
myset = set()
```

---

# Practice Programs

## 1. Remove Duplicates

Given:

```python id="8ynbmf"
numbers = [10, 20, 10, 30, 20, 40, 30]
```

Display only unique numbers.

---

## 2. Common Students

Given:

```python id="w95bt7"
class_a = {"Ahmed", "Sara", "Ali", "Fatima"}

class_b = {"Ali", "Fatima", "Rahul"}
```

Display students who are present in both classes.

---

## 3. Combine Two Sets

Create two Sets containing five numbers each and display their Union.

---

## 4. Set Difference

Create two Sets and display the elements that exist only in the first Set.

---

## 5. Add and Remove Elements

Create a Set of five fruits.

* Add a new fruit.
* Remove one fruit.
* Display the final Set.

---

# Quick Quiz

1. What is a Set?
2. Which brackets are used to create a Set?
3. Are Sets ordered?
4. Do Sets allow duplicate values?
5. Do Sets support indexing?
6. Which method adds an element?
7. What is the difference between `remove()` and `discard()`?
8. What does Union do?
9. What does Intersection do?
10. What does Difference do?
11. How do you create an empty Set?
12. What is one practical use of a Set?

---

# Summary

In this lesson, you learned:

* Creating Sets
* Unique values
* Unordered collections
* `add()` and `update()`
* `remove()` and `discard()`
* Looping through Sets
* Membership using `in`
* Union
* Intersection
* Difference
* Symmetric Difference
* Removing duplicates
* Comparing Lists, Tuples, and Sets

---

# Key Takeaway

> **Sets are ideal when you need to work with unique values or compare groups of data. Their most powerful features are Union, Intersection, and Difference.**
