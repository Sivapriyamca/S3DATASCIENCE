print("Sivapriya Rajan")
print("SJC21MCA-2042")

list1 = []
list2 = []
list3 = []
print("Sivapriya Rajan")
print("SJC21MCA-2042")

items = int(input(" Enter the total number of the list elements: "))

print(" Enter the items into List 1 : ")
for i in range(1, items + 1):
   num = int(input(" Enter the value of %d index is :" % i))
   list1.append(num)

print(" Enter the items into the List 2 : ")
for i in range(1, items + 1):
   num = int(input(" Enter the value of %d index is :" % i))
   list2.append(num)

for j in range(items):
   list3.append(list1[j] + list2[j])
print("\n Addition of the two lists is ", list3)
