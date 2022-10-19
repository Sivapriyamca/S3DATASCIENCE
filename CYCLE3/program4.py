print("Sivapriya Rajan")
print("SJC21MCA-2042")

import matplotlib.pyplot as plt
import numpy as np
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[173,153,195,147,120,144,148,109,174,130,172,131]
plt.plot(x, y, color='red', linestyle='solid' ,label='Affordable segment')

x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[189,189,105,112,173,109,151,197,174,145,177,161]
plt.plot(x,y,color='c', linestyle='solid' ,label='Luxury segment')

x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[185,185,126,134,196,153,112,133,200,145,167,110]
plt.plot(x,y,color='k',linestyle='solid',label='Super luxury segment')

plt.legend(["Affordable segment", "Luxury segment","Super luxury segment"], loc ="upper right")

plt.show()