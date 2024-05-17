import sys
def input():
    [n, m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for i in range(n+1)] #initialize a list of adjacent nodes of each other
    for i in range(m):
        [u,v] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append(v) # A[u] is the list of adjacent nodes of u
        A[v].append(u) # A[v] is the list of adjacent nodes of v
    return n, m, A

def DFS(u):
    # perform the DFS from the node u
    c[u] = nbCC # nbCC is the index of the last connected component being built
    for v in A[u]: # explore all adjacent nodes of u
        if c[v] ==-1: #the node v is not visited
            DFS(v)

def DFSGraph():
    global nbCC
    #perform the DFS on the given graph
    for v in range(1,n+1):
        c[v] = -1 # at the beginning. all the nodes are not visited
    for v in range(1,n+1):
        if c[v] == -1:
            #start to build a next connected component
            nbCC += 1
            DFS(v)

def printConnectedComponent():
    for k in range(1,nbCC+1):
        print('CC(',k,'): ', end = ' ')
        for v in range(1,n+1):
            if c[v] == k:
                print(v, end = ' ')
        print('')
        
n,m,A = input()
c = [-1 for v in range(n+1)]
nbCC = 0
DFSGraph()
printConnectedComponent()