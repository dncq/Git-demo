import sys
import numpy as np
import random

def partition (list_in, n):
    lst = list_in[:]
    random.shuffle(lst)
    return [lst[i::n] for i in range(n)]
[N,K] = [int(x) for x in sys.stdin.readline().split()]
# N: số thành phố
# K: số nhân viên
groups = []
cities = np.random.permutation([i for i in range(1,N+1)])
u = partition(cities, K)
for i in u:
    groups.append(list(i))
for k in groups:
    k.insert(0,0)
print(groups)


