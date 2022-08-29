print("Sivapriya Rajan")
print("SJC21MCA-2042")
print("21mca006- Anish Anjali")
n=int(input("Enter limit: "))
f1 = 0
f2 = 1
for x in range(0, n):
   print(f2, end=" ")
   next = f1 + f2
   f1 = f2
   f2 = next
