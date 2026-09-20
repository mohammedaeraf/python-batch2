try:
    file = open("students.txt", "r")
    print(file.read())

finally:
    file.close()