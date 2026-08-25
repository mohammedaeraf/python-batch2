# Tuples are like lists, but they are intended for fixed collections of values.
# Parentheses are commonly used to create a tuple; lists use square brackets.
# Tuples are immutable (unmodifiable) after they are created.
# Indexing, negative indexes, slicing, and loops work the same way as with lists.

student1 = ("Arif", 20, "Python Programming")
print(student1)

# These operations would fail because a tuple cannot be changed after creation.
# student1[1] = 21
# student1.append("Bhatkal")

# A tuple can store a sequence of related values, such as the days of a week.
week_days = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday")

# Slice indexes select Sunday, Monday, and Tuesday (the end index is excluded).
print(week_days[0:3])

# Iterating over a tuple visits each item in order.
for day in week_days:
    print(day)

# The in operator checks whether a value exists in the tuple.
search_day = "Funday"

if search_day in week_days:
    print(search_day,"is present in tuple")
else:
    print(search_day,"is not present in tuple")


# A multiline tuple makes a longer fixed sequence easier to read.
months = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July"
)

# Tuples can also represent a fixed group of values, such as an x/y point.
point = (10, 20)



