# '''
# If-Then-Else expression
# if x[2] = 1 then x[4] != 2
# '''
# from ortools.sat.python import cp_model
# class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
#     #print intermediate solution
#     def __init__(self,variables):
#         cp_model.CpSolverSolutionCallback.__init__(self)
#         self.__variables = variables
#         self.__solution_count = 0
#     def on_solution_callback(self):
#         self.__solution_count += 1
#         for v in self.__variables:
#             print('%s = %i'% (v,self.Value(v)), end = ' ')
#         print()
#     def solution_count(self):
#         return self.__solution_count
# model = cp_model.CpModel()
# x = {}
# for i in range(5):
#     x[i] = model.NewIntVar(1,5,'x[' + str(i) + ']')
# c1 = model.Add(x[2] + 3 != x[1])
# c2 = model.Add(x[3] <= x[4])
# c3 = model.Add(x[2] + x[3] == x[0] + 1)
# c4 = model.Add(x[4] <= 3)
# c5 = model.Add(x[1] + x[4] == 7)
# b = model.NewBoolVar('b')
# #constraints
# model.Add(x[2] == 1).OnlyEnforceIf(b)
# model.Add(x[2] != 1).OnlyEnforceIf(b.Not())
# model.Add(x[4] != 2).OnlyEnforceIf(b)

# solver = cp_model.CpSolver()
# #Force the solver to follow the decision strategy exactly
# solver.parameters.search_branching = cp_model.FIXED_SEARCH
# vars = [x[i] for i in range(5)]
# solution_printer = VarArraySolutionPrinter(vars)
# solver.SearchForAllSolutions(model,solution_printer)

# from ortools.sat.python import cp_model
from ortools.linear_solver import pywraplp
import itertools
filename = r"C:\Users\DELL\OneDrive\Máy tính\Test data\N_5_K_2.txt"
def INP(filename):
    with open(filename) as f:
        T = []
        for eachline in f:
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
M = set(range(1,K+1))
B = set(range(1,N+ 2*K + 1))
B2 = set(itertools.product(B,B))
F1 = set([(i, k + N) for i in B for k in M])
F2 = set([(k + K + N, i) for i in B for k in M])
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
# MAIN
solver = pywraplp.Solver.CreateSolver('SCIP')

# Variables:
x = {}
for k in M:
    for (i,j) in A:
        x[k,i,j] = solver.IntVar(0,1,f'x_{k}_{i}_{j}')

y = {}
for k in M:
    for i in B:
        y[k,i] = solver.IntVar(0, solver.infinity(),f'y_{k}_{i}')
z = {}
for i in B:
    z[i] = solver.IntVar(1,K, f'z_{i}')
u = solver.IntVar(0, solver.infinity(),'u')
# Constraints

#1
for i in range(1,N+1):
    solver.Add(solver.Sum([x[k,i,j] for k in M for j in forward[i]]) == solver.Sum([x[k,j,i] for k in M for j in backward[i]]) == 1)

#2
for k in M:
    for i in range(1,N+1):
        solver.Add(solver.Sum([x[k,i,j] for j in forward[i]]) == solver.Sum([x[k,j,i] for j in backward[i]]))

#3
for k in M:
    solver.Add(solver.Sum([x[k,k+N,j] for j in range(1,N+1)]) == solver.Sum([x[k,j,k+K+N] for j in range(1,N+1)]) == 1)

#4
for k in M:
    for (i,j) in A:
        solver.Add(C*(1-x[k,i,j]) + z[i] >= z[j])
#5
for k in M:
    for (i,j) in A:
        solver.Add(C*(1-x[k,i,j]) + z[j] >= z[i])
#6
for k in M:
    for (i,j) in A:
        solver.Add(C*(1-x[k,i,j]) + z[i] >= z[j])
#7
for k in M:
    for (i,j) in A:
        solver.Add(C*(1-x[k,i,j]) + y[k,j] >= y[k,i] + d[j] + t[i][j])
#8
for k in M:
    for (i,j) in A:
        solver.Add(C*(1-x[k,i,j]) + y[k,i] + d[j] + t[i][j] >= y[k,j])
#9
for k in M:
    solver.Add(y[k,k+N] == 0)

#10
for k in M:
    solver.Add(z[k+N] == z[k+K+N] == k)
#11
for k in M:
    solver.Add(y[k,k+K+N] <= u)

#Objective:
solver.Minimize(u)

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print('Minimal maximum cost:',u.solution_value())
else:
    print('No solution')


# CP-SAT
'''
model = cp_model.CpModel()
x = []
for k in range(K):
    t = []
    for i in range(N+1):
        t.append(model.NewBoolVar(f'x[{k},{i}]'))
    x.append(t)
y = []
for k in range(K):
    t = []
    for i in range(N+1):
        d = []
        for j in range(N+1):
            d.append(model.NewBoolVar(f'y[{k},{i},{j}]'))
        t.append(d)
    y.append(t)
print(y)

z = model.NewIntVar(0, 100,'z')

# Each customer is assigned to only one employee
for i in range(1,N+1):
    model.AddExactlyOne(x[k][i] for k in range(K))

# Every employee should depart and return to the depot
for k in range(K):
    model.AddExactlyOne(y[k][0][j] for j in range(1,N+1))
for k in range(K):
    model.AddExactlyOne(y[k][i][0] for i in range(1,N+1))
# There is exactly one incoming and outcoming edge
for k in range(K):
    for i in range(1,N+1):
        model.Add(cp_model.LinearExpr.Sum([y[k][i][j] for j in range(1,N+1) if j != i]) == x[k][i])
        model.Add(cp_model.LinearExpr.Sum([y[k][j][i] for j in range(1,N+1) if j != i]) == x[k][i])

# Linearization
for k in range(K):
    model.Add(z >= cp_model.LinearExpr.Sum([x[k][i]*d[i] for i in range(N+1)]) 
                 + cp_model.LinearExpr.Sum([y[k][i][j]*t[i][j] for i in range(N+1) for j in range(N+1)]))

# Objective function
model.Minimize(z)

# SOLVE
solver = cp_model.CpSolver()
status = solver.Solve(model)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'Total cost = {solver.ObjectiveValue()}')
else:
    print('No solution found')
    '''

