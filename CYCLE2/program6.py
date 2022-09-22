import numpy as np
print("Sivapriya Rajan")
print("SJC21MCA-2042")
print("   ")
a =np.array([[2,4,3,5],
             [4,3,2,1],
             [2,7,6,4],
             [9,8,5,3]])
print("two dimension array is")
print(a)
print("array excluding first row")
m1=np.delete(a,0,axis=0)
print(m1)
#print("alternate method for deleting first row")
#print(a[1:,])
print("array excluding last column")
print(a[:, :-1])
#print("alternate method for excluding last column")
#b=np.delete(a,-1,axis=1)
#print(b)
print(" elements of 1 st and 2 nd column in 2 nd and 3 rd row")
print(a[1:3,0:2])
print("the elements of 2 nd and 3 rd column")
print(a[:,[1,2]])
print(" 2 nd and 3 rd element of 1 st row")
print(a[0:1,1:3])
print("element from indices 4 to 10 in descenting order")
flat_array=a.flatten()
print(flat_array)
new=sorted(flat_array[-3:-10])
index=flat_array[11:4:-1]
print(index)




