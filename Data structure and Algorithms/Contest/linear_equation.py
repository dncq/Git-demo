import sys
# def input():
#     [n,N] = [int(x) for x in sys.stdin.readline().split()]
#     c = [int(x) for x in sys.stdin.readline().split()]
#     return n,N,c

# n,N,c = input()
# x = [0 for i in range(n+1)]
# T = 0 #sum of assigned variables, T is maintained incrementally
# cnt = 0
# lst = []
# def check(v,k):
#     global T  
#     T = 0
#     for i in range(1,k):
#         T = T + x[i]
#     if k < n:
#         return T + v < N 
#     else:
#         return T + v == N



# def solution():
#     global cnt
#     global lst
#     # r = 0 
#     # for i in range(n):
#     #     r += x[i+1] % c[i]
#     # if (x[1] % 2 == 0) and (x[2] % 4 == 0) and (x[3] % 3 == 0) and (x[4] % 5 == 0) and (x[1] / 2 + x[2] / 4 == 6):
#     # if r <= 0 and (x[1] / c[0]  < x[3] / c[2] ):

#     # if x[1] < x[2] < x[3] < x[4] < x[5] < x[6]:
#     cnt += 1
#     lst.append(x[1:])
#     # print(*x[1:])

# def Try(k):
#     # global cnt
#     # cnt += 1
#     global T
#     for v in range(1, N - T -(n-k) +1):
#         if check(v,k):
#             x[k] = v
#             T = T + v #update T incrementally
#             if k == n:
#                 solution()
#             else:
#                 Try(k+1)
#             T = T - v #recover T when backtracking
# # Try(1)
# # # print('Number of solution:', cnt)
# # # print(lst)





# def INP():
#     [n,M] = [int(x) for x in sys.stdin.readline().split()]
#     c = [int(x) for x in sys.stdin.readline().split()]
#     return n,M,c

# n,M,c = INP()

# T = 0
# R = sum(c) - c[0]
# count = 0
# x = [0 for i in range(n)]

# def check(v,k):
#     if k < n:
#         return 1
#     elif k == n:
#         return T + c[k]*v == M


# def solution():
#     # global count
#     # count += 1
#     for i in range(n):
#         print(x[i], end = ' ')
#     print()
#     # return count

# def Try(k):
#     global T
#     global R
#     for v in range(1,(M-T-R)//c[k] + 1):
#         if check(v,k):
#             x[k] = v
#             T += c[k]*x[k]
#             R -= c[k+1]
#             if k == n-1: solution()
#             else: Try(k+1)
#             T -= c[k]*x[k]
#             R += c[k+1]

# Try(0)

# print(c)



# ------------------------------------------------------------

#Not so good implementation (Sinh dãy n phần tử có tổng = N)
import sys

def input():
    [n,N] = [int(x) for x in sys.stdin.readline().split()]
    return n,N

n,N = input()
x = [0 for i in range(n+1)]

def check(v,k):
    T = 0 
    for i in range(1,k):
        T = T + x[i]
    if k < n:
        return T + v < N
    else:
        return T + v == N

def solution():
    for i in x[1:]:
        print(i, end=" ")
    print()
    # print(*x[1:])

def Try(k):
    for v in range(1,N+1):
        if check(v,k):
            x[k] = v
            if k == n:
                solution()
            else:
                Try(k+1)

Try(1)