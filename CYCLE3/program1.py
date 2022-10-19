print("Sivapriya Rajan")
print("SJC21MCA-2042")

import matplotlib.pyplot as plt
x=[2001,2002,2003,2004,2005,2006,2007]
y=[24000,22500,19700,17500,14500,10000,5800]
plt.plot(x, y, color='red', linestyle='dashed', linewidth = 2,
         marker='*', markerfacecolor='green', markersize=20)
plt.xlabel('year')
plt.ylabel('car value')

plt.title('value depreciation(left aligned)')
plt.show()