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
B=np.array([[3,2],[3,4]])
print("second matrix\n",B)
power=np.power(A,3)
print("cube using power function\n",power)

print("cube using * function\n",B*B*B)

print("cube usig '**' fuction \n",B**3)

square=np.multiply(A,A)
cube=np.multiply(square,A)
print("cube using multiply function\n",cube)

b=np.identity(2)
print("identity matrix is\n",b)
print(" each element of the matrix with different powers.\n",np.power(B,[[1,2],[3,4]]))
y=np.array([[4,3],
              [2,5]])
print("x^2+2y\n",(B**2)+(2*y))