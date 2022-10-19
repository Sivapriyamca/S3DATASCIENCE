print("Sivapriya Rajan")
print("SJC21MCA-2042")

import matplotlib.pyplot as plt
x=['walking','cycling','car','bus','train']
y=[29,15,35,18,3]
plt.xlabel('mode of transport')
plt.ylabel('frequency')
plt.bar(x,y, width=0.1 ,color="green")
plt.show()