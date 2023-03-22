from ortools.constraint_solver import pywrapcp
import sys


def INP():
    s = []
    for i in range(9):
        rows = [int(x) for x in sys.stdin.readline().split()]
        s.append(rows)
    return s

solver = pywrapcp.Solver('sudoku')
block_size = 3
line_size = block_size ** 2
line = range(0, line_size)
block = range(0, block_size)


initial_grid = INP()
grid = {}
for i in line:
    for j in line:
      grid[(i, j)] = solver.IntVar(1, line_size, 'grid %i %i' % (i, j))

  # AllDifferent on rows.
for i in line:
    solver.Add(solver.AllDifferent([grid[(i, j)] for j in line]))

  # AllDifferent on columns.
for j in line:
    solver.Add(solver.AllDifferent([grid[(i, j)] for i in line]))

  # AllDifferent on blocks.
for i in block:
    for j in block:
      one_block = []
      for di in block:
        for dj in block:
          one_block.append(grid[(i * block_size + di, j * block_size + dj)])

      solver.Add(solver.AllDifferent(one_block))

  # Initial values.
for i in line:
    for j in line:
      if initial_grid[i][j]:
        solver.Add(grid[(i, j)] == initial_grid[i][j])

all_vars = [grid[(i, j)] for i in line for j in line]

db = solver.Phase(all_vars,
                solver.INT_VAR_SIMPLE,
                solver.INT_VALUE_SIMPLE)

  # Solve.
solver.NewSearch(db)
count = 0 
while solver.NextSolution():
    for i in line:
        print ([int(grid[(i, j)].Value())for j in line])
        count += 1
    if count % 9 ==0:
        print('-------------------')
  
print ("Number of solutions:", solver.Solutions())






