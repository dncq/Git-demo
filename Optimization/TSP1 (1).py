from ortools.linear_solver import pywraplp
import sys
def input():
    [N] = [int(x) for x in sys.stdin.readline().split()]
    d = []
    d.append([])
    for i in range(N):
        r = [int(x) for x in sys.stdin.readline().split()]
        r.insert(0,0)
        d.append(r)
    return N, d

'''
def input():
    f = open("tsp_400.txt", "r")
    A = []
    for line in f:
        r = [int(x) for x in line.strip().split()]
        r.insert(0,0)
        A.append(r)
    [n] = [A[0][1]]
    A=[[]]+A[1:]
    
    f.close()
    return n, A
'''
def CreateVariables(solver):
    X = [[solver.IntVar(0,1,'X' + str(i) + ',' + str(j)+')') for j in range(N+1)] for i in range(N+1)]
    return X

def TSP_SEC(SECs):
    #SECs is the set of sub-tours
    solver=pywraplp.Solver.CreateSolver('CBC')
    X=CreateVariables(solver)
    for i in range(1,N+1):
        c=solver.Constraint(1,1)
        for j in range(1,N+1):
            if i !=j:
                c.SetCoefficient(X[j][i],1)
        c = solver.Constraint(1,1)
        for j in range(1, N+1):
            if j != i:
                c.SetCoefficient(X[i][j], 1)
    
    for S in SECs:
        c = solver.Constraint(0,len(S)-1)
        for i in S:
            for j in S:
                if i !=j:
                    c.SetCoefficient(X[j][i],1)
    
    obj = solver.Objective()
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                obj.SetCoefficient(X[i][j], d[i][j])
    
    res_start= solver.Solve()
    if res_start != pywraplp.Solver.OPTIMAL :
        print('Not found optimal')
        return None
    else :
        print('Optimal sub-tour', solver.Objective().Value())
        
    s = [[X[i][j].solution_value() for j in range(N+1)] for i in range(N+1)]
    return s

def findNext(X,current,cand):
    for i in cand:
        if X[current][i]>0:
            return i
    return -1#not found
def getFirst(S):
    for i in S:
        return i

def ExtractSubTour(solution):
    S=[]
    #visited=[False for i in range (1,N+1)]
    cand=set()
    for i in range(1,N+1):
        cand.add(i)
    while len(cand)>0:
         current = getFirst(cand)
         T=[]
         T.append(current)
         cand.remove(current)
         while True:
            next=findNext(solution,current,cand)
            #if next in T:
            if next==-1:
                break
            T.append(next)
            cand.remove(next)
            current=next
         #if len(T)== N:
            #return None# golbal tour
         S.append(T)
    return S
def TSP():
    SECs = []
    while True:
        solution = TSP_SEC(SECs)
        if solution == None:
            print('Not feasible')
            break
        S = ExtractSubTour(solution)
        print(S)
        print('number of subtour:', len(S))

        if len(S) == 1:
            print('found optimal solution')
            print('route =',S[0] +[1])
            break
        for Si in S:
            SECs.append(Si)
N,d=input()

TSP()
'''
10
0 2 2 7 5 7 4 10 8 9 
6 0 2 2 4 5 3 7 2 4 
4 2 0 1 5 8 2 9 3 1 
9 3 3 0 8 5 6 1 3 2 
7 2 1 2 0 5 8 9 5 1 
1 2 5 9 9 0 6 2 2 4 
3 7 2 4 1 6 0 6 6 6 
4 5 7 8 7 4 6 0 7 7 
6 1 2 8 1 7 9 9 0 9 
8 9 4 6 2 8 9 10 6 0
'''
