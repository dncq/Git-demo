''' Longwst common subsequences'''

# import sys

# def input():
#     X = [int(x) for x in sys.stdin.readline().split()]
#     Y = [int(x) for x in sys.stdin.readline().split()]
#     return X,Y

# X,Y = input()
# #print(X,Y)
# n = len(X)
# m = len(Y)
# S = [[0 for j in range(m)] for i in range(n)]
# # print(S)


# # smallest subproblem: S[0][j] and S[i][0]
# if X[0] == Y[0]:
#     S[0][0] = 1
# for j in range(m):
#     #S[0][j] = 1 if X[0] appears in Y[0..j] and 0, otherwise
#     if X[0] == Y[j]:
#         S[0][j] = 1
#         # trace[0][j] = 'D' 
#     else:
#         S[0][j] = S[0][j-1]
#         # trace[0][j] = 'L'
# for i in range(1,n):
#     if X[i] == Y[0]:
#         S[i][0] = 1
#         #trace[i][0] = 'D'
#     else:
#         S[i][0] = S[i-1][0]

# for i in range(1,n):
#     for j in range(1,m):
#         #compute S[i][j]
#         if X[i] == Y[j]:
#             S[i][j] = S[i-1][j-1] + 1
#             #ttrace[i][j] = 'D' #diagonal element
#         else:
#             # if S[i-1] > S[i][j-1]:
#             #     S[i][j] = S[i-1][j-1]  + 1
#                 # trace[i][j] = 'L'
#             S[i][j] = max(S[i-1][j], S[i][j-1])
#             #trace[i][j] = 'L' #left element
# res = S[n-1][m-1]
"""
i = n - 1
j = m - 1
s = []
while i >= 0 and j >= 0:
    if trace[i][j] == 'D':
        #retrieve the element appearing in the LCS
        s.append(X[i]) 
        i = i - 1
        j = j - 1
    elif trace[i][j] == 'L':
        j -= 1
    else:
        i -= 1
s.reverse()"""
# print('result = ', res)    

#wirg trace
'''
import sys
def input():
    x = [int(x) for x in sys.stdin.readline().split()]
    y = [int(x) for x in sys.stdin.readline().split()]
    return x,y

x,y = input()
n = len(x)
m = len(y)
s = [[0 for i in range(m)] for j in range(n)]
trace = [[' ' for i in range(m)] for j in range(n)]


if x[0]==y[0]:
    s[0][0] = 1

for j in range(1,m):
    if x[0] == y[j]:
        s[0][j] = 1
        trace[0][j] = 'D'
    else:
        s[0][j] = s[0][j-1]
        trace[0][j] = 'L'

for i in range(1,n):
    if x[i] == y[0]:
        s[i][0] = 1
        trace[i][0] = 'D'
    else:
        s[i][0] = s[i-1][0]
        trace[i][0] = 'U'
for i in range(1,n):
    for j in range(1,m):
        if x[i] == y[j]:
            s[i][j] = s[i-1][j-1]+1
            trace[i][j] = 'D'
        else:
            # s[i][j] = max(s[i-1][j],s[i][j-1])
            if s[i-1][j]>s[i][j-1]:
                s[i][j] = s[i-1][j]
                trace[i][j] = 'U'
            else:
                s[i][j] = s[i][j-1]
                trace[i][j] = 'L'

        
res = s[n-1][m-1]
i = n-1
j = m-1
s = []
while i>=0 and j>=0:
    if trace[i][j] == 'D':
        s.append(x[i])
        i = i-1
        j = j-1
    elif trace[i][j] == 'L':
        j = j-1
    else:
        i = i-1
s.reverse()
print(s)
print(res)
'''

