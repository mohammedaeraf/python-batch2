# Open the file manually, read all of its contents, and close it explicitly.
file = open("students.txt", "r")
content = file.read()
print(content)
file.close()

# The with statement closes the file automatically when this block ends.
with open("students.txt", "r") as file:
    # read() returns the entire file as one string.
    content = file.read()
    print(content)

# Iterate over the file one line at a time instead of loading it all at once.
with open("students.txt", "r") as file:
    for line in file:
        print(line)

# Open the file in append mode so new text is added after existing content.
with open("students.txt", "a") as file:
    # This text is appended exactly as written; it does not add a newline.
    file.write("Javed")

