import random
import math
import numpy as np
import matplotlib.pyplot as plt
import sys

N = 10
V = set(range(N+1))
location = [(np.random.uniform(0,50), np.random.uniform(0,50))]
plt.plot(location[-1][0], location[-1][1],'rs')

d = [0]
for i in V - {0}:
    location.append((np.random.uniform(0,50),np.random.uniform(0,50)))
    d.append(random.randint(1,3))
    plt.scatter(location[-1][0],location[-1][1],d[-1]*20,'b')
    plt.text(location[-1][0],location[-1][1],str(i))

plt.show()

def distance(a,b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

c = [[0 if i == j 
      else distance(location[i], location[j]) 
      for j in V] for i in V]

# np.random.seed(0)
# y0 = list(np.random.permutation(N))
# y = [y0[i] for i in range(N)]
# print(y)

def TSP_tour_cost(y,c,N):
    y.append(y[0])
    cost = 0
    for i in range(N):
        cost += c[y[i]][y[i+1]]
    y.pop(-1)
    return cost


def TSP_tour_plot(y,location,N):
    y.append(y[0])
    for i in range(N):
        plt.plot([location[y[i]][0], location[y[i+1]][0]],[location[y[i]][1], location[y[i+1]][1]],'r')
    # plt.show()
    y.pop(-1)

# print(TSP_tour_cost(y,c,N))
# TSP_tour_plot(y,location,N)

def TSP_onestep_opt2(y,c,N):
    y.append(y[0])
    for i in range(N-2):
        for j in range(i+2,N):
            total_distance_pre = c[y[i]][y[i+1]] + c[y[j]][y[j+1]]
            total_distance_post = c[y[i]][y[j]] + c[y[i+1]][y[j+1]]
            # print(y[i],y[i+1],y[j],y[j+1],total_distance_pre-total_distance_post)
            if total_distance_post < total_distance_pre:
                for k in range(math.ceil(((j-i-1)/2))):
                    temp = y[i+k+1]
                    y[i+k+1] = y[j-k]
                    y[j-k] = temp
                y.pop(-1)
                return (1,y)
    y.pop(-1)
    return (0,y)

def TSP_opt2(y,c,N,max_iter):
    cost_record = []
    for i in range(max_iter):
        (label,y) = TSP_onestep_opt2(y,c,N)
        cost_record.append(TSP_tour_cost(y,c,N))
        if label == 0:
            break
    return (cost_record, y)

def partition (list_in, n):
    lst = list_in[:]
    random.shuffle(lst)
    return [lst[i::n] for i in range(n)]
[K] = [int(x) for x in sys.stdin.readline().split()]
# N: số thành phố
# K: số nhân viên
group = []
cities = np.random.permutation([i for i in range(1,N+1)])
u = partition(cities, K)
for i in u:
    group.append(list(i))
for u in group:
    u.insert(0,0)
print(group)

c_group = []
location_group = []
for subgroup in group:
    c_group.append([[c[i][j] for j in subgroup] for i in subgroup])
    location_group.append([location[i] for i in subgroup])
print(c_group)
print(location_group)
# (label,y) = TSP_onestep_opt2(y,c,N)
# cost = TSP_tour_cost(y,c,N)
# (cost_record,y) = TSP_opt2(y,c,N,1000)
# print(cost_record[-1])
# TSP_tour_plot(y,location,N)
# plt.plot(cost_record)
# plt.show()
# print(label,cost,y)

max_iter = 100000
total_cost = 0
for m in range(K):
    sub_node = group[m]
    sub_N = len(sub_node)
    sub_c = c_group[m]
    sub_y = list(range(sub_N))
    sub_location = location_group[m]
    cost_record, sub_y = TSP_opt2(sub_y, sub_c,sub_N, max_iter)
    TSP_tour_plot(sub_y,sub_location,sub_N)
    total_cost += cost_record[-1]

for i in V-{0}:
    plt.scatter(location[i][0],location[i][1],d[i]*20,'b')
plt.show()
print(total_cost)