import numpy as np
#arr = np.array([3, 7, 2, 9, 1, 6, 8, 4])

#over_five = arr[arr > 5]
#print("Greater than 5:", over_five)

# Replace elements less than 4 with 0 in the original array
#arr[arr < 4] = 0
#print("After replacing <4 with 0:", arr)


#Q2

#arr = np.array([10, 20, 30, 40, 50, 60])
#a = arr[[1, 3, 4]]
#print(a)

#arr[[0, 2, 5]] = [100, 200, 300]
#print(arr)


#Q3

# a = np.array([1,2,3,4])
# b = np.array([10,20,30,40])
#
# #print(a + b)   # [11 22 33 44]
# #print(a - b)   # [-9 -18 -27 -36]
# #print(a * b)   # [10 40 90 160]
# #print(a / b)   # [0.1 0.1 0.1 0.1]
# print(a ** b)  # [1 1048576 205891132094649 1208925819614629174706176]
#


import numpy as np

scores = np.array([
    [45, 78, 82, 90],
    [88, 92, 79, 85],
    [55, 64, 60, 70],
    [95, 98, 99, 100],
    [35, 40, 50, 60]
])

# Task 1: Add 10 points to all scores less than 60
scores[scores < 60] += 10
print("After adding bonus points:\n", scores)

# Task 2: Fancy indexing
# Select students 2 and 3 (index 1 and 2)
selected_students = scores[[1, 2]]
print("\nSelected students:\n", selected_students)

# From these students, select 2nd and 3rd subjects (index 1 and 2)
selected_subjects = selected_students[:, [1, 2]]
print("\nSelected subjects from those students:\n", selected_subjects)

# Task 3: Element-wise math operations
# Average score per student
avg_per_student = scores.mean(axis=1)
print("\nAverage per student:\n", avg_per_student)

# Difference between highest and lowest score per student
diff_per_student = scores.max(axis=1) - scores.min(axis=1)
print("\nDifference between highest and lowest per student:\n", diff_per_student)
