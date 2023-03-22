# VRP
import random
import math
import mip
import itertools
# import numpy as np
import matplotlib.pyplot as plt

N = 10
V = set(range(N))
location = [(random.randint(0,10), random.randint(0,10))]
plt.plot(location[-1][0], location[-1][1],'rs')

d = [0]
for i in V - {0}:
    location.append((random.randint(0,10),random.randint(0,10)))
    d.append(random.randint(1,3))
    plt.scatter(location[-1][0],location[-1][1],d[-1]*20,'b')


plt.show()

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

c = [[0 if i==j else distance(location[i], location[j]) for i in V] for j in V]

capacity = 8
M = math.ceil(sum(d)/capacity)

# print(M)

model = mip.Model()

x = [[model.add_var(var_type = mip.BINARY) for j in V] for i in V]
# y = [model.add_var(var_type = mip.INTEGER) for i in V]

model.objective = mip.minimize(mip.xsum(c[i][j]*x[i][j] for i in V for j in V))

for i in V-{0}:
    model += mip.xsum(x[i][j] for j in V - {i}) == 1
for i in V-{0}:
    model += mip.xsum(x[j][i] for j in V - {i}) == 1
model += mip.xsum(x[0][j] for j in V - {0} )== M
model += mip.xsum(x[i][0] for i in V - {0} )== M

for r in range(1,N):
    for s in itertools.combinations(V-{0},r):
        S = set(s)
        NS = V - S
        demand = sum([d[i] for i in S])
        model += mip.xsum(x[i][j] for i in S for j in NS) >= math.ceil(demand/capacity)
model.optimize()

if model.num_solutions:
    print('Objective: %.2f'% model.objective_value)

    for i in V:
        if i == 0:
            plt.plot(location[0][0], location[0][1], 'rs')
        else:
            plt.scatter(location[i][0], location[i][1], d[i]*20,'b')
        for j in V:
            if x[i][j].x > 0.9:
                # model += y[i] >= y[i] + (N+1)*x[i][j] -N
                plt.plot([location[i][0],location[j][0]], [location[i][1], location[j][1]])
    plt.show()

# for i in V-{0}:
#     model += y[i]<= N
#     model += y[i]>= 1
# model += y[0] == 1

# model.optimize()

#Hill-Climbing Algorithm
