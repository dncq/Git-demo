# TSP
import random
import math
import mip
# import numpy as np
import matplotlib.pyplot as plt

N = 10
V = set(range(N))
location = []
for i in V:
    location.append((random.randint(0,10),random.randint(0,10)))
    plt.plot(location[-1][0], location[-1][1],'b*')
    # plt.text(location[-1][0],location[-1][1],str(i))

# plt.show()

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

c = [[0 if i==j else distance(location[i], location[j]) for i in V] for j in V]

model = mip.Model()

x = [[model.add_var(var_type = mip.BINARY) for j in V] for i in V]
y = [model.add_var(var_type = mip.INTEGER) for i in V]

model.objective = mip.minimize(mip.xsum(c[i][j]*x[i][j] for i in V for j in V))

for i in V:
    model += mip.xsum(x[i][j] for j in V - {i}) == 1
for i in V:
    model += mip.xsum(x[j][i] for j in V - {i}) == 1

for i in V:
    for j in V:
        if i != j:
            model += y[i] >= y[i] + (N+1)*x[i][j] -N

for i in V-{0}:
    model += y[i]<= N
    model += y[i]>= 1
model += y[0] == 1

model.optimize()

if model.num_solutions:
    print('Objective: %.2f'% model.objective_value)
    for i in V:
        print('y[%d]: %.0f'% (i, y[i].x))
        plt.plot(location[i][0],location[i][1],'b*')
        for j in V:
            if x[i][j].x > 0.9:
                plt.plot([location[i][0],location[j][0]], [location[i][1], location[j][1]],'r')
    plt.show()
