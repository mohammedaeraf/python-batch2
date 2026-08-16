students = ["Ali","Arif","Sunita","Joseph"]
# print(students)
print(students[3])

fruits = ["Apple","Banana","Pineapple"]
fruits[0] = "Orange"

fruits.append("Watermelon") # insert an element at the end

last_fruit = fruits.pop() # remove an element from the end

print("Last fruit ->", last_fruit)

fruits.insert(1,"Mango") # insert an element at the specified position
print(fruits)

numbers = [10,5,7,20,18]
print(len(numbers))  # len() is used to print the number of elements

total = 0
# for-in loop
for n in numbers:
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n,"is odd")
    # total = total + n # total = 35

total = sum(numbers)
print("Total value =", total)

max_no = max(numbers)
print("Max number", max_no)
