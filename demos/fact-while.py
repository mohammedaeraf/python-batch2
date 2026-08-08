# Factorial of 5 => 1 * 2 * 3 * 4 * 5

n = int(input("Enter a number: "))
fact = 1

i = 1
while i <= n:
    fact = fact * i
    # print("fact now = ", fact)
    i = i + 1

print("Factorial of",n,"=",fact)
