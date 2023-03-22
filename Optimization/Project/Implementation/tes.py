import sys
import random

def inp():
    [N,K] = [int(x) for x in sys.stdin.readline().split()]
    d = [int(x) for x in sys.stdin.readline().split()]
    t = []
    for i in range(N+1):
        rows = [int(x) for x in sys.stdin.readline().split()]
        t.append(rows)
    return N,K,d,t
N,K,d,t = inp()
d.insert(0,0)
x = [[0,1],[0,1],[1,0],[1,0],[0,1],[1,0]]
print(x)
print()
y =  [[[0,1],[1,1],[1,0],[0,0],[1,0],[0,1]],
      [[0,1],[1,1],[1,0],[0,0],[1,0],[0,1]],
      [[0,1],[1,1],[1,0],[0,0],[1,0],[0,1]],
      [[0,1],[1,1],[1,0],[0,0],[1,0],[0,1]],
      [[0,1],[1,1],[1,0],[0,0],[1,0],[0,1]],
      [[0,1],[1,1],[1,0],[0,0],[1,0],[0,1]]]
for i in y:
    print(i)
print('Demand')
for k in range(K):
    print([d[i] + x[i][k] for i in range(N+1)])
    print([t[i][j] + y[i][j][k] for i in range(N+1) for j in range(N+1)])
# print(t)
# print([0 for j in range(5) for i in range(5)])

'''
5 2
60 80 70 10 90 
0 50 100 60 40 80 
50 0 50 40 20 60 
100 50 0 50 70 40 
60 40 50 0 60 20 
40 20 70 60 0 80 
80 60 40 20 80 0 
'''