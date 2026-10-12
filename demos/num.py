import numpy as np # alias name

data1 = [75, 80, 65, 90,85]
data2 = [45, 50, 39, 52,43]

scores = np.array(data1)
mean = np.mean(scores)
max_score = np.max(scores)
min_score = np.min(scores)

print("Average Score =", mean)
print("Max Score =", max_score)
print("Min Score =", min_score)

numbers = np.array([10,20,40,100])
print(numbers * 2)
print(numbers + 5)

