import numpy as np

arr = np.array([5,6,7,8,9,10,11,12,13,14,15])
print(arr)
print(arr.dtype)
print(arr.size)
print(arr.ndim)
print(arr.shape)

quetwo_Array = np.array([1, 2, 3, 4, 5,6,7,8,9,10,11,12])

quetwo_twod = quetwo_Array.reshape(3,4)
print(quetwo_twod)

quetwo_Array= np.delete(quetwo_Array,9)
quetwo_Array = np.append(quetwo_Array,20)
print(quetwo_Array)


a = np.array([12, 4, 7, 1, 9])

a = np.sort(a)
print(a)

d = np.array([[1,2,3],[4,5,6],[7,8,9]])
e = d[0:2]
last_column = d[2]
print(e)
print(last_column + "is the last column")


f = np.array([1,2,3,4,5])

f = np.reshape(5,1)

ar = np.array([[10,20,30],[40,50,60],[70,80,90]])

ar_v = ar[2:1]
