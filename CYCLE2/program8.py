print("Sivapriya Rajan")
print("SJC21MCA-2042")
import numpy as np

arr = np.arange(5)
print("1D arr : \n", arr)
print("Shape : ", arr.shape)

a = np.insert(arr, 1, 9)
print("\nArray after insertion : ", a)
print("Shape : ", a.shape)

arr = np.arange(12).reshape(3, 4)
print("\n\n2D arr : \n", arr)
print("Shape : ", arr.shape)

a = np.insert(arr, 1, 9, axis=1)
print("\nArray after insertion : \n", a)
print("Shape : ", a.shape)
