# Factorial of 5 => 1 * 2 * 3 * 4 * 5 = 5 * 4 * 3 * 2 * 1

# 4 x 5 = 5 x 4

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i
    # print("fact now = ", fact)

print("Factorial of",n,"=",fact)