from ortools.linear_solver import pywraplp
import itertools
# MAIN

# def get_plan(r0):
#   r = copy.copy(r0)
#   route = []
#   while len(r) != 0:
#     plan = [r[0]]
#     del (r[0])
#     l = 0
#     while len(plan) > l:
#       l = len(plan)
#       for i, j in enumerate(r):
#         if plan[-1][1] == j[0]:
#           plan.append(j)
#           del (r[i])
#       if plan not in route:
#         route.append(plan)
#   return(route)

class SubSetGenerator:
    def __init__(self, N):
        self.N = N
        self.x = [0 for i in range(N+1)]

    def __CollectSubset__(self):
        S = []
        for i in range(1, self.N + 1):
            if self.x[i] == 1:
                S.append(i)
        return S

    def GenerateFirstSubset(self):
        return self.__CollectSubset__()

    def GenerateNextSubset(self):
        N = self.N
        x = self.x
        i = N
        while i >= 1 and x[i] == 1:
            i = i-1
        if i == 0:
            return None

        x[i] = 1
        for j in range(i+1, N+1):
            x[j] = 0
        return self.__CollectSubset__()
    
filename = r"C:\Users\DELL\OneDrive\Máy tính\Test data\N_5_K_2.txt"
def INP(filename):
    with open(filename) as f:
        T = []
        for eachline in f:
            # line = map(int, eachline)
            T.append(eachline.split())
        N = int(T[0][0])
        K = int(T[0][1])
        d = [int(x) for x in T[1]]
        S = []
        for line in T[2:]:
            eachline = map(int, line)
            S.append(list(eachline))
        return N,K,d,S
# N: số lượng khách hàng
# K: số lượng nhân viên
# M: thời gian bảo trì
# S: thời gian di chuyển giữa 2 địa điểm
N,K,d,t = INP(filename)
d.insert(0,0)
for i in range(2*K):
    d.append(0)

for i in t:
    for k in range(2*K):
        i.append(i[0])
t.pop(0)
for i in t:
    i.pop(0)

for k in range(2*K):
    new = []
    for i in range(N+2*K):
        if i <= N-1:
            new.append(t[i][-1])
        else:
            new.append(0)
    t.append(new)
t.insert(0,[0 for i in range(N+2*K)])
for i in t:
    i.insert(0,0)

C = 1e5 + 7
P = set(range(1,K+1))
B = set(range(1,N+ 2*K + 1))
B2 = set(itertools.product(B,B))
F1 = set([(i, k + N) for i in B for k in P])
F2 = set([(k + K + N, i) for i in B for k in P])
F3 = set([(i,i) for i in B])

A = B2 - F1 - F2 - F3
# print(A)
forward = {}
backward = {}
for (i,j) in A:
    if i not in forward:
        forward[i] = [j]
    else:
        forward[i].append(j)
for i in forward:
    forward[i] = set(forward[i])
backward = {}
for (j,i) in A:
    if i not in backward:
        backward[i] = [j]
    else:
        backward[i].append(j)
for i in backward:
    backward[i] = set(backward[i])

M = 100000
# MAIN
solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)
# solver = pywraplp.Solver.CreateSolver('SCIP')

# Decision Varialbes
x = {}
y = {}
u = {}

for k in P:
    for (i,j) in A:
        x[i,j,k] = solver.IntVar(0,1,f'x_{i}_{j}_{k}')

for k in P:
    for i in B:
        y[i,k] = solver.IntVar(0,solver.infinity(),f'y_{i}_{k}')

z = solver.IntVar(0,solver.infinity(),'z')


for i in range(1,N+1):
    solver.Add(solver.Sum([x[i,j,k] for k in P for j in forward[i]]) == solver.Sum([x[j,i,k] for k in P for j in backward[i]]) == 1)

for k in P:
    for i in range(1,N+1):
        solver.Add(solver.Sum([x[i,j,k] for k in P for j in forward[i]]) == solver.Sum([x[j,i,k] for k in P for j in backward[i]]))

for k in P:
    solver.Add(solver.Sum([x[k+N,j,k] for j in range(1,N+1)]) == solver.Sum([x[j,k+K+N,k] for j in range(1,N+1)]))

for k in P:
    for (i,j) in A:
    # for i in range(1,N+1):
    #     for j in range(1,N+1):
            solver.Add(y[j,k] >= y[i,k] + d[j] + t[i][j] - M*(1-x[i,j,k]))

for k in P:
    for (i,j) in A:
            solver.Add(y[j,k] - M*(1-x[i,j,k]) <= y[i,k] + d[j] + t[i][j])
for k in P:
    solver.Add(y[k+N,k] == 0)
for k in P:
    solver.Add(y[k+K+N,k] <= z)
# for k in range(1,K+1):
#     for j in range(N+1):
#         for i in range(N+1):
#             x[i,j,k] = solver.IntVar(0,1,f'x_{i}_{j}_{k}')

# for k in range(1,K+1):
#     for i in range(N+1):
#         y[i,k] = solver.IntVar(0,solver.infinity(),f'y_{i}_{k}')

# for k in range(1,K+1):
#     for i in range(N+1):
#         u[i,k] = solver.IntVar(1,N,f'u_{i}_{k}')

# z = solver.IntVar(0,solver.infinity(),'z')


# # Constraints
# for k in range(1,K+1):
#     for i in range(1,N+1):
#         solver.Add(solver.Sum([x[i,j,k] for j in range(1,N+1)]) == 1)

# for k in range(1,K+1):
#     solver.Add(solver.Sum([x[0,j,k] for j in range(1,N+1)]) == 1)
# for k in range(1,K+1):
#     solver.Add(solver.Sum([x[i,0,k] for i in range(1,N+1)]) == 1)

# for k in range(1,K+1):
#     for i in range(N+1):
#         for j in range(N+1):
#             solver.Add(y[j,k] >= y[i,k] + d[i] + t[i][j] - M*(1 - x[i,j,k]))

# for k in range(1,K+1):
#     for i in range(N+1):
#         for j in range(N+1):
#             solver.Add(z >= y[i,k] + d[i] + t[i][j])

# # Ràng buộc về u

# for k in range(1,K+1):
#     solver.Add(u[0,k] == 0)

# # Sub-tour elimination
# for k in range(1,K+1):
#     for j in range(1,N+1):
#         for i in range(1,N+1):
#             solver.Add(u[i,k] - u[j,k] + C * x[i,j,k] <= M - 1)
# # Objective function
solver.Minimize(z)

status = solver.Solve()
if status != pywraplp.Solver.OPTIMAL:
    print('cannot find optimal solution')
else:
    print('optimal objective value = ', z.solution_value())
