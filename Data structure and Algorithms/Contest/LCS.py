import sys

def in_put():
    # a,b = input().split()
    X = [int(x) for x in sys.stdin.readline().split()]
    Y = [int(x) for x in sys.stdin.readline().split()]
    return X,Y
a,b = input().split()
X,Y = in_put()
n = len(X)
m = len(Y)
S = [[0 for j in range(m)] for i in range(n)]

if X[0] == Y[0]:
    S[0][0] = 1
for j in range(m):
    if X[0] == Y[j]:
        S[0][j] = 1

    else:
        S[0][j] = S[0][j-1]

for i in range(1,n):
    if X[i] == Y[0]:
        S[i][0] = 1

    else:
        S[i][0] = S[i-1][0]

for i in range(1,n):
    for j in range(1,m):

        if X[i] == Y[j]:
            S[i][j] = S[i-1][j-1] + 1

        else:
            S[i][j] = max(S[i-1][j], S[i][j-1])
res = S[n-1][m-1]
print(res)