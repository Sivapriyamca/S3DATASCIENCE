print("Sivapriya Rajan")
print("SJC21MCA-2042")
print("   ")

import numpy as np
arr1=np.array([1,8,3,7,5,6])

arr2=np.array([[1,6,3,4,5,8],
               [1,2,7,4,4,6],
               [3,2,3,4,2,9],
               [2,9,3,4,5,6],
               [1,7,3,4,2,8]])
print("first array",arr1)
print("sum of first array arr1 is",np.sum(arr1))
print("Sum of arr1(uint8) : ", np.sum(arr1, dtype=np.uint8))
print("Sum of arr1(float32) : ", np.sum(arr1, dtype=np.float32))
print("second array",arr2)
print("sum of 2d array arr2 is ",np.sum(arr2))
print("Sum of arr2(uint8) : ", np.sum(arr2, dtype=np.uint8))
print("Sum of arr2(float32) : ", np.sum(arr2, dtype=np.float32))