# Sum of 1st 4 digits
# sum = 1 + 2 + 3 + 4 
# input = 4
# output = 10

n = int(input("Enter a number: "))
total = 0
for i in range(1,n+1):
    total = total + i
    # print("total now =", total)

print("Sum of 1st",n,"numbers =", total)
