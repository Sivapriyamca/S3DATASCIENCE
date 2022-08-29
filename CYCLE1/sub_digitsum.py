print("Sivapriya Rajan")
print("SJC21MCA-2042")
num=int(input("enter a positive number"))
digsum=0
new_num=num
while new_num >= digsum:
    list1 = [int(x) for x in str(new_num)]
    for i in list1:
        digsum=digsum+i
    new_num=num-digsum

    print(new_num)
print(new_num-new_num)



