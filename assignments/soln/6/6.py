# ============================================================
# Lab Assignment 06 – Lists in Python
# Solutions
# ============================================================


# ============================================================
# 1. Display All Elements Using a Loop
# ============================================================

students = ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"]

print("Question 1")
print("Student Names:")

for student in students:
    print(student)


# ============================================================
# 2. Calculate Total and Average Marks
# ============================================================

marks = [75, 82, 91, 68, 84]

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("\nQuestion 2")
print("Total Marks =", total)
print("Average Marks =", average)


# ============================================================
# 3. Count Even and Odd Numbers
# ============================================================

numbers = [12, 17, 20, 25, 32, 41, 50, 63, 70, 81]

even_count = 0
odd_count = 0

for number in numbers:

    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("\nQuestion 3")
print("Even Numbers =", even_count)
print("Odd Numbers =", odd_count)


# ============================================================
# 4. Find the Largest and Smallest Number
# ============================================================

numbers = [45, 12, 78, 34, 91, 23, 67]

largest = max(numbers)
smallest = min(numbers)

print("\nQuestion 4")
print("Largest Number =", largest)
print("Smallest Number =", smallest)


# ============================================================
# 4 - Challenge
# Find Largest and Smallest Without max() and min()
# ============================================================

numbers = [45, 12, 78, 34, 91, 23, 67]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("\nQuestion 4 - Challenge")
print("Largest Number =", largest)
print("Smallest Number =", smallest)


# ============================================================
# 5. Search for an Item in a List
# ============================================================

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

search_fruit = input("\nEnter Fruit: ")

if search_fruit in fruits:
    print(search_fruit, "is available.")
else:
    print(search_fruit, "is not available.")


# ============================================================
# Bonus – Separate Even and Odd Numbers
# ============================================================

numbers = [11, 22, 35, 40, 53, 64, 77, 80]

even_numbers = []
odd_numbers = []

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("\nBonus Question")
print("Original List =", numbers)
print("Even Numbers =", even_numbers)
print("Odd Numbers =", odd_numbers)