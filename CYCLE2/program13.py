print("Sivapriya Rajan")
print("SJC21MCA-2042")
import numpy as np
rows=int(input("enter the number of rows:"))
column=int(input("enter the number of column:"))
print("enter the values to the  matrix:")
A=[[int(input()) for i in range(column)]for i in range(rows)]
print("first matrix is")
for j in A:
    print(j)
power=np.power(A,3)
print("cube using power function",power)
cube=np.multiply(A,3)
print("cube using multiply function",cube)