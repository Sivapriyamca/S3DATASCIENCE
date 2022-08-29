print("Sivapriya Rajan")
print("SJC21MCA-2042")
s1 = int(input("Enter the length for Side 1:"))
s2 = int(input("Enter the length for Side 2:"))
s3 = int(input("Enter the length for side 3:"))
if s1+s2+s3 ==180:
   if s1 == s2 and s2 == s3 and s3==s1:
       print("The given lengths are of an Equilateral triangle ")
   elif s1 == s2 or s1 == s3 or s2==s3:
       print("The given lengths are of an Isosceles triangle")
   else:
       print("The given lengths are of a Scalar triangle")
else:
    print("sum of angles of triangle should not exceed 180")
