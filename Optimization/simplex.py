from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')
INF = solver.infinity()
# print(INF)

x1 = solver.IntVar(0,INF,'x[1]')
x2 = solver.IntVar(0,INF,'x[2]')
x3 = solver.IntVar(0,INF,'x[3]')
x4 = solver.IntVar(0,INF,'x[4]')
x5 = solver.IntVar(0,INF,'x[5]')
x6 = solver.IntVar(0,INF,'x[6]')
x7 = solver.IntVar(0,INF,'x[7]')
x8 = solver.IntVar(0,INF,'x[8]')

solver.Add(2*x1 + x2 + x3 == 8)
solver.Add(3*x1 + 4*x2 + x4 == 24)
solver.Add(x1 - x2 + x5 == 2)
solver.Add(0.8*x3 + 0.8*x4 - x6 == 0.6)
solver.Add(0.4*x3 + 0.4*x4 - x7 == 0.8)
solver.Add(0.6*x3 + 0.6*x4 - x8 == 0.2)
# solver.Add(x1-5*x2+x3<=15)
# solver.Add(3*x1+2*x2-2*x3<=20)
# solver.Add(4*x1+x3<=10)

solver.Maximize(x1 + x2)

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print('Solution: ', end = '')
    print(solver.Objective().Value())
    print(x1.solution_value())
    print(x2.solution_value())
    print(x3.solution_value())
    print(x4.solution_value())
    print(x5.solution_value())
    print(x6.solution_value())
    print(x7.solution_value())
    print(x8.solution_value())
