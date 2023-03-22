# Importing packages
import matplotlib.pyplot as plt
import numpy as np
# Define x and y values
x = [5, 10, 50,50,100, 100]
y = [0.03,0.58,10.45,21.37,43.12,58.76]

plt.plot(x, y)
plt.title('Integer Linear Programming', fontsize = 18)
# plt.axhline(np.mean(y),color = None,label="Mean score={:.3f}".format(np.mean(y)),linestyle="--",linewidth= 1)
# plt.xlabel('Running time', fontsize=14)
# # plt.ylabel('Running time (ms)', fontsize=14)
# plt.grid(True)
plt.show()
# Plot a simple line chart without any feature
# plt.plot(x, y)
# plt.show()

import statistics
std_dev = statistics.stdev(results)