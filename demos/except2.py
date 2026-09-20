try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = x/y

except ValueError:
    print("Please enter whole numbers only")

except ZeroDivisionError:
    print("Second number should not be zero(0)")

# executes when there is no error or exception
else: 
    print("Result =", result)

# executes wheter or not there is an error
finally: 
    print("Clearing up resources...")