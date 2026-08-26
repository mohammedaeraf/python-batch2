# 🐍 Python Lesson Notes: Introduction to OOP

## 1. Learning Objectives

By the end of this lesson, students will be able to:

- Understand the basic idea of **Object-Oriented Programming (OOP)**.
- Understand **Classes** and **Objects**.
- Create a simple class.
- Create objects from a class.
- Define attributes and methods.
- Understand `self`.
- Use the `__init__()` constructor.
- Create simple real-world programs using OOP.

---

# 2. What is OOP?

**OOP** stands for **Object-Oriented Programming**.

It is a programming approach where we organize programs around **objects**.

An object can represent something from the real world.

Examples:

```text
Student
Car
Bank Account
Employee
Mobile Phone
Product
Book
```

Each object can have:

- **Properties / Data**
- **Behaviours / Actions**

For example, a **Student** may have:

```text
Properties:
Name
Age
Marks

Behaviours:
Study()
AttendClass()
DisplayDetails()
```

---

# 3. Why Do We Need OOP?

Consider a program storing information about students.

Without OOP, we might write:

```python
student1_name = "Ahmed"
student1_age = 20
student1_marks = 85

student2_name = "Sara"
student2_age = 21
student2_marks = 92
```

As the program grows, managing the data becomes difficult.

With OOP, we can create a **Student class** and then create many Student objects.

```text
Student Class
      ↓
 ┌────┴────┐
 ↓         ↓
Ahmed     Sara
Object    Object
```

---

# 4. Class and Object

These are the two most important concepts in introductory OOP.

### Class

A **class** is a blueprint or template for creating objects.

### Object

An **object** is an actual instance created from a class.

### Real-world analogy

Think about a house.

```text
House Blueprint → Class
Actual House    → Object
```

The blueprint describes what a house should contain.

The actual houses are created using that blueprint.

---

# 5. Creating a Simple Class

Python uses the `class` keyword.

```python
class Student:
    pass
```

Here:

```text
class → keyword
Student → class name
```

`pass` means:

> "There is nothing to do here yet."

---

# 6. Creating an Object

We can create an object from the class:

```python
class Student:
    pass


student1 = Student()

print(student1)
```

`student1` is an **object** of the `Student` class.

---

# 7. Multiple Objects

We can create many objects from the same class.

```python
class Student:
    pass


student1 = Student()
student2 = Student()
student3 = Student()
```

All three objects belong to the `Student` class.

```text
             Student
              Class
                ↓
      ┌─────────┼─────────┐
      ↓         ↓         ↓
  student1  student2  student3
```

---

# 8. Attributes

An **attribute** is data associated with an object.

For example:

```text
Student
 ├── name
 ├── age
 └── marks
```

We can create attributes:

```python
class Student:
    pass


student1 = Student()

student1.name = "Ahmed"
student1.age = 20
student1.marks = 85

print(student1.name)
print(student1.age)
print(student1.marks)
```

Output:

```text
Ahmed
20
85
```

---

# 9. The Problem with the Previous Approach

We can create attributes manually:

```python
student1.name = "Ahmed"
student1.age = 20
student1.marks = 85
```

But imagine creating 100 students.

We would have to repeatedly assign these values.

Python provides a better way using:

```python
__init__()
```

---

# 10. The `__init__()` Method ⭐

`__init__()` is a special method that runs automatically when an object is created.

Example:

```python
class Student:

    def __init__(self):
        print("Student object created")


student1 = Student()
```

Output:

```text
Student object created
```

When we write:

```python
student1 = Student()
```

Python automatically calls:

```python
__init__()
```

---

# 11. Passing Data to `__init__()`

We can pass information when creating the object.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ahmed", 20)

print(student1.name)
print(student1.age)
```

Output:

```text
Ahmed
20
```

---

# 12. Understanding `self` ⭐

`self` refers to the **current object**.

Consider:

```python
self.name = name
```

The right side:

```python
name
```

is the value passed to the constructor.

The left side:

```python
self.name
```

is the attribute belonging to the current object.

For example:

```python
student1 = Student("Ahmed", 20)
```

Inside the object:

```text
self.name → Ahmed
self.age  → 20
```

---

# 13. Creating Multiple Students

Now the same class can create multiple students.

```python
class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks


student1 = Student("Ahmed", 20, 85)
student2 = Student("Sara", 21, 92)

print(student1.name)
print(student1.marks)

print(student2.name)
print(student2.marks)
```

Output:

```text
Ahmed
85
Sara
92
```

Each object has its **own data**.

---

# 14. Class vs Object

Consider:

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
```

This defines the **class**.

Then:

```python
student1 = Student("Ahmed", 85)
student2 = Student("Sara", 92)
```

These are **objects**.

```text
Class
Student
   │
   ├── student1
   │     name = Ahmed
   │     marks = 85
   │
   └── student2
         name = Sara
         marks = 92
```

---

# 15. Methods

A **method** is a function defined inside a class.

For example:

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name =", self.name)
        print("Marks =", self.marks)
```

Now create an object:

```python
student1 = Student("Ahmed", 85)

student1.display()
```

Output:

```text
Name = Ahmed
Marks = 85
```

---

# 16. Method vs Function

You have already learned functions.

### Function

```python
def add(a, b):
    return a + b
```

It exists independently.

### Method

A method is a function that belongs to a class.

```python
class Student:

    def display(self):
        print("Student Details")
```

We call it using an object:

```python
student1.display()
```

### Simple Rule

> **Function → Independent**
> **Method → Belongs to a class/object**

---

# 17. Method with `self`

Methods usually need `self` as their first parameter.

```python
class Student:

    def display(self):
        print("Student Details")
```

When we call:

```python
student1.display()
```

Python automatically passes the current object as `self`.

---

# 18. Method with Additional Parameters

A method can also accept other parameters.

```python
class Calculator:

    def add(self, a, b):
        return a + b


calculator = Calculator()

result = calculator.add(10, 20)

print(result)
```

Output:

```text
30
```

Notice:

```python
def add(self, a, b):
```

`self` refers to the object, while `a` and `b` are normal parameters.

---

# 19. Practical Example – Student Class

Let's create a more complete example.

```python
class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display(self):

        print("Name =", self.name)
        print("Marks =", self.marks)

    def check_result(self):

        if self.marks >= 40:
            print("Result = Pass")
        else:
            print("Result = Fail")


student1 = Student("Ahmed", 85)

student1.display()
student1.check_result()
```

Output:

```text
Name = Ahmed
Marks = 85
Result = Pass
```

---

# 20. Another Practical Example – Car

A Car can have:

### Attributes

```text
Brand
Model
Year
```

### Behaviours

```text
Start
Stop
Display Details
```

Python:

```python
class Car:

    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year

    def display(self):

        print("Brand =", self.brand)
        print("Model =", self.model)
        print("Year =", self.year)


car1 = Car("Toyota", "Corolla", 2025)

car1.display()
```

Output:

```text
Brand = Toyota
Model = Corolla
Year = 2025
```

---

# 21. Multiple Car Objects

```python
class Car:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def display(self):

        print(self.brand, self.model)


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "City")
car3 = Car("Hyundai", "Creta")

car1.display()
car2.display()
car3.display()
```

Output:

```text
Toyota Corolla
Honda City
Hyundai Creta
```

One class can create many objects.

---

# 22. Practical Example – Bank Account

A bank account can have:

### Attributes

```text
Account Number
Account Holder
Balance
```

### Behaviours

```text
Deposit
Withdraw
Display Balance
```

Example:

```python
class BankAccount:

    def __init__(self, account_number, holder, balance):

        self.account_number = account_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):

        self.balance = self.balance + amount

    def display_balance(self):

        print("Balance =", self.balance)


account1 = BankAccount(101, "Ahmed", 5000)

account1.deposit(2000)

account1.display_balance()
```

Output:

```text
Balance = 7000
```

---

# 23. Why OOP is Useful

Imagine a large application containing:

```text
Students
Teachers
Courses
Employees
Products
Orders
Customers
```

Instead of keeping unrelated variables and functions everywhere, we can organize the program using classes.

```text
Application
    │
    ├── Student Class
    ├── Teacher Class
    ├── Course Class
    ├── Product Class
    └── Customer Class
```

This makes large programs easier to:

- Organize
- Understand
- Maintain
- Extend
- Reuse

---

# 24. OOP and Real-World Objects

A useful way to understand OOP is to think about real-world objects.

| Real-World Object | Possible Attributes      | Possible Methods              |
| ----------------- | ------------------------ | ----------------------------- |
| Student           | name, age, marks         | study(), display()            |
| Car               | brand, model, speed      | start(), stop()               |
| Bank Account      | number, holder, balance  | deposit(), withdraw()         |
| Product           | name, price, quantity    | display(), calculate_total()  |
| Employee          | name, salary, department | display(), calculate_salary() |

---

# 25. A Simple OOP Structure

Students should remember this basic pattern:

```python
class ClassName:

    def __init__(self, value1, value2):

        self.value1 = value1
        self.value2 = value2

    def method(self):

        # perform some task
        pass


object1 = ClassName(value1, value2)

object1.method()
```

---

# 26. Important OOP Terms

| Term          | Meaning                       |
| ------------- | ----------------------------- |
| **Class**     | Blueprint/template            |
| **Object**    | Instance of a class           |
| **Attribute** | Data belonging to an object   |
| **Method**    | Function belonging to a class |
| `self`        | Refers to the current object  |
| `__init__()`  | Initializes an object         |

---

# 27. Class and Object Analogy

Think about a **Student ID Card**.

The design/template might contain:

```text
Name
Photo
ID
Course
```

The template is similar to a:

> **Class**

An actual ID card for Ahmed is similar to an:

> **Object**

Another ID card for Sara is another:

> **Object**

```text
              Student Class
                   │
          ┌────────┴────────┐
          ↓                 ↓
      Ahmed Object       Sara Object
       Name: Ahmed        Name: Sara
       ID: 101            ID: 102
```

---

# 28. Practice Program – Employee

Create an `Employee` class with:

### Attributes

- Name
- Department
- Salary

### Method

`display()`

Expected output:

```text
Name = Ahmed
Department = IT
Salary = 45000
```

---

# 29. Practice Program – Rectangle

Create a `Rectangle` class with:

### Attributes

- Length
- Breadth

### Methods

- `calculate_area()`
- `calculate_perimeter()`

Formulas:

```text
Area = Length × Breadth

Perimeter = 2 × (Length + Breadth)
```

Example:

```text
Length = 10
Breadth = 5

Area = 50
Perimeter = 30
```

---

# 30. Practice Program – Product

Create a `Product` class with:

- Name
- Price
- Quantity

Create a method:

```text
calculate_total()
```

Formula:

```text
Total = Price × Quantity
```

Example:

```text
Product = Keyboard
Price = 1500
Quantity = 2

Total = 3000
```

---

# ⭐ Challenge – Student Result System

Create a `Student` class containing:

### Attributes

```text
name
english
maths
science
```

### Methods

```text
calculate_total()
calculate_average()
display_result()
```

The program should create a Student object and display:

```text
Student Name = Ahmed
Total = 240
Average = 80.0
Result = Pass
```

This is a good challenge because it combines concepts students have already learned:

```text
Class
   ↓
Object
   ↓
Attributes
   ↓
Methods
   ↓
if-else
   ↓
Calculations
```

---

# 🎯 Key Takeaways

Remember these five concepts first:

### 1. Class

A blueprint.

```python
class Student:
    pass
```

### 2. Object

An instance of a class.

```python
student1 = Student()
```

### 3. Attribute

Data belonging to an object.

```python
self.name = name
```

### 4. Method

A function inside a class.

```python
def display(self):
    print(self.name)
```

### 5. `__init__()`

Used to initialize object data.

```python
def __init__(self, name):
    self.name = name
```

---

## 🧠 One-Minute Revision

```text
             CLASS
       (Blueprint / Template)
                ↓
             OBJECT
       (Actual Instance)
                ↓
      ┌─────────┴─────────┐
      ↓                   ↓
 ATTRIBUTES             METHODS
   (Data)              (Actions)
      ↓                   ↓
 self.name            display()
 self.age             calculate()
 self.marks           check_result()
```

> **OOP is a way of organizing programs around objects that combine data (attributes) and behaviour (methods).**

For your students, I would **not introduce inheritance, polymorphism, encapsulation, decorators, class methods, or static methods in this first OOP lesson**. The first goal should be to make **Class → Object → `__init__()` → `self` → Attributes → Methods** completely comfortable before moving to those topics.
