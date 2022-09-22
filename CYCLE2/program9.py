print("Sivapriya Rajan")
print("SJC21MCA-2042")

import numpy as np
arr = np.arange(5)
print("1D arr : \n", arr)

a=np.diag(arr)
print("\nArray after diag() in 1D: ", a)

arr = np.arange(9).reshape(3, 3)
print("\n\n2D arr : \n", arr)

a=np.diag(arr)
print("\nArray after diag() in 2D: ",a)