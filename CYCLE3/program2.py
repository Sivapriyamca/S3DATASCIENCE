print("Sivapriya Rajan")
print("SJC21MCA-2042")

import matplotlib.pyplot as plt
x=['monday','tuesday','wednesday','thursday','friday']
y=[300,450,150,400,650]
plt.subplot(2,1,1)
plt.plot(x, y, color='cyan', linestyle='dotted', linewidth = 3,
         marker='h', markerfacecolor='magenta', markersize=12, mec='b')
plt.xlabel('Days of week')
plt.ylabel('sales of drink')
plt.title(' sales data1(right aligned)')
plt.grid(color='blue',linestyle=':')



x=['monday','tuesday','wednesday','thursday','friday']
y=[400,500,350,300,500]
plt.subplot(2,1,2)
plt.plot(x, y, color='yellow', linestyle='dashed', linewidth = 3,
         marker='d', markerfacecolor='green', markersize=12, mec='r')
plt.xlabel('Days of week')
plt.ylabel('sales of food')
plt.title(' sales data2(center aligned)')
plt.grid(color='blue',linestyle=':')

plt.show()
