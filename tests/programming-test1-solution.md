# Advanced Python Programming Test Solutions

## Question 1: Student Marks Management

Write a Python program that accepts the student's name and marks in three subjects.

Your program should:

1. Accept the student's name.
2. Accept marks in three subjects.
3. Calculate the total marks.
4. Calculate the average marks.
5. Display the student's name, total marks, and average marks.
6. Display the result based on the following conditions:
   - Average marks greater than or equal to 90: Grade A
   - Average marks greater than or equal to 75: Grade B
   - Average marks greater than or equal to 60: Grade C
   - Average marks greater than or equal to 40: Grade D
   - Average marks below 40: Fail

**Sample Input:**

Student Name: Sara  
Subject 1 Marks: 85  
Subject 2 Marks: 90  
Subject 3 Marks: 80

**Sample Output:**

Student Name: Sara  
Total Marks: 255  
Average Marks: 85.0  
Grade: B

### Solution

```
name = input("Student Name: ")

mark1 = float(input("Subject 1 Marks: "))
mark2 = float(input("Subject 2 Marks: "))
mark3 = float(input("Subject 3 Marks: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 90:
grade = "A"
elif average >= 75:
grade = "B"
elif average >= 60:
grade = "C"
elif average >= 40:
grade = "D"
else:
grade = "Fail"

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
```

---
## Question 2: Product Inventory Management

Write a Python program to manage a list of products using a list of dictionaries.

Each product should contain the following details:

- Product ID
- Product Name
- Price
- Quantity

Your program should:

1. Store details of at least three products.
2. Display all products with their prices and quantities.
3. Calculate and display the total inventory value for each product using:

   Total Value = Price × Quantity

4. Calculate and display the total value of the entire inventory.
5. Display the name of the product with the highest price.

**Sample Data:**

Product 1: Laptop, Price: 50000, Quantity: 2  
Product 2: Mouse, Price: 500, Quantity: 10  
Product 3: Keyboard, Price: 1500, Quantity: 5

**Sample Output:**

Product: Laptop, Price: 50000, Quantity: 2, Total Value: 100000  
Product: Mouse, Price: 500, Quantity: 10, Total Value: 5000  
Product: Keyboard, Price: 1500, Quantity: 5, Total Value: 7500  

Total Inventory Value: 112500  
Most Expensive Product: Laptop

### Solution

```
products = [
    {"id": 1, "name": "Laptop", "price": 50000, "quantity": 2},
    {"id": 2, "name": "Mouse", "price": 500, "quantity": 10},
    {"id": 3, "name": "Keyboard", "price": 1500, "quantity": 5}
]

total_inventory_value = 0

most_expensive_product = products[0]

for product in products:
    total_value = product["price"] * product["quantity"]
    total_inventory_value += total_value

    print(
        f"Product: {product['name']}, "
        f"Price: {product['price']}, "
        f"Quantity: {product['quantity']}, "
        f"Total Value: {total_value}"
    )

    if product["price"] > most_expensive_product["price"]:
        most_expensive_product = product

print("\nTotal Inventory Value:", total_inventory_value)
print("Most Expensive Product:", most_expensive_product["name"])
```
