# Python Tutorial: File Handling

## 1. Learning Objectives

By the end of this lesson, students will be able to:

* Understand File Handling in Python.
* Open and close files.
* Read data from a file.
* Write data to a file.
* Append data to an existing file.
* Understand different file modes.
* Use `with open()` safely.
* Read files line by line.
* Create simple practical programs using files.

---

# 2. What is File Handling?

So far, most of our programs have worked with data temporarily.

For example:

```python
name = input("Enter your name: ")
print(name)
```

Once the program ends, the data stored in `name` is lost.

**File Handling** allows us to store data permanently in files.

For example:

```text
Python Program
      ↓
     Data
      ↓
    File
      ↓
Saved on Computer
```

The next time the program runs, we can read the saved data.

---

# 3. Why Do We Need File Handling?

Consider a student registration program.

Without File Handling:

```text
Student enters details
        ↓
Program stores details
        ↓
Program closes
        ↓
Data is lost
```

With File Handling:

```text
Student enters details
        ↓
Program stores details
        ↓
Data saved in file
        ↓
Program closes
        ↓
Data remains available
```

Files can be used to store:

* Student information
* Employee records
* Bills
* Notes
* Logs
* Reports
* Configuration data

---

# 4. Opening a File

Python provides the `open()` function.

### Syntax

```python
open(filename, mode)
```

Example:

```python
file = open("students.txt", "r")
```

Here:

```text
students.txt → File name
r             → Mode
```

---

# 5. File Modes

The most important modes for beginners are:

| Mode | Purpose           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write             |
| `a`  | Append            |
| `x`  | Create a new file |

### Remember

```text
r → Read
w → Write
a → Append
x → Create
```

---

# 6. Reading a File

Suppose we have a file called:

```text
students.txt
```

containing:

```text
Ahmed
Sara
Rahul
Fatima
```

We can read it using:

```python
file = open("students.txt", "r")

content = file.read()

print(content)

file.close()
```

### Output

```text
Ahmed
Sara
Rahul
Fatima
```

---

# 7. Closing a File

After using a file, we should close it:

```python
file.close()
```

Example:

```python
file = open("students.txt", "r")

content = file.read()

print(content)

file.close()
```

Closing the file releases the resources used by the file.

---

# 8. Using `with open()`

Python provides a better and safer way to work with files:

```python
with open("students.txt", "r") as file:
    content = file.read()

    print(content)
```

The file is automatically closed when the `with` block ends.

### Recommended Approach

For most Python programs, prefer:

```python
with open(...) as file:
```

instead of manually using:

```python
file.close()
```

---

# 9. Reading the Entire File with `read()`

```python
with open("students.txt", "r") as file:

    content = file.read()

    print(content)
```

`read()` reads the **entire contents** of the file.

---

# 10. Reading a Specific Number of Characters

We can specify how many characters to read.

```python
with open("students.txt", "r") as file:

    content = file.read(10)

    print(content)
```

This reads the first **10 characters**.

---

# 11. Reading One Line

Use `readline()`.

Suppose the file contains:

```text
Ahmed
Sara
Rahul
```

Program:

```python
with open("students.txt", "r") as file:

    line = file.readline()

    print(line)
```

Output:

```text
Ahmed
```

Only the first line is read.

---

# 12. Reading Multiple Lines

We can call `readline()` repeatedly:

```python
with open("students.txt", "r") as file:

    print(file.readline())
    print(file.readline())
    print(file.readline())
```

This reads three lines.

However, there is a better approach for an unknown number of lines.

---

# 13. Reading a File Line by Line

We can use a `for` loop.

```python
with open("students.txt", "r") as file:

    for line in file:
        print(line)
```

This is a very useful technique.

### Concept

```text
File
 ↓
Line 1
 ↓
Line 2
 ↓
Line 3
 ↓
...
```

---

# 14. Removing Extra Newline

When reading lines, each line normally contains a newline character `\n`.

For example:

```python
with open("students.txt", "r") as file:

    for line in file:
        print(line)
```

This may produce extra spacing.

We can use `strip()`:

```python
with open("students.txt", "r") as file:

    for line in file:
        print(line.strip())
```

`strip()` removes unnecessary spaces and newline characters from the beginning and end.

---

# 15. Writing to a File

Use the `w` mode.

```python
with open("students.txt", "w") as file:

    file.write("Ahmed")
```

If the file does not exist, Python creates it.

If it already exists, its previous contents are **replaced**.

⚠️ This is important:

> **`w` mode overwrites existing file contents.**

---

# 16. Writing Multiple Lines

We can write multiple lines using `\n`.

```python
with open("students.txt", "w") as file:

    file.write("Ahmed\n")
    file.write("Sara\n")
    file.write("Rahul\n")
```

The file will contain:

```text
Ahmed
Sara
Rahul
```

---

# 17. Writing Multiple Lines Using One String

We can also write:

```python
students = "Ahmed\nSara\nRahul\n"

with open("students.txt", "w") as file:
    file.write(students)
```

---

# 18. Writing User Input to a File

This is a good beginner-level practical example.

```python
name = input("Enter your name: ")

with open("names.txt", "w") as file:
    file.write(name)

print("Name saved successfully.")
```

If the user enters:

```text
Ahmed
```

the file will contain:

```text
Ahmed
```

---

# 19. Appending to a File

The `a` mode means **append**.

Append means:

> Add new data to the end of the existing file without deleting its contents.

Example:

```python
with open("students.txt", "a") as file:

    file.write("Fatima\n")
```

If the file originally contains:

```text
Ahmed
Sara
Rahul
```

after appending:

```text
Ahmed
Sara
Rahul
Fatima
```

---

# 20. Difference Between `w` and `a`

This is very important.

### `w` – Write

```python
with open("students.txt", "w") as file:
    file.write("Ahmed\n")
```

Existing contents are replaced.

### `a` – Append

```python
with open("students.txt", "a") as file:
    file.write("Ahmed\n")
```

Existing contents are preserved and new data is added at the end.

### Remember

```text
w → Replace
a → Add to existing data
```

---

# 21. Creating a New File Using `x`

The `x` mode is used to create a new file.

```python
with open("newfile.txt", "x") as file:

    file.write("Hello Python")
```

If the file already exists, Python generates an error.

This is useful when you specifically want to ensure that you are creating a new file rather than overwriting an existing one.

---

# 22. File Modes Summary

| Mode | Meaning | Existing File           |
| ---- | ------- | ----------------------- |
| `r`  | Read    | Reads existing file     |
| `w`  | Write   | Overwrites contents     |
| `a`  | Append  | Adds to end             |
| `x`  | Create  | Error if already exists |

---

# 23. Practical Program – Save Student Name

```python
name = input("Enter student name: ")

with open("students.txt", "w") as file:
    file.write(name)

print("Student name saved.")
```

---

# 24. Practical Program – Add Multiple Students

```python
with open("students.txt", "w") as file:

    for i in range(5):

        name = input("Enter student name: ")

        file.write(name + "\n")

print("All students saved successfully.")
```

The program asks for five names and saves them in the file.

---

# 25. Practical Program – Read Student Names

```python
with open("students.txt", "r") as file:

    for name in file:
        print(name.strip())
```

---

# 26. Practical Program – Add a New Student

Suppose `students.txt` already contains:

```text
Ahmed
Sara
Rahul
```

We can add another student:

```python
name = input("Enter new student name: ")

with open("students.txt", "a") as file:
    file.write(name + "\n")

print("Student added successfully.")
```

---

# 27. Practical Program – Count Number of Lines

Suppose:

```text
students.txt

Ahmed
Sara
Rahul
Fatima
```

We can count the number of students:

```python
count = 0

with open("students.txt", "r") as file:

    for line in file:
        count = count + 1

print("Number of Students =", count)
```

Output:

```text
Number of Students = 4
```

This combines:

```text
File
 +
Loop
 +
Counter
```

---

# 28. Practical Program – Search in a File

Suppose `students.txt` contains:

```text
Ahmed
Sara
Rahul
Fatima
```

We can search for a student:

```python
search_name = input("Enter name to search: ")

found = False

with open("students.txt", "r") as file:

    for name in file:

        if name.strip() == search_name:
            found = True
            break


if found:
    print("Student found.")
else:
    print("Student not found.")
```

This combines:

```text
File
 +
Loop
 +
if-else
 +
break
```

---

# 29. Practical Program – Save Marks

```python
name = input("Enter student name: ")
marks = input("Enter marks: ")

with open("student.txt", "w") as file:

    file.write("Name: " + name + "\n")
    file.write("Marks: " + marks + "\n")

print("Student details saved.")
```

The file might contain:

```text
Name: Ahmed
Marks: 85
```

---

# 30. Reading the Saved Student Details

```python
with open("student.txt", "r") as file:

    content = file.read()

print(content)
```

Output:

```text
Name: Ahmed
Marks: 85
```

---

# 31. Understanding `\n`

`\n` represents a **new line**.

For example:

```python
text = "Hello\nPython"
print(text)
```

Output:

```text
Hello
Python
```

This is very useful when writing multiple lines to a file.

---

# 32. File Location

When we write:

```python
with open("students.txt", "w") as file:
```

Python normally looks for the file in the program's **current working directory**.

For beginner projects, keeping the `.py` file and `.txt` file in the same folder makes things simple.

Example:

```text
Python Project
│
├── students.py
└── students.txt
```

---

# 33. Handling File Not Found

Suppose we try:

```python
with open("students.txt", "r") as file:
    print(file.read())
```

If `students.txt` doesn't exist, Python will generate an error.

We can handle this using `try-except`.

```python
try:

    with open("students.txt", "r") as file:
        print(file.read())

except FileNotFoundError:

    print("File not found.")
```

For beginners, understand the basic idea:

> `try` → attempt the operation
> `except` → handle an error if it occurs

---

# 34. A Complete Mini Project – Student File

Let's combine several concepts.

### Step 1 – Save Students

```python
with open("students.txt", "w") as file:

    for i in range(3):

        name = input("Enter student name: ")

        file.write(name + "\n")

print("Students saved successfully.")
```

### Step 2 – Display Students

```python
with open("students.txt", "r") as file:

    print("\nStudent List:")

    for name in file:
        print(name.strip())
```

### Concepts Used

```text
User Input
     ↓
Loop
     ↓
File Writing
     ↓
File Reading
     ↓
Loop
```

---

# 35. Another Mini Project – Simple Notes App

### Save a Note

```python
note = input("Enter your note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved.")
```

### Display Notes

```python
with open("notes.txt", "r") as file:

    print("\nYour Notes:")

    for note in file:
        print("-", note.strip())
```

This is a simple example of how real applications can store information permanently.

---

# 36. Important `open()` Pattern

Students should remember this pattern:

### Reading

```python
with open("file.txt", "r") as file:
    content = file.read()
```

### Writing

```python
with open("file.txt", "w") as file:
    file.write("Hello")
```

### Appending

```python
with open("file.txt", "a") as file:
    file.write("Hello\n")
```

---

# 37. Common Mistakes

### Mistake 1 – Forgetting the mode

```python
open("students.txt")
```

Although Python defaults to reading, it is better for beginners to explicitly specify the mode:

```python
open("students.txt", "r")
```

---

### Mistake 2 – Using `w` When You Want to Add Data

This:

```python
with open("students.txt", "w") as file:
    file.write("New Student\n")
```

will overwrite existing contents.

Use:

```python
with open("students.txt", "a") as file:
    file.write("New Student\n")
```

when you want to add data.

---

### Mistake 3 – Forgetting `\n`

This:

```python
file.write("Ahmed")
file.write("Sara")
```

produces:

```text
AhmedSara
```

Instead:

```python
file.write("Ahmed\n")
file.write("Sara\n")
```

produces:

```text
Ahmed
Sara
```

---

# 38. File Handling – Quick Reference

| Task                 | Code                      |
| -------------------- | ------------------------- |
| Open for reading     | `open("file.txt", "r")`   |
| Open for writing     | `open("file.txt", "w")`   |
| Open for appending   | `open("file.txt", "a")`   |
| Create new file      | `open("file.txt", "x")`   |
| Read entire file     | `file.read()`             |
| Read one line        | `file.readline()`         |
| Write data           | `file.write()`            |
| Close file           | `file.close()`            |
| Recommended approach | `with open(...) as file:` |

---

# 39. `read()` vs `readline()` vs Loop

| Method             | Purpose           |
| ------------------ | ----------------- |
| `read()`           | Read entire file  |
| `readline()`       | Read one line     |
| `for line in file` | Read line by line |

### Example

```python
with open("students.txt", "r") as file:

    for line in file:
        print(line.strip())
```

For beginners, **reading line by line with a `for` loop** is an especially useful pattern to practice.

---

# 40. Practice Programs

### Exercise 1 – Create a File

Create a file called `welcome.txt` and write:

```text
Welcome to Python Programming
I am learning File Handling.
```

---

### Exercise 2 – Save Names

Ask the user to enter the names of **5 students** and save them to `students.txt`.

---

### Exercise 3 – Read Names

Read `students.txt` and display all student names using a loop.

---

### Exercise 4 – Add a Student

Ask the user for a new student's name and append it to `students.txt`.

---

### Exercise 5 – Count Students

Read `students.txt` and display the number of students stored in the file.

---

### Exercise 6 – Search Student

Ask the user for a student name and check whether that student exists in `students.txt`.

---

# ⭐ Challenge – Simple Contact Book

Create a program that stores contact information in a text file.

For example:

```text
Ahmed - 9876543210
Sara - 9123456780
Rahul - 9988776655
```

The program should:

1. Ask for a name and phone number.
2. Save the contact using **append mode**.
3. Display all contacts from the file.
4. Ask for a name and search for that contact.

### Concepts to use

```text
Functions
    +
File Handling
    +
Loops
    +
if-else
    +
Strings
```

---

# 🎯 Summary

In this lesson, you learned:

* What File Handling is.
* Why files are needed.
* `open()`
* File modes: `r`, `w`, `a`, `x`
* `read()`
* `readline()`
* Reading files using loops
* `write()`
* `\n`
* Appending data
* `with open()`
* Basic error handling
* Practical file-based programs

## ⭐ Remember

```text
r → Read
w → Write / Overwrite
a → Append
x → Create
```

And the most recommended pattern is:

```python
with open("file.txt", "r") as file:
    # work with the file
```

> **File Handling allows Python programs to save data permanently and retrieve it later.**
