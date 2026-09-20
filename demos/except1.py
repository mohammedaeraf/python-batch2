# Part 1 - Square 
print("Program Part 1 \n----------------------")
try:
    # Convert the user's text input to an integer before doing arithmetic.
    n = int(input("Enter a number: "))
    square = n * n
    print("Square of",n,"=",square)
except:
    # int() raises an error when the input is not a valid whole number.
    print("Incorrect number entered..")

# Part 2 - Area of Rect
print("Program Part 2 \n----------------------")

# These fixed length and breadth values are used to calculate the rectangle's area.
l = 10
b = 5
area = l * b
print("Area =",area)