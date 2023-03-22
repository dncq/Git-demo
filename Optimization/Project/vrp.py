'''from ortools.linear_solver import pywraplp

def solve_assignment_problem(N, K, d, t):
    solver = pywraplp.Solver('solve_assignment_problem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Xác định biến
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
    # Ràng buộc
    c = {}
    for k in range(K):
        c[k] = solver.IntVar(0, solver.infinity(), f"c_{k}")
    z = solver.IntVar(0, solver.infinity(),'z')

    # Constraint: The working time of each worker k
    for k in range(K):
        solver.Add(c[k] == solver.Sum([d[i-1]*x[i, k] for i in range(1,N+1)]) + solver.Sum([t[i][j]*y[i, j, k] for i in range(N + 1) for j in range(N + 1) if i != j]))
    
    # Constraint: Every customer should be served by only one worker k
    for i in range(1,N+1):
        solver.Add(solver.Sum([x[i,k] for k in range(K)]) == 1)

    # Constraint: All workers must depart and arrive at the depot
    solver.Add(solver.Sum([y[i,0,k] for i in range(1,N+1) for k in range(K)]) == K)
    solver.Add(solver.Sum([y[0,j,k] for j in range(1,N+1) for k in range(K)]) == K)

    # Constraint: Flow assignment constraint
    # solver.Add(solver.Sum([y[i,j,k] for i in range(1,N+1) for j in range(1,N+1) for k in range(K) if i!= j]) == x[i,k] for i in range(1,N+1) for k in range(K))
    # solver.Add(solver.Sum([y[j,i,k] for i in range(1,N+1) for j in range(1,N+1) for k in range(K) if i!= j]) == x[i,k] for i in range(1,N+1) for k in range(K))
    for k in range(K):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i!= j:
                # solver.Add(solver.Sum([y[i,j,k] for i in range(1,N+1) for k in range(K)]) == x[i,k])
                    solver.Add(solver.Sum([y[i,j,k]]) == x[i,k])
            for j in range(1,N+1):
                if i != j:
                # solver.Add(solver.Sum([y[j,i,k] for i in range(1,N+1) for k in range(K)]) == x[i,k])
                    solver.Add(solver.Sum([y[j,i,k]]) == x[i,k])
    # Constraint: Linearization of the objective function
    for k in range(K):
        solver.Add(z >= c[k])
    
    # Hàm mục tiêu
    solver.Minimize(z)

    # Tìm giải
    sol = solver.Solve()

    # Trả về kết quả
    if sol == pywraplp.Solver.OPTIMAL:
        return solver.Objective().Value()
    else:
        return None

# Ví dụ
N = 5
K = 2
d = [60, 80, 70, 10, 90]
t =  [[0, 50, 100, 60, 40, 80], 
      [50, 0 ,50, 40, 20, 60], 
      [100, 50, 0, 50, 70, 40], 
      [60, 40, 50, 0, 60, 20], 
      [40, 20, 70, 60, 0, 80], 
      [80, 60, 40, 20, 80, 0]] 

print(K)
print(solve_assignment_problem(N, K, d, t))



5 2
[[60, 80, 70, 10, 90], 
[0, 50, 100, 60, 40, 80], 
[50, 0 ,50, 40, 20, 60], 
[100, 50, 0, 50, 70, 40], 
[60, 40, 50, 0, 60, 20], 
[40, 20, 70, 60, 0, 80], 
[80, 60, 40, 20, 80, 0]] 


# '''
# from ortools.sat.python import cp_model

# def solve_mtsp(num_vehicles, nodes, distances):
#   model = cp_model.CpModel()
  
#   # Variables
#   start_vars = []
#   end_vars = []
#   for i in range(len(nodes)):
#     start_vars.append(model.NewIntVar(0, num_vehicles - 1, 'start_%i' % i))
#     end_vars.append(model.NewIntVar(0, num_vehicles - 1, 'end_%i' % i))
#   vehicle_vars = []
#   for i in range(len(nodes)):
#     vehicle_vars.append(model.NewIntVar(0, num_vehicles - 1, 'vehicle_%i' % i))
#   total_time = model.NewIntVar(0, int(1e10), 'total_time')
  
#   # Constraints
#   for i in range(len(nodes)):
#     model.Add(start_vars[i] == end_vars[i])
#     for j in range(i + 1, len(nodes)):
#       model.Add(vehicle_vars[i] != vehicle_vars[j]).OnlyEnforceIf(start_vars[i] == start_vars[j])
#       model.Add(vehicle_vars[i] != vehicle_vars[j]).OnlyEnforceIf(end_vars[i] == end_vars[j])
#   for i in range(len(nodes)):
#     for j in range(i + 1, len(nodes)):
#       model.Add(start_vars[i] <= end_vars[j]).OnlyEnforceIf(vehicle_vars[i] == vehicle_vars[j])
#       model.Add(start_vars[j] <= end_vars[i]).OnlyEnforceIf(vehicle_vars[i] == vehicle_vars[j])
#   for i in range(num_vehicles):
#     indices = [j for j in range(len(nodes)) if i == vehicle_vars[j]]
#     model.AddNoOverlap(start_vars[indices[0]], end_vars[indices[-1]], indices, vehicle_vars)
  
#   # Objective
#   obj_var = []
#   for i in range(len(nodes)):
#     for j in range(i + 1, len(nodes)):
#       if vehicle_vars[i] == vehicle_vars[j]:
#         obj_var.append(distances[i][j])
#   model.Minimize(model.Sum(obj_var))
  
#   # Solve
#   solver = cp_model.CpSolver()
#   solver.Solve(model)
  
#   # Result
#   result = []
#   for i in range(num_vehicles):
#     indices = [j for j in range(len(nodes)) if i == vehicle_vars[j].Value()]
#     result.append([nodes



from ortools.sat.python import cp_model

def mTSP_solver(num_vehicles, nodes, distances):
    model = cp_model.CpModel()
    num_nodes = len(nodes)

    # create variables
    start_variables = []
    end_variables = []
    transit_variables = []
    for i in range(num_vehicles):
        start_variables.append(model.NewIntVar(0, num_nodes - 1, 'start_%i' % i))
        end_variables.append(model.NewIntVar(0, num_nodes - 1, 'end_%i' % i))
        transit_variables.append([model.NewIntVar(0, 1, 'transit_%i_%i' % (i, j)) for j in range(num_nodes)])

    # create constraints
    # Each node can only be visited once
    for j in range(num_nodes):
        nodes_visited = [transit_variables[i][j] for i in range(num_vehicles)]
        model.Add(sum(nodes_visited) <= 1)

    # Start and end nodes must be different
    for i in range(num_vehicles):
        model.Add(start_variables[i] != end_variables[i])

    # Add transit constraints
    for i in range(num_vehicles):
        for j in range(num_nodes):
            for k in range(num_nodes):
                if j != k:
                    model.Add(transit_variables[i][j] + transit_variables[i][k] <= 1 + (start_variables[i] == j) +
                              (end_variables[i] == k))

    # Each vehicle must visit at least one node
    for i in range(num_vehicles):
        model.Add(sum(transit_variables[i]) >= 1)

    # Create a solver and solve
    solver = cp_model.CpSolver()
    solver.Solve(model)

    # Get the results
    for i in range(num_vehicles):
        print('Vehicle %i starts at node %i and ends at node %i' % (i, solver.Value(start_variables[i]), solver.Value(end_variables[i])))

        route = []
        for j in range(num_nodes):
            if solver.Value(transit_variables[i][j]) == 1:
                route.append(j)
        print('Route:', route)
