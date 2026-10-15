import matplotlib.pyplot as plt

# Student names and their corresponding marks.
students = ["Ahmed", "Sara", "Rahul", "Fatima"]
marks = [85, 92, 78, 88]

# Draw one bar for each student's mark.
plt.bar(students, marks)

# Label the chart and its axes.
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

# Display the finished chart.
plt.show()