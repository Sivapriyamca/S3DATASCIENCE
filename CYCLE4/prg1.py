print("Sivapriya Rajan")
print("SJC21MCA-2042")

import pandas as pd
data=pd.read_csv("iris.csv")
print(data)
print("\nshape of dataset:")
print(data.shape )
print("\nFirst 5 and last five rows of data set(head and tail)")
print(data.head(5))
print(data.tail(5))
print("\nSize of dataset")
print(data.size)

print("No:of samples available for each variety")


print("\nDescription of the data set( use describe")
print(data.describe)