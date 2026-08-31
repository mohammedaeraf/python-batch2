# JSON -> JavaScript Object Notation
# Dictionaries are similar to JSON objects with key-value pairs

# Example 1: Student dictionary containing personal and academic information
student1 = {
    "name":"Mohammed Mubin",
    "age": 23,
    "course": "Web Design",
    "marks": 94
}

# Example 2: Product dictionary with details about an item (price, description, category)
product1 = {
    "title":"HP Pavillion Laptop",
    "price": 75000,
    "discounted_price":65000,
    "description": "15.6 inch screen, i5 Core 12 Gen",
    "category": "Laptops"
}

# Alternative representation of product data as a tuple (immutable, ordered sequence)
product_tuple = ("HP Pavillion Laptop", 75000, 65000, "15.6 inch screen, i5 Core 12 Gen", "Laptops")

# RGB color values stored as a tuple (Red, Green, Blue)
color = (200,90,190)

# Coordinate point stored as a tuple (x, y)
point = (20,30)

# Access dictionary value using .get() method (returns None if key doesn't exist)
print(product1.get("title"))

# Access dictionary value using bracket notation (raises error if key doesn't exist)
print(product1["title"])

# Print all keys in the dictionary
print(product1.keys())

# Iterate through all values in the dictionary
for val in product1.values():
    print(val, end="; ")

# Iterate through all key-value pairs in the dictionary
for key,value in product1.items():
    print(key, "=>", value, end="; ")

# Loop Through a List of Students 
students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Rahul", "marks": 78}
]

for student in students:
    # for each student, print its name and marks
    print(student["name"], "-", student["marks"])


