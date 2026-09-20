# Try the input conversion and division so specific errors can be handled below.
try:
    # int() raises ValueError when either input is not a whole number.
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    # Division raises ZeroDivisionError when the second number is zero.
    result = x/y

# Handle invalid text separately from a division-by-zero error.
except ValueError:
    print("Please enter whole numbers only")

except ZeroDivisionError:
    print("Second number should not be zero(0)")

# The else block runs only when the try block completes successfully.
else: 
    print("Result =", result)

# The finally block runs whether an exception occurred or not.
finally: 
    print("Clearing up resources...")