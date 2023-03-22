import sys
from ortools.linear_solver import pywraplp

def input():
    [N] = [int(x) for x in sys.stdin.readline().split()]
    d = []
    d.append([])
    for i in range(N):
        r = [int(x) for x in sys.stdin.readline().split()]
        r.insert(0,0)
        d.append(r)
    return N, d

def CreateVariable(solver):
    # SECs: the set of sub-tours
    X = [[solver.IntVar(0,1,'X' + str(i) + ',' + str(j)+')') for j in range(N+1)] for i in range(N+1)]
    return X

# solver = pywraplp.Solver.CreateSolver('CBC')

def TSP_SEC(SECs):
    solver = pywraplp.Solver.CreateSolver('CBC')
    X = CreateVariable(solver)
    for i in range(1,N+1):
        c = solver.Constraint(1,1)
        for j in range(1,N+1):
            if i != j:
                c.SetCoefficient(X[i][j],1)
        c = solver.Constraint(1,1)
        for j in range(1,N+1):
            if i != j:
                c.SetCoefficient(X[j][i],1)
        
    for S in SECs:
        c = solver.Constraint(0,len(S)-1)
        for i in S:
            for j in S:
                if i!=j:
                    c.SetCoefficient(X[i][j],1)
    
    obj = solver.Objective()
    for i in range(1,N+1):
        for j in range(1,N+1):
            obj.SetCoefficient(X[i][j],d[i][j])

    res_stat = solver.Solve()
    if res_stat != pywraplp.Solver.OPTIMAL:
        print('cannot find optimal for sub-problem')
        return None
    else:
        print('optimal value sub-problem = ', solver.Objective().Value())
    
    s = [[X[i][j].solution_value() for i in range(N+1)] for j in range(N+1)]
    return s

def findnext(solution,current,cand):
    for i in cand:
        if solution[current][i] > 0:
            return i
    return -1 # not found

# def extractSolutionRoute(X,current):
#     route = []
#     route.append(current)

#     return route

def getfirst(S):
    for i in S:
        return i

def ExtractSubTour(solution):
    S = []
    # visited = [False for i in range(1,N+1)]
    cand = set()
    for i in range(1,N+1):
        cand.add(i)
    while len(cand)> 0:
        cur = getfirst(cand)
        T = []
        T.append(cur)
        cand.remove(cur)
        while True:
            next = findnext(solution,cur,cand)
            if next == -1 :
                break
            T.append(next)
            cand.remove(next)
            cur = next
        S.append(T)

    return S

def TSP():
    # solver = pywraplp.Solver.CreateSolver('CBC')
    SECs = []
    while True:
        solution = TSP_SEC(SECs)
        # S = ExtractSubTour(X)
        if solution == None:
            print('not feasible')
            break
        print('Found X')

        S = ExtractSubTour(solution)
        print(S)
        if S == None:
            print('found optimal solution')
            break
        for S1 in S:
            SECs.append(S1)

N,d = input()
TSP()

'''
    # allocating_cost = {} # có thể bỏ qua cái này
    # for i in other_customer:
    #     for m in seed_customer:
    #         allocating_cost[i,m] = min(c[0][i] + c[i][m] + c[m][0], c[0][m] + c[m][i]) + d[i] + d[m] 
    #         allocating_cost[i,m] = round(allocating_cost[i,m]*1000)
    # print(allocating_cost)
'''