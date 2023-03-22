""" x = (x0, x1, ...., x(n-1))
    f(x) = c(x0,x1) + c(x1,x2) + ... + c(x(n-1), x(n))
    Try(k) 
    -----------------------------------------------"""
'''import random
import sys
def input():
    [n] = [int(x) for x in sys.stdin.readline().split()]
    A = []
    for i in range(n):
        row = [int(x) for x in sys.stdin.readline().split()]
        A.append(row)
    return n, A
n, c = input()

x = [0 for i in range(n)]
mark = [False for v in range(n)]
f = 0 # represents the total travel cost (distance), accumulated
f_best = 1e9 + 7 # represent the best objective value
cm = 10000

def Solution():
    global f
    """check if the current solution is better than the best solution found so far"""
    if f + c[x[n-1]][x[0]] < f_best:
        # f_best = f + c[x[n-1]][x[0]]
        print('Current solution: ',x,' --> update best: ', f_best)
        f_best[:] = x[:]
def Try(k): #try all value for x[k]
    global f
    for v in range(n):
        if mark[v] == False: #value v has not been used
            x[k] = v
            f = f + c[x[k-1]][x[k]]
            mark[v] = True # mark value v has been used
            if k == n-1:
                Solution()
            else:
                g = f + cm*(n-k) #lower bound of the objective function
                if g < f_best:
                    Try(k+1)
            mark[v] = False
            f = f - c[x[k-1]][x[k]]
def genData(n):
    #c = [[0] for i in range(n) for j in range(n)]
    for i in range(n):
        for j in range(n):
            c = random.randint(1,10)
            print(c, end = ' ')
        print('')

genData(6)
x[0] = 0
mark[0] = True
Try(1) '''


# TSP
# import sys
# def input():
#     [n] = [int(x) for x in sys.stdin.readline().split()]
#     c = []
#     for i in range(n):
#         row = [int(x) for x in sys.stdin.readline().split()]
#         c.append(row)
#     return n,c

# n, c = input()
# Cm = 1e9
# for i in range(n):
#     for j in range(n):
#         if i != j and c[i][j] < Cm:
#             Cm = c[i][j]
# #print(c)

# x = [0 for i in range(n)]
# mark = [False for v in range(n)]
# x_best = [0 for i in range(n)]
# f = 0 # represents the total travel cost (distance), accumulated
# f_best = 1000000000 #represents the best objective value

# def solution():
#     '''
#     Check if the current solution is better than the best soluion found so far 
#     if so, then update the best solution found so far
#     '''
#     global f_best
#     if f + c[x[n-1]][x[0]] < f_best:
#         f_best = f + c[x[n-1]][x[0]]
#         print('current solution', f_best)
#         x_best[:] = x[:]

# def Try(k): #try all value for x[k]
#     global f
#     for v in range(n):
#         if mark[v] == False:
#             x[k] = v
#             f = f+c[x[k-1]][x[k]]
#             mark[v] = True #mark value v as it is used
#             if k == n-1:
#                 solution()
#             else:
#                 if f+ Cm*(n-k) < f_best:
#                     Try(k+1)
#             mark[v]= False
#             f = f - c[x[k-1]][x[k]]

# x[0] = 0
# mark[0] = True
# Try(1)
# print(f_best)


# Backtracking (Very slow)


import sys
def INP():
    [n,M] = [int(x) for x in sys.stdin.readline().split()] 
    c = []
    for i in range(n):
        row = [int(x) for x in sys.stdin.readline().split()]
        c.append(row)
    return n,M,c
# n : number of cities
# c: cost of travelling between cities
n,M,c = INP()
f = 0 # represent the current total cost of travelling 
f_best = 1e9 # represent the munumum cost of travelling
mark = [False for i in range(n)] # mark[i] = True: the i-th city has been visited
x = [0 for i in range(n)] # Travelling path 
x_best = [0 for i in range(n)]
count = 0

def updateBest():
    global f_best
    global count
    if f + c[x[n-1]][x[0]] < f_best:
        f_best = f + c[x[n-1]][x[0]]
        x_best[:] = x[:]

def Try(k):
    global f
    global count
    for v in range(n):
        if mark[v] == False:
            x[k] = v
            f = f +  c[x[k-1]][x[k]]
            mark[v] = True
            if k == n-1: 
                updateBest()
                count += 1
            else: 
                Try(k+1)
                count += 1
            # recover the original state before proceeding to the next city
            f = f - c[x[k-1]][x[k]]
            mark[v] = False

x[0] = 0
mark[0] = True
Try(1)
print(f_best)
print(count)


# DATA INSTANCES
'''
4
0 3 1 9
3 0 2 5
1 2 0 10
9 5 10 0
----
6
0 10 4 5 4 8
7 0 10 1 6 3
10 7 0 10 7 7
8 4 4 0 7 7
4 9 3 7 0 8
3 8 8 9 6 0
----
12
0 1 9 8 1 4 8 3 10 7 10 8
5 0 8 6 1 3 4 1 10 3 4 10
2 6 0 6 4 10 7 5 4 10 9 10
7 6 10 0 6 3 6 6 8 10 2 8
10 7 2 5 0 9 7 2 8 8 5 8
4 2 1 3 7 0 3 9 7 10 10 1
7 6 8 6 9 1 0 10 9 7 9 10
9 6 10 9 9 7 8 0 7 3 4 10
9 3 9 4 2 6 3 3 0 10 6 5
6 4 10 8 7 2 6 10 1 0 2 9
9 9 3 1 6 8 9 8 7 6 0 2
5 2 7 8 3 3 8 4 7 8 1 0
----
14
0 4 8 8 4 6 5 8 2 4 6 3 4 10
3 0 10 2 7 4 10 1 3 3 10 9 6 7
8 1 0 3 8 8 10 2 6 4 7 7 1 3
6 3 5 0 8 6 9 2 1 4 2 9 10 6
3 9 3 2 0 10 7 5 3 1 6 4 9 5
3 1 8 3 4 0 6 2 5 7 7 3 7 2
1 6 8 10 4 10 0 4 1 4 8 6 10 10
6 3 6 1 1 3 1 0 7 7 10 10 5 4
3 7 3 3 10 5 6 9 0 8 5 9 10 9
1 7 10 9 9 9 4 3 5 0 7 5 7 9
7 5 5 7 7 6 2 3 1 6 0 3 1 6
7 4 7 4 7 10 2 7 3 1 9 0 4 1
6 9 1 7 10 6 5 8 4 3 7 6 0 6
4 6 3 5 1 10 10 7 5 3 7 8 8 0
'''