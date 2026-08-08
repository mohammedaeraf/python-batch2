# Factorial of 5 => 5 * 4 * 3 * 2 * 1

n = int(input("Enter a number: "))
fact = 1

for i in range(n, 0, -1):
    fact = fact * i
    print("fact now = ", fact)

print("Factorial of",n,"=",fact)

# fact now = 5
# fact now = 20
# fact now = 60
# fact now = 120
# fact now = 120

# Winners are not the ones who try different things, 
# but they are the ones who try things differently