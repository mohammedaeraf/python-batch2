# Advanced Python Programming – MCQ Answer Key with Questions

## Question 1

What is the output of the following code?

```
x = 12if x > 10:    print("A")else:    print("B")
```

1. A
2. Both A and B
3. B
4. No output

Correct Answer: Option 1 — A

## Question 2

What is the output of this code?

```
for i in range(1, 5):    print(i, end=" ")
```

1. 1 2 3 4 5
2. 2 3 4 5
3. 0 1 2 3 4
4. 1 2 3 4

Correct Answer: Option 4 — 1 2 3 4

## Question 3

What is the output?

```
numbers = [10, 20, 30]numbers.append(40)print(len(numbers))
```

1. 4
2. 5
3. 40
4. 3

Correct Answer: Option 1 — 4

## Question 4

What does the expression `numbers[1:4]` return when `numbers = [5, 10, 15, 20, 25]`?

1. [5, 10, 15, 20]
2. [10, 15, 20]
3. [15, 20]
4. [10, 15, 20, 25]

Correct Answer: Option 2 — [10, 15, 20]

## Question 5

What is the output?

```
text = "Python"print(text.upper())
```

1. pYTHON
2. PYTHON
3. Python
4. python

Correct Answer: Option 2 — PYTHON

## Question 6

What is the output?

```
def add(a, b):    return a + bprint(add(3, 4))
```

1. 34
2. 7
3. None
4. a + b

Correct Answer: Option 2 — 7

## Question 7

What is the result of this function call?

```
def calculate(a, b=5):    return a * bcalculate(3)
```

1. 15
2. 3
3. Error because b is missing
4. 8

Correct Answer: Option 1 — 15

## Question 8

Which statement about Python tuples is correct?

1. Tuples use curly braces by default
2. Tuples are immutable sequences
3. Tuples are mutable sequences
4. Tuples cannot contain strings

Correct Answer: Option 2 — Tuples are immutable sequences

## Question 9

What is the output?

```
student = {"name": "Sara", "marks": 90}print(student["marks"])
```

1. Sara
2. 90
3. name
4. marks

Correct Answer: Option 2 — 90

## Question 10

What is the output of the following code?

```
numbers = [10, 20, 30, 40, 50, 60]print(numbers[-3:])
```

1. [10, 20, 30]
2. [30, 40, 50]
3. [40, 50, 60]
4. [50, 60]

Correct Answer: Option 3 — [40, 50, 60]

## Question 11

Which method returns the key-value pairs of a dictionary for iteration?

1. `pairs()`
2. `values()`
3. `keys()`
4. `items()`

Correct Answer: Option 4 — `items()`

## Question 12

What is the output of the following code?

```
set1 = {1, 2, 3, 4}set2 = {3, 4, 5, 6}print(set1.intersection(set2))
```

1. {1,2}
2. {3,4}
3. {5,6}
4. {1,2,3,4,5,6}

Correct Answer: Option 2 — {3,4}

## Question 13

Which exception is typically raised by `int("hello")`?

1. IndexError
2. KeyError
3. TypeError
4. ValueError

Correct Answer: Option 4 — ValueError

## Question 14

In a `try-except-else-finally` structure, when does the `finally` block execute?

1. Only when no exception occurs
2. Whether an exception occurs or not, in normal control flow
3. Only when an exception occurs
4. Only when a return statement appears

Correct Answer: Option 2 — Whether an exception occurs or not, in normal control flow

## Question 15

Which statement imports Python's math module using the alias `m`?

1. `import m from math`
2. `math import as m`
3. `import math as m`
4. `include math as m`

Correct Answer: Option 3 — `import math as m`

## Question 16

In a Python class, what is the main purpose of the `__init__()` method?

1. To destroy an object
2. To import external modules
3. To initialize an object's attributes when it is created
4. To repeat a loop

Correct Answer: Option 3 — To initialize an object's attributes when it is created

## Question 17

In a Python instance method, what does `self` normally refer to?

1. A global variable
2. The parent class
3. The current object instance
4. The Python interpreter

Correct Answer: Option 3 — The current object instance

## Question 18

Which NumPy function calculates the arithmetic mean of an array named `marks`?

1. `np.mean(marks)`
2. `np.sort(marks)`
3. `np.total(marks)`
4. `np.max(marks)`

Correct Answer: Option 1 — `np.mean(marks)`

## Question 19

After running `df = pd.read_csv("sales.csv")`, which Pandas command displays the first five rows by default?

1. `df.describe()`
2. `df.info()`
3. `df.head()`
4. `df.tail()`

Correct Answer: Option 3 — `df.head()`

## Question 20

Which chart is generally most suitable for showing how sales change month by month?

1. Box plot
2. Pie chart
3. Line chart
4. Scatter plot

Correct Answer: Option 3 — Line chart
