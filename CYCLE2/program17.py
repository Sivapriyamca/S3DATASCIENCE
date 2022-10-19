print("Sivapriya Rajan")
print("SJC21MCA-2042")
import numpy as np
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
print("matrix A\n",A)

b = np.array([[-3],
              [5],
              [-2]])
print("matrix b\n",b)
a=np.linalg.inv(A)
x= np.linalg.solve(a, b)
print("Value of X=A -1 b: ")
print(x)