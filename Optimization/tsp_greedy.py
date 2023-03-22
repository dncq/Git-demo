import sys

# Greedy nearest neighbor
def INP(filename):
    with open(filename,'w') as f:

        [n] = [int(x) for x in sys.stdin.readline().split()]
        A = []
        for i in range(n):
            r = [int(x) for x in sys.stdin.readline().split()]
            A.append(r)
        for line in A:
            row = ''
            for j in range(len(line)):
                row = row + str(line[j]) + ' '
            f.write(line + '\n')
    return n,A

def writesolution(n,S,filename):
    with open(filename,'w') as f:
        f.write(str(n) + '\n')
        s = ''
        for i in S:
            s = s + str(i) + ' '
        f.write(s)

def select(C, lastPoint):
    minD = 1e9
    sel = 0
    for i in C:
        if A[lastPoint][i] < minD:
            minD = A[lastPoint][i]
            sel = i
    return sel

def greedy(s): # s is the starting point of the nearest neighbor greedy algorithm
    last = s
    S = [s]
    C = set()
    for i in range(n):
        if i!= s:
            C.add(i)
    while len(C) > 0:
        e = select(C,last)
        C.remove(e)
        S.append(e)
    return S

n,A = INP('1000.txt')
sol = greedy(1)
# print(n)
# for i in sol:
#     print(i+1, end = ' ')
writesolution(n,sol,'sol-1000.txt')
#