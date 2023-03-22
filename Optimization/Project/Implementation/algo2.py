# Code của Quyên

# def solve_assignment_problem(N, K, d, t):
#     solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)

#     # Define variables
#     x = {}
#     y = {}
#     for k in range(1,K+1):
#         for i in range(N+1):
#             x[i, k] = solver.IntVar(0, 1, f"x_{i}_{k}")
#     for k in range(1,K + 1):
#         for j in range(N + 1):
#             for i in range(N + 1):
#                 if i != j:
#                     y[i, j, k] = solver.IntVar(0, 1, f"y_{i}_{j}_{k}")

#     z = solver.IntVar(0, solver.infinity(),'z')

#     # Constraints

#     for i in range(1, N+1):
#         solver.Add(solver.Sum([x[i, k] for k in range(1,K+1)]) == 1)

#     for k in range(1,K+1):
#         solver.Add(solver.Sum([y[i, 0, k] for i in range(1, N + 1)]) == 1)
#     for k in range(1,K+1):
#         solver.Add(solver.Sum([y[0, j, k] for j in range(1, N + 1)]) == 1)       

#     for k in range(1,K+1):
#         for i in range(1,N+1):
# #             if i!= j:
#             # solver.Add(solver.Sum([y[i,j,k] for i in range(1,N+1) for k in range(K)]) == x[i,k])
#                 solver.Add(solver.Sum([y[i,j,k] for j in range(1,N+1) if j != i]) == x[i,k])
#         for i in range(1,N+1):
# #             if i != j:
#             # solver.Add(solver.Sum([y[j,i,k] for i in range(1,N+1) for k in range(K)]) == x[i,k])
#                 solver.Add(solver.Sum([y[j,i,k] for j in range(1,N+1) if j != i]) == x[i,k])

#     demand_term = {}
#     traveling_term = {}
#     for k in range(1,K+1):
#         demand_term[k] = []
#         for i in range(N+1):
#             demand_term[k].append(d[i]*x[i,k])
#     for k in range(1,K+1):
#         traveling_term[k] = []
#         for i in range(N+1):
#             for j in range(N+1):
#                 if j != i:
#                     traveling_term[k].append(t[i][j]*y[i,j,k])

#     for k in range(1,K+1):
#         solver.Add(solver.Sum(demand_term[k]) + solver.Sum(traveling_term[k]) <= z)
        
#     # Add DFJ sub-tour elimination constraints
#     # SG = SubSetGenerator(N)
#     # S = SG.GenerateFirstSubset()
#     # while True:
#     #     if len(S)>= 2 and len(S) < N:
#     #         c = solver.Constraint(0, len(S))
#     #         for k in range(1,K+1):
#     #             for i in S:
#     #                 for j in S:
#     #                     if i != j:
#     #                         c.SetCoefficient(y[i,j,k], 1)
#     #     S = SG.GenerateNextSubset()
#     #     if S == None:
#     #         break

    
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             if i != j:
#                 s = solver.Sum([y[i, j, k] for k in range(1,K+1)])
#                 solver.Add(s >= 2)

#     solver.Minimize(z)
    
#     status = solver.Solve()
#     # if status == pywraplp.Solver.OPTIMAL:
#     #     return z.solution_value()
#     # else:
#     #     return None

#     # Solve and return the result
#     if status == pywraplp.Solver.OPTIMAL:
#         res = z.solution_value()
#     #     print("Assignment costs for each team:", res[0])
#         print("Minimal maximum cost:", res)
#         paths = {}
#         for k in range(1,K+1):
#             path = [0]
#             for i in range(1, N + 1):
#                 if x[i, k].solution_value() == 1:
#                     path.append(i)
#                 else:
#                     continue
#             path.append(0)
#             paths[k] = path
#         return paths
#     else:
#         return None

# print(solve_assignment_problem(N, K, d, t))
