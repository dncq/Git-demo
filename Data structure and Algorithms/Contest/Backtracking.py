#Generate all binary strings of length n
# n = int(input())
# x = [0 for j in range(n)]
# count = 0
# def Try(k):
#     for v in range(0,2):
#         x[k] = v
#         if k == n-1: 
#             solution()
#         else:
#             Try(k+1)
        
# def solution():
#     global count
#     for i in range(n):
#         print(x[i], end = '')
#     count += 1
#     print()
# Try(0)
# print('Number of strings:',count)

# ---------------------------------------------------------

#Generate all binary strings of length n without consecutive 1
# n = int(input())
# x = [0 for j in range(n)]
# # count = 0
# def check(v,k):
#     if k == 0:
#         return 1
#     return v + x[k-1] <= 1
# def Try(k):
#     for v in range(0,2):
#         if check(v,k):
#             x[k] = v
#             if k == n-1: 
#                 solution()
#             else:
#                 Try(k+1)

# def solution():
#     # global count
#     for i in range(n):
#         print(x[i], end = '')
#     # count += 1
#     print()
# Try(0)
# print('Number of strings:',count)

# ----------------------------------------------

#Generate all m-element subset of the set of n-element
# Equivalent to the problem: Enumerate all set S(m,n) = {(a1,a2,.., am) s.t 1<= a1 < a2 < ... < am <= n}
import sys
def input():
    [m,n] = [int(x) for x in sys.stdin.readline().split()]
    return m,n
m,n = input()
x = [0 for i in range(m)]
# count = 0
def Try(k):
    for v in range(x[k-1] + 1, n-m+k+2):
        x[k] = v
        if k == m-1: 
            solution()
        else:
            Try(k+1)

def solution():
    # global count
    for i in range(m):
        print(x[i], end = ' ')
    # count += 1
    print()
Try(0)
# print('Number of subsets:',count)

# ----------------------------------------------

#Generate all permutations of n
# n = int(input())
# x = [0 for i in range(n)]
# def solution():
#     for i in range(n):
#         print(x[i], end = ' ')
#     print()

# def check(v,k):
#     for i in range(k):
#         if v == x[i]:
#             return False
#     return True

# def Try(k):
#     for v in range(1,n+1):
#         if check(v,k):
#             x[k] = v
#             if k == n-1:
#                 solution()
#             else:
#                 Try(k+1)
# Try(0)

# ----------------------------------------------------

#Place n queens such that no two queens attack each other
# n = int(input())
# x = [0 for j in range(1,n+1)] #j: the number of column (j = 1,2,...,n)
#                           #x[j]: the number of row at column j (x[j] = 1,2,...n)
# count = 0
# def check(v,k):
#     for i in range(k):
#         if v == x[i]:  
#             return False
#         elif v + k == x[i] + i: 
#             return False
#         elif v - k == x[i] - i: 
#             return False
#     return True

# def Try(k):
#     for v in range(1,n+1):
#         if check(v,k):
#             x[k] = v
#             if k == n-1: 
#                 solution()
#             else: 
#                 Try(k+1)

# def solution():
#     global count
#     for i in range(n):
#         print(x[i], end = ' ')
#     count += 1
#     print()
# Try(0)
# print('Number of solutions:', count)

# ---------------------------------------------------

# #Generate all solution of sudoku problem
# x = [[0 for i in range(9)] for j in range(9)]
# count = 0
# def solution():
#     global count
#     # for r in range(9):
#     #     for c in range(9):
#     #         print(x[r][c], end = ' ')
#     #     print()
#     count += 1
#     # print('-----------------')
# def check(v,r,c):
#     for m in range(r):
#         if x[m][c] == v:
#             return False
#     for h in range(c):
#         if x[r][h] == v:
#             return False
#     I = r // 3
#     J = c // 3
#     i = r - 3*I
#     j = c - 3*J
#     for i1 in range(i):
#         for j1 in range(3):
#             if x[3*I + i1][3*J + j1] == v:
#                 return False
#     for j1 in range(j):
#         if x[3*I + i][3*J + j1] == v:
#             return False
#     return True

# def Try(r,c):
#     for v in range(1,10):
#         if check(v,r,c):
#             x[r][c] = v
#             if r == 8 and c == 8:
#                 solution()
#             else:
#                 if c == 8:
#                     Try(r+1,0)
#                 else:
#                     Try(r,c+1)
# Try(0,0)
# print('Number of solutions:', count)

# -------------------------------------

#Count the number of sudoku solutions
# def input():
#     A = []
#     for i in range(9):
#         rows = [int(x) for x in sys.stdin.readline().split()]
#         A.append(rows)
#     return A
# x = input()
# count = 0
# def solution():
#     global count
#     count += 1
# def check(v,r,c):
#     for m in range(r):
#         if x[m][c] == v:
#             return False
#     for h in range(c):
#         if x[r][h] == v:
#             return False
#     I = r // 3
#     J = c // 3
#     i = r - 3*I
#     j = c - 3*J
#     for i1 in range(i):
#         for j1 in range(3):
#             if x[3*I + i1][3*J + j1] == v:
#                 return False
#     for j1 in range(j):
#         if x[3*I + i][3*J + j1] == v:
#             return False
#     return True
# def Try(r,c):
#     for v in range(1,10):
#         if check(v,r,c):
#             x[r][c] = v
#             if r == 8 and c == 8:
#                 solution()
#             else:
#                 if c == 8:
#                     Try(r+1,0)
#                 else:
#                     Try(r,c+1)
# Try(0,0)
# print(count)    

""" 0 0 3 4 0 0 0 8 9
    0 0 6 7 8 9 0 2 3
    0 8 0 0 2 3 4 5 6
    0 0 4 0 6 5 0 9 7
    0 6 0 0 9 0 0 1 4
    0 0 7 2 0 4 3 6 5
    0 3 0 6 0 2 0 7 8
    0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 """

# Toán rời rạc
n = 5
count = 0
x = [0 for i in range(n)]
def solution():
    global count
    count += 1
    # for i in range(n):
    #     print(x[i], end = ' ')
    # print()

def check(x,k):
    if k == 0:
        return True
    if x[k-1] == x[k] == 0 or x[k-1] == x[k] == 1:
        return False
    return True

def Try(k):
    for v in range(3):
        if check(x,k):
            x[k] = v
            if k == n-1:
                solution()
            else:
                Try(k+1)

Try(0)
print(count)
