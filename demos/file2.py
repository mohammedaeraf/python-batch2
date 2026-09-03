# Keep reading names until the user chooses to stop.
with open("students.txt", "a") as file:
    while True:
        name = input("Enter your name: ")

        # Write each name on its own line in the students file.
        file.write(name + "\n")

        # Ask whether another name should be read and saved.
        answer = input("Do you want to continue? (yes/no): ")
        if answer == "no":
            break