# Open the file and read its contents inside the try block.
try:
    file = open("students.txt", "r")
    print(file.read())

# Always close the file after the read attempt to release the file resource.
finally:
    file.close()