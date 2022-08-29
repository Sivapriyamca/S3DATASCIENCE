print("Sivapriya Rajan")
print("SJC21MCA-2042")
list2=[0,1,2,3,4,5,6,7,8,9]
mob_number=int(input("enter your mobile number"))
list1=[int(x) for x in str(mob_number)]
print(list1)
print(list2)
for i in range(0,10,1):
    if i not in list1:
            print(i)


