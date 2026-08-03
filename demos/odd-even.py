# Program to read a number and output if it's odd or even
# Odd Nos - 1,3,5,7...
# Even Nos - 2,4,6,8... (Numbers divisible by 2)

n = int(input("Enter a number: "))
n = 7
rem = n % 2
# print("Remainder =", rem)

if rem == 0:
    print(n, "is even")
else:
    print(n, "is odd")



