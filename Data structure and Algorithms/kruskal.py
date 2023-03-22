import sys
def inp():
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    E = []
    for i in range(m):
        [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
        E.append([u,v,w])
    return n,m,E

n,m,E = inp()

E = sorted(E,key = lambda x: x[2])

p = [0 for i in range(n+1)]
r = [0 for i in range(n+1)]

def FindSet(x):
    if x != p[x]:
        p[x] = FindSet(p[x])
    return p[x]

def Unify(x,y):
    if r[x] > r[y]:
        p[y] = x # make y the child of x
    else:
        p[x] = y # make x the child of y
        if r[x] == r[y]:
            r[y] = r[y]+1
        

def MakeSet(x):
    p[x] = x
    r[x] = 0

def print_disjoint_set():
    for i in range(1,n+1):
        print('p','[',str(i),'] =',str(p[i]),'r[',str(i),'] =',str(r[i]))



# for i in range(1,n+1):
#     MakeSet(1)
# print_disjoint_set()

# Unify(1,3)
# print('after unifying (1,3):')
# print_disjoint_set()

# Unify(3,6)
# print('after unifying (3,6):')
# print_disjoint_set()

def Kruskal():
    for v in range(1,n+1):
        MakeSet(v)
    T = []
    for [u,v,w] in E:
        ru = FindSet(u)
        rv = FindSet(v)
        if ru != rv:
            Unify(ru,rv)
            T.append([u,v,w])
            if len(T) == n-1:
                break
    return T
    # print_disjoint_set()
MST = Kruskal()
print('MST is:', MST)