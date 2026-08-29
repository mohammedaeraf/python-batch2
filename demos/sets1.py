fruits = {"Apple", "Mango", "Banana", "Kiwi"}
print(fruits)

fruits.add("Watermelon")

fruits_sorted = sorted(fruits)
print(fruits_sorted)

for fruit in fruits:
    print(fruit)

search_fruit = "Kiwi"
if search_fruit in fruits:
    print(search_fruit, "is present in the set")
else:
    print(search_fruit, "is not present in the set")

numbers = {10,20,30,20,10,40,30}
print(numbers)


# observant