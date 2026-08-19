students = ["Ahmed", "Sara", "Rahul", "Fatima", "Zeeshan"]

for student in students:
    print(student)


marks = [75, 82, 91, 68, 84]
total = 0
for mark in marks:
    total = total + mark

average = total/len(marks)


numbers = [45, 12, 78, 34, 91, 120, 67]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Largest =",largest)
print("Smallest =",smallest)

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
entered_fruit = input("Enter a fruit: ")

if entered_fruit in fruits:
    print(entered_fruit,"is available")
else:
    print(entered_fruit,"is not available")
