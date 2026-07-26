# Python Programming – Lesson 0 Notes

## Topic: Installing Python and Setting Up Visual Studio Code (VS Code)

---

# Learning Objectives

By the end of this lesson, you will be able to:

- Download and install Python.
- Verify that Python is installed correctly.
- Install Visual Studio Code (VS Code).
- Install the Python extension in VS Code.
- Create and run your first Python program.

---

# What is Python?

Python is a simple, powerful, and beginner-friendly programming language used for:

- Web Development
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Data Science
- Automation
- Desktop Applications
- Cyber Security

Before writing Python programs, we need to install Python and a code editor.

---

# Step 1: Download Python

Visit the official Python website:

**https://www.python.org/downloads/**

Download the latest stable version for your operating system.

---

# Step 2: Install Python

Double-click the downloaded installer.

### Important

✔ Check the box:

```
Add Python to PATH
```

before clicking **Install Now**.

This allows Python to be used from the Command Prompt and VS Code.

Wait until the installation completes.

---

# Step 3: Verify the Installation

Open **Command Prompt**.

Type:

```bash
python --version
```

or

```bash
python -V
```

Example Output

```text
Python 3.13.7
```

You can also check pip:

```bash
pip --version
```

Example Output

```text
pip 25.x.x
```

---

# Step 4: Install Visual Studio Code

Download VS Code from:

**https://code.visualstudio.com/**

Run the installer and complete the installation.

---

# Step 5: Open VS Code

Launch Visual Studio Code.

You should see the Welcome Screen.

---

# Step 6: Install the Python Extension

Click the **Extensions** icon on the left side.

Search for:

```
Python
```

Install the extension published by **Microsoft**.

This extension provides:

- Syntax highlighting
- Auto-completion
- Error detection
- Debugging
- Run support

---

# Step 7: Create a Project Folder

Create a folder on your computer.

Example:

```
PythonCourse
```

Open this folder in VS Code.

**File → Open Folder**

---

# Step 8: Create Your First Python File

Click

```
New File
```

Name the file:

```
hello.py
```

Python files always use the **.py** extension.

---

# Step 9: Write Your First Program

```python
print("Hello World")
```

Save the file by pressing:

```
Ctrl + S
```

---

# Step 10: Run the Program

There are several ways to run a Python program in VS Code.

### Method 1

Click the

```
▶ Run
```

button in the top-right corner.

---

### Method 2

Right-click anywhere inside the editor.

Choose

```
Run Python File
```

---

### Method 3

Open the integrated terminal.

Menu:

```
Terminal → New Terminal
```

Run:

```bash
python hello.py
```

Output:

```text
Hello World
```

---

# Selecting the Python Interpreter

If VS Code asks you to select an interpreter:

Press

```
Ctrl + Shift + P
```

Search for:

```
Python: Select Interpreter
```

Choose the latest installed Python version.

Example:

```
Python 3.13
```

---

# Useful Keyboard Shortcuts

| Shortcut         | Purpose         |
| ---------------- | --------------- |
| Ctrl + S         | Save File       |
| Ctrl + C         | Copy            |
| Ctrl + V         | Paste           |
| Ctrl + Z         | Undo            |
| Ctrl + /         | Comment Code    |
| Ctrl + Shift + P | Command Palette |
| Ctrl + `         | Open Terminal   |

---

# Folder Structure

Example

```
PythonCourse
│
├── hello.py
├── calculator.py
├── marks.py
└── students.py
```

Keeping all programs in one folder makes them easy to organize.

---

# Common Errors

## 1. Python is not recognized

Error

```text
'python' is not recognized...
```

Solution:

- Reinstall Python.
- Make sure **Add Python to PATH** is checked.

---

## 2. File Saved Without .py Extension

Incorrect

```
hello
```

Correct

```
hello.py
```

---

## 3. Wrong Interpreter Selected

Solution:

Select the correct Python interpreter from:

```
Python: Select Interpreter
```

---

## 4. Forgot to Save the File

Always save your file before running it.

Shortcut:

```
Ctrl + S
```

---

# Your First Program

```python
print("Welcome to Python Programming!")
print("My first Python program")
```

Output

```text
Welcome to Python Programming!
My first Python program
```

---

# Practice Exercises

1. Install Python.
2. Install VS Code.
3. Install the Python extension.
4. Create a folder named **PythonCourse**.
5. Create a file named **hello.py**.
6. Display your name using `print()`.
7. Display your city.
8. Display three lines of text.

---

# Summary

In this lesson, you learned:

- How to install Python
- How to verify the installation
- How to install VS Code
- How to install the Python extension
- How to create a Python file
- How to run a Python program
- How to use the integrated terminal

---

# Key Takeaway

> **A properly configured development environment is the first step toward becoming a successful Python programmer. Once Python and VS Code are set up, you're ready to start building programs with confidence.**
