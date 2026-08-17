# Create a list of student names
students = ["Ali","Arif","Sunita","Joseph"]
print(students)  # Output: ['Ali', 'Arif', 'Sunita', 'Joseph']
print(students[3])  # Access the 4th element (index 3) -> Joseph

# Create a list of fruits
fruits = ["Apple","Banana","Pineapple"]
fruits[0] = "Orange"  # Replace the first element with "Orange"

fruits.append("Watermelon")  # Add "Watermelon" to the end of the list

last_fruit = fruits.pop()  # Remove and return the last element ("Watermelon")

print("Last fruit ->", last_fruit)

fruits.insert(1,"Mango")  # Insert "Mango" at index 1 (between first and second elements)
print(fruits)  # Output: ['Orange', 'Mango', 'Banana', 'Pineapple']

# Create a list of numbers
numbers = [10,5,7,20,18]
print(len(numbers))  # len() returns the number of elements in the list -> 5

total = 0
# Loop through each number in the list
for n in numbers:
    # Check if the number is even (divisible by 2)
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n,"is odd")

# Calculate the sum of all numbers in the list using the sum() function
total = sum(numbers)
print("Total value =", total)  # Output: 60

# Find and print the maximum number in the list
max_no = max(numbers)
print("Max number", max_no)  # Output: 20
