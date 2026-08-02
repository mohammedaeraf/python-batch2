units = int(input("Enter the units consumed: "))

slab1_rate = 5
slab2_rate = 7
slab3_rate = 10

total_bill = 0

if units <= 100:
    total_bill = units * slab1_rate
elif units <= 200:
    total_bill = (100 * slab1_rate) + ((units-100) * slab2_rate) 

print("-------Electricity Bill for July 2026-------")
print("Your units consumed:", units)
print("Your total bill for the month is Rs", total_bill)

