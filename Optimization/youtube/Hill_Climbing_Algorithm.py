import random
import math
import mip
import itertools
import numpy as np
import matplotlib.pyplot as plt

N = 20
K = 5
V = set(range(N+1))
location = [(np.random.uniform(0,10), np.random.uniform(0,10))]
plt.plot(location[-1][0], location[-1][1],'rs')

d = [0]
for i in V - {0}:
    location.append((np.random.uniform(0,10),np.random.uniform(0,10)))
    d.append(random.randint(1,3))
    plt.scatter(location[-1][0],location[-1][1],d[-1]*20,'b')
    plt.text(location[-1][0],location[-1][1],str(i))
plt.show()

def distance(a,b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

e = []
for i in range(1,N + 1):
    e.append('%.0f'%np.random.uniform(1,6))
    
c = [[0 if i==j else '%.0f'%distance(location[i], location[j]) for j in V] for i in V]

capacity = 8
M = math.ceil(sum(d)/capacity)

Sorted_cities = []

for i in range (1, N + 1):
    Sorted_cities.append((c[0][i] + e[i - 1], str(i)))

Sorted_cities.sort(reverse = 1)

print(Sorted_cities)

Centre = [Sorted_cities[0:K]]

