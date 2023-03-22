from ortools.linear_solver import pywraplp
import time
# MAIN
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
# d: thời gian bảo trì
# t: thời gian di chuyển giữa 2 địa điểm
N,K,d,t = INP(filename)
d.insert(0,0)

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


solver = pywraplp.Solver.CreateSolver('SCIP')
X = [[solver.IntVar(0,1,'X(' + str(i) + ',' + str(k)+')') 
        for k in range(K)] 
        for i in range(N+1)]

Y = [[[solver.IntVar(0,1,'X(' + str(i) + ',' + str(j) + str(k) +')') 
        for k in range(K)] 
        for j in range(N+1)]
        for i in range(N+1)]

c = [solver.IntVar(0, solver.infinity(), 'C(' + str(k) + ')') for k in range(1,K+1)]

z = solver.IntVar(0, solver.infinity(), 'z')

# Constraints
for k in range(K):
    solver.Add(c[k] == sum([d[i]*X[i][k] for i in range(N+1)]) + 
                       sum([t[i][j]*Y[i][j][k] for i in range(N+1) for j in range(N+1)]))

for i in range(1,N+1):
    solver.Add(sum([X[i][k] for k in range(K)]) == 1)

for k in range(K):
    solver.Add(sum([Y[0][j][k] for j in range(1,N+1)]) == 
               sum([Y[j][0][k] for j in range(1,N+1)]) == 1)

for k in range(K):
    for i in range(1,N+1):
        solver.Add(sum([Y[i][j][k] for j in range(1,N+1) if j != i]) ==
                   sum([Y[j][i][k] for j in range(1,N+1) if j != i]) == X[i][k])
                   
for k in range(K):
    solver.Add(z >= c[k])

solver.Minimize(z)
status = solver.Solve()
if status != pywraplp.Solver.OPTIMAL:
    print('No optimal solution')
else:
    print('Optimal objective value:', z.solution_value())