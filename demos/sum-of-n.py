# Sum of 1st 5 digits
# sum = 1 + 2 + 3 + 4 + 5

n = int(input("Enter a number: "))
i = 1
total = 0
while i <=n :
    total = total + i
    i = i + 1

print("Total =", total)
