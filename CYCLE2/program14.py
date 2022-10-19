print("Sivapriya Rajan")
print("SJC21MCA-2042")
import numpy as np
np.random.seed(42)
A = np.random.randint(0, 10, size=(5, 6))
B = np.random.randint(0, 10, size=(3, 3))
print("Matrix A:\n{}\n".format(A))
print("Matrix B:\n{}\n".format(B))
C = A[1:4, 2:5] @ B
A[1:4, 2:5] = C
print("Matrix c:\n{}\n".format(C))

print("Matrix A after sub-matrix multiplication:\n{}\n".format(A))