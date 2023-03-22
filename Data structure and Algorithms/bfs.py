FirstLine = [int(x) for x in input().split()]
n = FirstLine[0]
m = FirstLine[1]
# print(n,m)
A = [[] for i in range(n+1)] # AdjacentList
for i in range(m):
    [u,v] = [int(x) for x in input().split()]
    A[u].append(v)
    A[v].append(u)

# for i in range(1,n+1):
#     print('A[{}]'.format(i),'=',A[i])

def BFS(u):
    Q = []
    Q.append(u)
    level[u] = 0
    while len(Q)>0:
        v = Q.pop(0)
        for x in A[v]:
            if level[x] == -1:
                level[x] = level[v]+1
                Q.append(x)

def BFSGraph():
    for v in range(1,n+1):
        level[v] = -1
    for v in range(1,n+1):
        if level[v] == -1:
            BFS(v)


level = [-1 for v in range(n+1)]
BFSGraph()
for v in range(1,n+1):
    print('Level of {}'.format(v),'=',level[v])