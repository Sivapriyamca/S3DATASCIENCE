
print("Sivapriya Rajan")
print("SJC21MCA-2042")

rows = int(input("Enter the Number of rows : "))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
print("Sivapriya Rajan")
print("SJC21MCA-2042")

matrix_a = [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in matrix_a:
   print(n)

print("Enter the elements of Second Matrix:")
matrix_b = [[int(input()) for i in range(column)] for i in range(rows)]
for n in matrix_b:
   print(n)

result = [[0 for i in range(column)] for i in range(rows)]

for i in range(rows):
   for j in range(column):
       result[i][j] = matrix_a[i][j] + matrix_b[i][j]
print("sum of the matrices is")
for r in result :
    print(r)