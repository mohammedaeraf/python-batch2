import matplotlib.pyplot as plt

students = ["Ahmed", "Sara", "Rahul", "Fatima"]
marks = [85, 92, 78, 88]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()