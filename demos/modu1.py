import calculator
import factorial

n = int(input("Enter a number: "))
fact = factorial.calc_fact(n)
print("Factorial of",n,"=",fact)

sum = calculator.add(10,5)
print("Sum =", sum)

diff = calculator.subtract(5,2)
print("Difference =", diff)

product = calculator.multiply(5,2)
print("Product =", product)

