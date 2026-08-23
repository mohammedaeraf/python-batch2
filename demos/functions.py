# Functions - used to create reusable code
# System Defined Functions - print(), input(), int(), upper()
# User Defined Functions - Functions that you define

def greet():
    # The indented block is the code that runs whenever greet() is called.
    print("Welcome to Python Course!")
greet() # Call the function to run its code.


# Function with Params
def add(a, b):
    # a and b receive the values supplied by the caller.
    sum = a + b
    print("Sum of", a, "and",b,"is", sum)

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
add(a,b)  # The variables a and b are arguments for this call.
add(30,40)  # Literal values can also be passed as arguments.


# Function with return statement
def rect_area(l,b):
    area = l * b
    # return sends the calculated value back to the code that called the function.
    return area

area = rect_area(6,4) # Store the returned area (6 * 4 = 24).
print("Area of rectangle =",area)


# Functions that contain loops
def mult_table(n):
    print("******** Table of",n,"********")
    for i in range(1,11):
        ans = n * i
        print(n, "x", i, "=", ans)
    print("-----------------------------")
    print()

mult_table(5)
mult_table(7)
