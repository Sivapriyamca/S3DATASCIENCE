print("Sivapriya Rajan")
print("SJC21MCA-2042")


num = int(input("Enter any number: "))
sum = 0
for i in range(1, num):
   if(num % i == 0):
       sum = sum + i
if (sum == num):
   print("The number is a PERFECT Number ")
else:
   print("The number is NOT A PERFECT Number !")

