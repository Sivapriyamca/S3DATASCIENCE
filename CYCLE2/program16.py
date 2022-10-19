print("Sivapriya Rajan")
print("SJC21MCA-2042")
import numpy as np

B=np.array([[3,4],[4,3]])
C=np.transpose(B)
if (C == B).all() :
    print(" A is symmetric Matrix")
elif (C == -B).all():
    print("A is skew symmetric matrix")
else:
    print("not symmetric and skew symmetric")
