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

#
# import numpy as np
#
# scores = np.array([
#     [45, 78, 82, 90],
#     [88, 92, 79, 85],
#     [55, 64, 60, 70],
#     [95, 98, 99, 100],
#     [35, 40, 50, 60]
# ])
#
# # Task 1: Add 10 points to all scores less than 60
# scores[scores < 60] += 10
# print("After adding bonus points:\n", scores)

# # Task 2: Fancy indexing
# # Select students 2 and 3 (index 1 and 2)
# selected_students = scores[[1, 2]]
# print("\nSelected students:\n", selected_students)
#
# # From these students, select 2nd and 3rd subjects (index 1 and 2)
# selected_subjects = selected_students[:, [1, 2]]
# print("\nSelected subjects from those students:\n", selected_subjects)
#
# # Task 3: Element-wise math operations
# # Average score per student
# avg_per_student = scores.mean(axis=1)
# print("\nAverage per student:\n", avg_per_student)
#
# # Difference between highest and lowest score per student
# diff_per_student = scores.max(axis=1) - scores.min(axis=1)
# print("\nDifference between highest and lowest per student:\n", diff_per_student)

# import numpy as np
#
# images = np.array([
#     [[ 12,  34,  45,  23],
#      [ 56,  78,  12,  34],
#      [ 90, 123,  45,  67],
#      [ 12,  34,  56,  78]],
#
#     [[200, 180, 190, 210],
#      [220, 230, 200, 210],
#      [180, 170, 160, 150],
#      [140, 130, 120, 110]],
#
#     [[  0,   0,   0,   0],
#      [  0,   0,   0,   0],
#      [255, 255, 255, 255],
#      [255, 255, 255, 255]],
#
#     [[50, 60, 70, 80],
#      [90,100,110,120],
#      [130,140,150,160],
#      [170,180,190,200]],
#
#     [[10, 20, 30, 40],
#      [50, 60, 70, 80],
#      [90,100,110,120],
#      [130,140,150,160]],
#
#     [[5, 15, 25, 35],
#      [45, 55, 65, 75],
#      [85, 95,105,115],
#      [125,135,145,155]]
# ])
#
#
# images[images < 50 ] = 0
# selected_images = images[[1,3,5]]
# two_by_two = selected_images[:, :2,:2]
#
# average_pixels = images.mean(axis=0)
# diffrence = images.max(axis=1) - images.min(axis=1)
# flatten_image = images.ravel()
# print(flatten_image)


import numpy as np

scores = np.array([
    [45, 78, 82, 90],
    [88, 92, 79, 85],
    [55, 64, 60, 70],
    [95, 98, 99,100],
    [35, 40, 50, 60],
    [72, 65, 68, 74]
])


print("shape:", scores.shape)
print("ndim:", scores.ndim)
print("dtype:", scores.dtype)


scores_clean = scores.copy()
scores_clean[scores_clean < 50] = 0
print("\nAfter cleaning (<50 -> 0):\n", scores_clean)


selected_scores = scores_clean[[1, 3, 5]]
print("\nSelected students (2,4,6):\n", selected_scores)


last_two_subjects = selected_scores[:, -2:]
print("\nLast two subjects of selected students:\n", last_two_subjects)


scores_bonus = scores_clean + 5
print("\nAfter adding +5 bonus (sample):\n", scores_bonus)


scores_bonus[:, -1] *= 2
print("\nAfter doubling last column (sample):\n", scores_bonus)


avg_per_student = scores_bonus.mean(axis=1)    # shape (6,)
avg_per_subject = scores_bonus.mean(axis=0)    # shape (4,)
max_per_subject = scores_bonus.max(axis=0)     # shape (4,)

print("\nAverage per student:\n", avg_per_student)
print("\nAverage per subject:\n", avg_per_subject)
print("\nMax per subject:\n", max_per_subject)

flattened = scores_bonus.flatten()
reshaped_3_8 = flattened.reshape(3, 8)
print("\nFlattened length:", flattened.shape)
print("Reshaped to (3,8):", reshaped_3_8.shape)
