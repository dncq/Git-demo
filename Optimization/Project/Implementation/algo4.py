from ortools.sat.python import cp_model

def main():
  model = cp_model.CpModel()

  num_workers = 4
  num_tasks = 8

  # Variables
  workers = [model.NewIntVar(0, num_tasks - 1, 'worker_%i' % i) for i in range(num_workers)]
  assignments = [[model.NewBoolVar('assigned_%i_to_%i' % (j, i)) for j in range(num_tasks)] for i in range(num_workers)]

  # Constraints
  for i in range(num_workers):
    model.Add(sum(assignments[i][j] for j in range(num_tasks)) == 1)

  for j in range(num_tasks):
    model.Add(sum(assignments[i][j] for i in range(num_workers)) == 1)

  for i in range(num_workers):
    for j in range(num_tasks):
      model.Add(workers[i] >= j).OnlyEnforceIf(assignments[i][j])
      model.Add(workers[i] <= j).OnlyEnforceIf(assignments[i][j])

  # Objective
  objective = model.NewIntVar(0, num_tasks * num_workers, 'objective')
  model.AddMaxEquality(objective, [workers[i] + num_tasks * i for i in range(num_workers)])
  model.Minimize(objective)

  # Solve
  solver = cp_model.CpSolver()
  solver.Solve(model)

  # Print Solution
  for i in range(num_workers):
    for j in range(num_tasks):
      if solver.Value(assignments[i][j]):
        print("Worker", i, "is assigned to task", j)

# if __name__ == '_main_':
main()