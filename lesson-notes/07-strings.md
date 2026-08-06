# Python Programming – Lesson 7 Notes

# Topic: Strings in Python

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand what a String is.
- Create and display Strings.
- Access individual characters using indexes.
- Use negative indexing.
- Extract parts of a String using slicing.
- Find the length of a String.
- Loop through characters in a String.
- Use common String methods.
- Combine Strings with loops and conditional statements.

---

# 1. What is a String?

A **String** is a sequence of characters used to store text.

Strings are written inside single or double quotation marks.

### Example

```python
name = "Ahmed"
city = 'Mangalore'

print(name)
print(city)
```

### Output

```text
Ahmed
Mangalore
```

---

# 2. Strings Can Contain Different Characters

A String can contain:

- Letters
- Numbers
- Spaces
- Symbols

### Example

```python
name = "Mohammed"
course = "Python Programming"
code = "PYTHON123"

print(name)
print(course)
print(code)
```

---

# 3. String Indexing

Just like Lists, every character in a String has an **index**.

Python indexing starts from **0**.

Consider:

```python
language = "PYTHON"
```

The indexes are:

```text
Character:   P   Y   T   H   O   N
             ↓   ↓   ↓   ↓   ↓   ↓
Index:       0   1   2   3   4   5
```

---

# 4. Accessing Characters

We can access individual characters using their index.

```python
language = "PYTHON"

print(language[0])
print(language[1])
print(language[5])
```

### Output

```text
P
Y
N
```

---

# 5. Negative Indexing

Python also allows negative indexes.

```text
Character:    P   Y   T   H   O   N

Positive:     0   1   2   3   4   5
Negative:    -6  -5  -4  -3  -2  -1
```

Example:

```python
language = "PYTHON"

print(language[-1])
print(language[-2])
```

### Output

```text
N
O
```

Remember:

```text
-1 → Last character
-2 → Second-last character
```

---

# 6. Finding the Length of a String

The `len()` function returns the number of characters in a String.

```python
name = "Python"

print(len(name))
```

### Output

```text
6
```

Spaces are also counted as characters.

```python
course = "Python Programming"

print(len(course))
```

---

# 7. String Slicing

Slicing allows us to extract a portion of a String.

### Syntax

```text
string[start:stop]
```

Example:

```python
text = "Python Programming"

print(text[0:6])
```

### Output

```text
Python
```

Remember:

> The `stop` index is **not included**.

---

# 8. More Slicing Examples

```python
text = "Python Programming"

print(text[0:6])
print(text[7:18])
```

### Output

```text
Python
Programming
```

---

# 9. Slicing from the Beginning

If the starting index is omitted, Python starts from index `0`.

```python
text = "Python Programming"

print(text[:6])
```

### Output

```text
Python
```

---

# 10. Slicing Until the End

If the ending index is omitted, Python continues until the end.

```python
text = "Python Programming"

print(text[7:])
```

### Output

```text
Programming
```

---

# 11. Looping Through a String

Because a String is a sequence of characters, we can use a `for` loop.

```python
name = "Python"

for letter in name:
    print(letter)
```

### Output

```text
P
y
t
h
o
n
```

This is very similar to looping through a List:

```python
students = ["Ahmed", "Sara", "Ali"]

for student in students:
    print(student)
```

---

# 12. Check Whether Text Exists

Use the `in` operator to check whether a character or text exists inside a String.

```python
text = "Python Programming"

if "Python" in text:
    print("Python Found")
else:
    print("Python Not Found")
```

### Output

```text
Python Found
```

---

# 13. Convert to Uppercase

Use the `upper()` method.

```python
name = "python"

print(name.upper())
```

### Output

```text
PYTHON
```

---

# 14. Convert to Lowercase

Use `lower()`.

```python
name = "PYTHON"

print(name.lower())
```

### Output

```text
python
```

---

# 15. Capitalize a String

```python
text = "python programming"

print(text.capitalize())
```

### Output

```text
Python programming
```

---

# 16. Convert Words to Title Case

Use `title()`.

```python
course = "python programming fundamentals"

print(course.title())
```

### Output

```text
Python Programming Fundamentals
```

---

# 17. Replace Text

Use `replace()` to replace part of a String.

```python
text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

### Output

```text
I like Python
```

---

# 18. Remove Extra Spaces

The `strip()` method removes spaces from the beginning and end.

```python
name = "   Ahmed   "

print(name.strip())
```

### Output

```text
Ahmed
```

---

# 19. Find the Position of Text

Use `find()`.

```python
text = "Python Programming"

position = text.find("Programming")

print(position)
```

### Output

```text
7
```

`Programming` starts at index `7`.

---

# 20. Count Characters

The `count()` method counts how many times a character or text occurs.

```python
text = "banana"

print(text.count("a"))
```

### Output

```text
3
```

---

# 21. startswith()

Checks whether a String starts with particular text.

```python
course = "Python Programming"

if course.startswith("Python"):
    print("Yes")
else:
    print("No")
```

### Output

```text
Yes
```

---

# 22. endswith()

Checks whether a String ends with particular text.

```python
filename = "assignment.py"

if filename.endswith(".py"):
    print("Python File")
else:
    print("Not a Python File")
```

### Output

```text
Python File
```

---

# 23. Joining Strings

Strings can be combined using the `+` operator.

```python
first_name = "Ahmed"
last_name = "Khan"

full_name = first_name + " " + last_name

print(full_name)
```

### Output

```text
Ahmed Khan
```

This is called **String Concatenation**.

---

# 24. Repeating a String

The `*` operator can repeat a String.

```python
text = "Python "

print(text * 3)
```

### Output

```text
Python Python Python
```

---

# 25. Program – Count the Number of Vowels

Let's combine:

**Strings + Loops + Conditional Statements**

```python
text = input("Enter a word: ")

count = 0

for letter in text:

    if letter in "aeiouAEIOU":
        count = count + 1

print("Number of Vowels =", count)
```

### Sample Output

```text
Enter a word: Education

Number of Vowels = 5
```

---

# 26. Program – Count a Particular Character

```python
text = input("Enter some text: ")
letter = input("Enter character to search: ")

count = 0

for ch in text:

    if ch == letter:
        count = count + 1

print("Occurrences =", count)
```

### Sample Output

```text
Enter some text: banana
Enter character to search: a

Occurrences = 3
```

Python also provides:

```python
text.count(letter)
```

But solving it with a loop helps us understand the programming logic.

---

# 27. Program – Reverse a String

```python
text = input("Enter a word: ")

reverse = ""

for letter in text:
    reverse = letter + reverse

print("Reverse =", reverse)
```

### Sample Output

```text
Enter a word: Python

Reverse = nohtyP
```

---

# 28. String Slicing Shortcut for Reverse

Python also allows us to reverse a String using slicing:

```python
text = "Python"

print(text[::-1])
```

### Output

```text
nohtyP
```

For beginners, it is useful to first understand the **loop-based solution** before learning the shortcut.

---

# 29. Program – Palindrome Checker

A **palindrome** is a word that reads the same forwards and backwards.

Examples:

```text
madam
level
radar
civic
```

Program:

```python
word = input("Enter a word: ")

reverse = word[::-1]

if word == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

### Sample Output

```text
Enter a word: madam

Palindrome
```

---

# 30. Program – Count Uppercase and Lowercase Letters

```python
text = input("Enter some text: ")

upper = 0
lower = 0

for letter in text:

    if letter.isupper():
        upper = upper + 1

    elif letter.islower():
        lower = lower + 1

print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)
```

---

# 31. Useful String Methods

| Method         | Purpose                         |
| -------------- | ------------------------------- |
| `upper()`      | Converts to uppercase           |
| `lower()`      | Converts to lowercase           |
| `capitalize()` | Capitalizes first character     |
| `title()`      | Capitalizes each word           |
| `strip()`      | Removes leading/trailing spaces |
| `replace()`    | Replaces text                   |
| `find()`       | Finds position                  |
| `count()`      | Counts occurrences              |
| `startswith()` | Checks starting text            |
| `endswith()`   | Checks ending text              |
| `isupper()`    | Checks uppercase                |
| `islower()`    | Checks lowercase                |

---

# 32. Lists vs Strings

Lists and Strings have several similarities.

### List

```python
fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])
```

### String

```python
name = "Python"

print(name[0])
```

Both support:

- Indexing
- Negative indexing
- Slicing
- `len()`
- `in`
- Loops

---

# Important Difference: Strings are Immutable

Lists can be modified:

```python
fruits = ["Apple", "Mango"]

fruits[0] = "Orange"

print(fruits)
```

But individual characters in a String cannot be changed directly.

This will produce an error:

```python
name = "Python"

name[0] = "J"
```

Strings are therefore called **immutable**.

---

# Common Mistake – Index Out of Range

```python
name = "Python"

print(name[10])
```

This produces an error because `"Python"` only has indexes `0` through `5`.

---

# Common Mistake – Forgetting Quotes

Incorrect:

```python
name = Python
```

Correct:

```python
name = "Python"
```

Text values must be enclosed within quotes.

---

# Practice Programs

Write Python programs to:

### 1. Display Each Character

Accept a name and display every character on a separate line.

---

### 2. Count Characters

Accept a sentence and display the total number of characters.

---

### 3. Convert Case

Accept a name and display it in:

- Uppercase
- Lowercase
- Title Case

---

### 4. Count Vowels

Accept a word and count the number of vowels.

---

### 5. Character Search

Accept a word and a character. Check whether the character exists in the word.

---

### 6. Reverse a String

Accept a word and display it in reverse.

---

### 7. Palindrome Checker

Check whether the entered word is a palindrome.

Example:

```text
madam → Palindrome
python → Not a Palindrome
```

---

# Quick Quiz

1. What is a String?
2. Which quotation marks can be used to create Strings?
3. What is the index of the first character?
4. What does index `-1` represent?
5. What does `len()` do?
6. What is String slicing?
7. Which method converts a String to uppercase?
8. What does `strip()` do?
9. Which method can count occurrences of a character?
10. Can individual characters of a String be changed directly?
11. What does **immutable** mean?
12. What is a palindrome?

---

# Summary

In this lesson, you learned:

- Creating Strings
- String indexing
- Negative indexing
- String slicing
- `len()`
- Looping through Strings
- `in` operator
- String concatenation
- `upper()` and `lower()`
- `capitalize()` and `title()`
- `strip()`
- `replace()`
- `find()`
- `count()`
- `startswith()` and `endswith()`
- Reversing Strings
- Palindrome checking
- String immutability

---

# Key Takeaway

> **A String is a sequence of characters. Many concepts learned with Lists—such as indexing, slicing, `len()`, loops, and the `in` operator—also work with Strings. However, unlike Lists, Strings are immutable and cannot be modified character by character.**
