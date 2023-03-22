'''from ortools.linear_solver import pywraplp

def solve_assignment_problem(N, K, d, t):
    solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Define variables
    x = {}
    y = {}
    for i in range(N + 1):
        for k in range(K):
            x[i, k] = solver.IntVar(0, 1, f"x_{i}_{k}")
    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(K):
                if i != j:
                    y[i, j, k] = solver.IntVar(0, 1, f"y_{i}_{j}_{k}")
    c = {}
    for k in range(K):
        c[k] = solver.IntVar(0, solver.infinity(), f"c_{k}")
    z = solver.IntVar(0, solver.infinity(),'z')

    # Constraints
    for k in range(K):
        solver.Add(c[k] == solver.Sum([d[i-1] * x[i, k] for i in range(1, N + 1)]) + solver.Sum([t[i][j] * y[i, j, k] for i in range(N + 1) for j in range(N + 1) if i != j]))
    for i in range(1, N + 1):
        solver.Add(solver.Sum([x[i, k] for k in range(K)]) == 1)
    solver.Add(solver.Sum([y[i, 0, k] for i in range(1, N + 1) for k in range(K)]) == K)
    solver.Add(solver.Sum([y[0, j, k] for j in range(1, N + 1) for k in range(K)]) == K)
    for k in range(K):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i != j:
                    solver.Add(y[i, j, k] <= x[i, k])
                    solver.Add(y[i, j, k] <= x[j, k])
                    solver.Add(y[i, j, k] >= x[i, k] + x[j, k] - 1)
    for k in range(K):
        solver.Add(c[k] <= z)

    # Add sub-tour elimination constraints
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                s = solver.Sum([y[i, j, k] for k in range(K)])
                solver.Add(s <= K - 1)

    solver.Minimize(z)
  # Solve and return the result
    if solver.Solve() == pywraplp.Solver.OPTIMAL:
        return [c[k].solution_value() for k in range(K)], z.solution_value()
    return None
N = 5
K = 2
d = [60, 80, 70, 10, 90]
t =  [[0, 50, 100, 60, 40, 80], 
      [50, 0 ,50, 40, 20, 60], 
      [100, 50, 0, 50, 70, 40], 
      [60, 40, 50, 0, 60, 20], 
      [40, 20, 70, 60, 0, 80], 
      [80, 60, 40, 20, 80, 0]] 

result = solve_assignment_problem(N, K, d, t)
if result is not None:
    print("Assignment costs for each team:", result[0])
    print("Minimum total cost:", result[1])
else:
    print("The problem could not be solved.")
print(N)
print(K)

print(solve_assignment_problem(N, K, d, t))'''

'''
from ortools.linear_solver import pywraplp

def solve_assignment_problem(N, K, d, t):
    solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Define variables
    x = {}
    y = {}
    for i in range(N + 1):
        for k in range(K):
            x[i, k] = solver.IntVar(0, 1, f"x_{i}_{k}")
    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(K):
                if i != j:
                    y[i, j, k] = solver.IntVar(0, 1, f"y_{i}_{j}_{k}")
    c = {}
    for k in range(K):
        c[k] = solver.IntVar(0, solver.infinity(), f"c_{k}")
    z = solver.IntVar(0, solver.infinity(),'z')

    # Constraints
    for k in range(K):
        solver.Add(c[k] == solver.Sum([d[i-1] * x[i, k] for i in range(1, N + 1)]) + solver.Sum([t[i][j] * y[i, j, k] for i in range(N + 1) for j in range(N + 1) if i != j]))
    for i in range(1, N + 1):
        solver.Add(solver.Sum([x[i, k] for k in range(K)]) == 1)
    solver.Add(solver.Sum([y[i, 0, k] for i in range(1, N + 1) for k in range(K)]) == K)
    solver.Add(solver.Sum([y[0, j, k] for j in range(1, N + 1) for k in range(K)]) == K)
    for k in range(K):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i != j:
                    solver.Add(y[i, j, k] <= x[i, k])
                    solver.Add(y[i, j, k] <= x[j, k])
                    solver.Add(y[i, j, k] >= x[i, k] + x[j, k] - 1)
    for k in range(K):
        solver.Add(c[k] <= z)

    # Add sub-tour elimination constraints
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                s = solver.Sum([y[i, j, k] for k in range(K)])
                solver.Add(s <= K - 1)

    solver.Minimize(z)
  # Solve and return the result
    if solver.Solve() == pywraplp.Solver.OPTIMAL:
#     return None
        paths = []
        for k in range(K):
            path = []
            for i in range(1, N + 1):
                if x[i, k].solution_value() == 1:
                    path.append(i)
                    for j in range(1, N + 1):
                        if y[i, j, k].solution_value() == 1 and i != j:
                            path.append(j)
                            break
            paths.append(path)
        return [c[k].solution_value() for k in range(K)], z.solution_value(), paths
    else: 
        return None
N = 5
K = 2
d = [60, 80, 70, 10, 90]
t =  [[0, 50, 100, 60, 40, 80], 
      [50, 0 ,50, 40, 20, 60], 
      [100, 50, 0, 50, 70, 40], 
      [60, 40, 50, 0, 60, 20], 
      [40, 20, 70, 60, 0, 80], 
      [80, 60, 40, 20, 80, 0]] 
print(solve_assignment_problem(N, K, d, t))'''
'''
from ortools.linear_solver import pywraplp

def solve_assignment_problem(N, K, d, t):
    solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Define variables
    x = {}
    y = {}
    for i in range(N + 1):
        for k in range(K):
            x[i, k] = solver.IntVar(0, 1, f"x_{i}_{k}")
    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(K):
                if i != j:
                    y[i, j, k] = solver.IntVar(0, 1, f"y_{i}_{j}_{k}")
    c = {}
    for k in range(K):
        c[k] = solver.IntVar(0, solver.infinity(), f"c_{k}")
    z = solver.IntVar(0, solver.infinity(),'z')

    # Constraints
    for k in range(K):
        solver.Add(c[k] == solver.Sum([d[i-1] * x[i, k] for i in range(1, N + 1)]) + solver.Sum([t[i][j] * y[i, j, k] for i in range(N + 1) for j in range(N + 1) if i != j]))
    for i in range(1, N + 1):
        solver.Add(solver.Sum([x[i, k] for k in range(K)]) == 1)
    solver.Add(solver.Sum([y[i, 0, k] for i in range(1, N + 1) for k in range(K)]) == K)
    solver.Add(solver.Sum([y[0, j, k] for j in range(1, N + 1) for k in range(K)]) == K)
    for k in range(K):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i != j:
                    solver.Add(y[i, j, k] <= x[i, k])
                    solver.Add(y[i, j, k] <= x[j, k])
                    solver.Add(y[i, j, k] >= x[i, k] + x[j, k] - 1)
    for k in range(K):
        solver.Add(c[k] <= z)

    # Add sub-tour elimination constraints
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                s = solver.Sum([y[i, j, k] for k in range(K)])
                solver.Add(s <= K - 1)

    solver.Minimize(z)
  # Solve and return the result
    if solver.Solve() == pywraplp.Solver.OPTIMAL:
        res = [c[k].solution_value() for k in range(K)], z.solution_value()
        print("Assignment costs for each team:", res[0])
        print("Minimum total cost:", res[1])

        for k in range(K):
            path = []
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if i!= j:
                        if y[i, j, k].solution_value() > 0:
                            path.append((i,j))
            print(f"Worker {k+1} path: {path}")
        return res
    else:
        print("The problem could not be solved.")
        return None
N = 5
K = 2
d = [60, 80, 70, 10, 90]
t =  [[0, 50, 100, 60, 40, 80], 
      [50, 0 ,50, 40, 20, 60], 
      [100, 50, 0, 50, 70, 40], 
      [60, 40, 50, 0, 60, 20], 
      [40, 20, 70, 60, 0, 80], 
      [80, 60, 40, 20, 80, 0]] 
print(solve_assignment_problem(N, K, d, t))
'''
from ortools.linear_solver import pywraplp

def solve_assignment_problem(N, K, d, t):
    solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # Define variables
    x = {}
    y = {}
    for i in range(N + 1):
        for k in range(K):
            x[i, k] = solver.IntVar(0, 1, f"x_{i}_{k}")
    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(K):
                if i != j:
                    y[i, j, k] = solver.IntVar(0, 1, f"y_{i}_{j}_{k}")
    c = {}
    for k in range(K):
        c[k] = solver.IntVar(0, solver.infinity(), f"c_{k}")
    z = solver.IntVar(0, solver.infinity(),'z')

    # Constraints
    for k in range(K):
        solver.Add(c[k] == solver.Sum([d[i] * x[i, k] for i in range(N + 1)]) + solver.Sum([t[i][j] * y[i, j, k] for i in range(N + 1) for j in range(N + 1) if i != j]))
    for i in range(1, N + 1):
        solver.Add(solver.Sum([x[i, k] for k in range(K)]) == 1)

    solver.Add(solver.Sum([y[i, 0, k] for i in range(1, N + 1) for k in range(K)]) == K)
    solver.Add(solver.Sum([y[0, j, k] for j in range(1, N + 1)  for k in range(K)]) == K)       
    
#     for k in range(K):
#         for i in range(1, N + 1):
#             for j in range(1, N + 1):
#                 if i != j:
#                     solver.Add(y[i, j, k] <= x[i, k])
#                     solver.Add(y[i, j, k] <= x[j, k])
#                     solver.Add(y[i, j, k] >= x[i, k] + x[j, k] - 1)

    # Constraint: Flow assignment constraint
    # solver.Add(solver.Sum([y[i,j,k] for i in range(1,N+1) for j in range(1,N+1) for k in range(K) if i!= j]) == x[i,k] for i in range(1,N+1) for k in range(K))
    # solver.Add(solver.Sum([y[j,i,k] for i in range(1,N+1) for j in range(1,N+1) for k in range(K) if i!= j]) == x[i,k] for i in range(1,N+1) for k in range(K))
    for k in range(K):
        for i in range(1,N+1):
#             if i!= j:
            # solver.Add(solver.Sum([y[i,j,k] for i in range(1,N+1) for k in range(K)]) == x[i,k])
                solver.Add(solver.Sum([y[i,j,k] for j in range(1,N+1) if j != i]) == x[i,k])
        for i in range(1,N+1):
#             if i != j:
            # solver.Add(solver.Sum([y[j,i,k] for i in range(1,N+1) for k in range(K)]) == x[i,k])
                solver.Add(solver.Sum([y[j,i,k] for j in range(1,N+1) if j != i]) == x[i,k])
                    
    for k in range(K):
        solver.Add(c[k] <= z)

    # Add DFJ sub-tour elimination constraints
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                s = solver.Sum([y[i, j, k] for k in range(K)])
                solver.Add(s <= K - 1)

    solver.Minimize(z)
  
  # Solve and return the result
    if solver.Solve() == pywraplp.Solver.OPTIMAL:
        res = [c[k].solution_value() for k in range(K)], z.solution_value()
        print("Assignment costs for each team:", res[0])
        print("Minimum total cost:", res[1])
        paths = []
        for k in range(K):
            path = []
            for i in range(1, N + 1):
                if x[i, k].solution_value() == 1:
                    path.append(i)
                else:
                    continue
            paths.append(path)
        return paths
    else:
        return None

# MAIN
filename = r"C:\Users\DELL\OneDrive\Máy tính\test_2.txt"
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
'''
N = 6
K = 2

d = [15, 30, 20, 30, 60, 45]
d.insert(0,0)
t =  [[0, 30, 54, 39, 48, 43, 20],
    [48, 0 ,23 ,40 ,32 ,44 ,60],
    [20, 20, 0 ,30 ,40 ,30 ,45],
    [30, 35, 40, 0 ,20 ,30 ,60],
    [20, 20, 30, 40, 0 ,50 ,10],
    [10 ,10 ,20 ,30 ,50 ,0 ,20],
    [50, 50, 10, 20, 30, 40, 0]]
'''
'''
N = 5
K = 2
d = [60, 80, 70, 10, 90]
d.insert(0,0)
t =  [[0, 50, 100, 60, 40, 80], 
      [50, 0 ,50, 40, 20, 60], 
      [100, 50, 0, 50, 70, 40], 
      [60, 40, 50, 0, 60, 20], 
      [40, 20, 70, 60, 0, 80], 
      [80, 60, 40, 20, 80, 0]] 
'''

paths= solve_assignment_problem(N, K, d, t)
print(paths)
