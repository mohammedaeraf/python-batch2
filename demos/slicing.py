# List Slicing
# Create a list of numbers to slice.
numbers = [10,20,30,40,50,60]

# Get items at indexes 1 through 3; the stop index is not included.
print(numbers[1:4])
# Get items at indexes 3 through 5.
print(numbers[3:6])

# Omit the stop index to slice from index 3 to the end.
print(numbers[3:])
# Omit the start index to slice from the beginning through index 2.
print(numbers[:3])
# Omit both indexes to make a copy of the whole list.
print(numbers[:])

# Use a negative index to get the last item.
print(numbers[-1])
# Slice from the fourth item from the end up to, but not including, the last item.
print(numbers[-4:-1])
# Slice from the fourth item from the end through the end.
print(numbers[-4:])
# Slice the last two items.
print(numbers[-2:])


# Use a step of 2 to select every other item.
print(numbers[0:6:2])
# The omitted start and stop indexes use the whole list.
print(numbers[::2])


# Use a step of -1 to reverse the list.
print(numbers[::-1]) 
# Move backward from index 4 down to, but not including, index 0.
print(numbers[4:0:-1]) 






