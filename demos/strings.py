# Strings are immutable
course = "python"
n = 10
print(course[0])

course[0] = "z"




print(len(course))
print(course[0:5])
print(course[-1])

print(course[0:])
print(course[:3])

print(course * 3)

name = "abbas attar"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

if "arif" in name:
    print("Arif exists in the name")
else:
    print("Arif doesn't exist in the name")
text = input("Enter a word:")
reverse = text[::-1]

if text == reverse:
    print("The text you entered",text,"is palindrome")
else:
    print("The text you entered",text,"is not a palindrome")
    

