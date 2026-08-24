# 🧪 Lab Assignment 07 – Strings in Python

## 📘 Instructions

1. Write each program in a separate Python file.
2. Accept input from the user wherever required.
3. Use **Strings, loops, and conditional statements** wherever appropriate.
4. Display clear and meaningful output.
5. Test each program with different inputs.

---

## 1️⃣ Display Characters of a String

Write a Python program that accepts a word from the user and displays each character on a separate line using a loop.

### Sample Output

```text
Enter a word: Python

P
y
t
h
o
n
```

**Hint:** Use a `for` loop to iterate through the String.

---

## 2️⃣ Count Vowels in a String

Write a program that accepts a word or sentence and counts the number of **vowels**.

Consider both uppercase and lowercase vowels.

### Sample Output

```text
Enter text: Education

Number of Vowels = 5
```

**Hint:**

```python
if letter in "aeiouAEIOU":
```

Use a variable such as `count` to keep track of the number of vowels.

---

## 3️⃣ Count a Particular Character

Write a Python program that:

- Accepts a word or sentence.
- Accepts a character to search for.
- Displays how many times that character occurs.

### Sample Output

```text
Enter text: banana
Enter character to search: a

Occurrences of a = 3
```

**Hint:** Loop through the String and compare each character with the character entered by the user.

---

## 4️⃣ Reverse a String

Write a Python program that accepts a word and displays it in **reverse order**.

### Sample Output

```text
Enter a word: Python

Original = Python
Reverse = nohtyP
```

**Hint:** Try solving it using a loop:

```python
reverse = ""
```

Then build the reversed String one character at a time.

**Challenge:** After completing the loop-based solution, try using String slicing.

---

## 5️⃣ Palindrome Checker

A **palindrome** is a word that reads the same forwards and backwards.

Examples:

```text
madam
level
radar
civic
```

Write a program that accepts a word and checks whether it is a palindrome.

### Sample Output 1

```text
Enter a word: madam

madam is a Palindrome.
```

### Sample Output 2

```text
Enter a word: python

python is not a Palindrome.
```

**Hint:**

First reverse the word and then compare:

```text
Original Word == Reversed Word
```

Use an `if-else` statement to display the result.

---

# ⭐ Bonus Question – Character Analyzer

Write a Python program that accepts a sentence and counts the number of:

- Uppercase letters
- Lowercase letters
- Digits
- Spaces

### Sample Input

```text
Enter text: Python Class 2026
```

### Sample Output

```text
Uppercase Letters = 2
Lowercase Letters = 9
Digits = 4
Spaces = 2
```

**Hint:** You can use:

```python
letter.isupper()
letter.islower()
letter.isdigit()
letter.isspace()
```

---

## 🎯 Learning Outcomes

After completing this lab, students should be able to:

- Iterate through Strings using loops.
- Search and count characters.
- Combine Strings with conditional statements.
- Reverse Strings.
- Compare Strings.
- Identify palindromes.
- Use String methods such as `isupper()`, `islower()`, `isdigit()`, and `isspace()`.
