import sys
from ortools.linear_solver import pywraplp

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


def input():
    [N] = [int(x) for x in sys.stdin.readline().split()]
    d = []
    d.append([])
    for i in range(N):
        r = [int(x) for x in sys.stdin.readline().split()]
        r.insert(0,0)
        d.append(r)
    return N, d


N, d = input()
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         print(d[j][j], end = '')
#     print('')

solver = pywraplp.Solver.CreateSolver('CBC')
X = [[solver.IntVar(0,1,'X' + str(i) + ',' + str(j)+')') for j in range(N+1)] for i in range(N+1)]
print(X)
#flow balance constraint
for i in range(1, N+1):
    c = solver.Constraint(1,1)
    for j in range(1, N+1):
        if i != j:
            c.SetCoefficient(X[j][i], 1)
    c = solver.Constraint(1,1)
    for j in range(1, N+1):
        if j != i:
            c.SetCoefficient(X[i][j], 1)



# state SEC (Sub-Tour Elimination Constraint)
SG = SubSetGenerator(N)
S = SG.GenerateFirstSubset()
while True:
    if len(S)>= 2 and len(S) < N:
        c = solver.Constraint(0, len(S) - 1)
        for i in S:
            for j in S:
                if i != j:
                    c.SetCoefficient(X[i][j], 1)
    S = SG.GenerateNextSubset()
    if S == None:
        break

def findnext(current):
    for i in range(1, N+1):
        if X[current][i].solution_value() > 0:
            return i
    return -1 # not found

def extractSolutionRoute():
    route = []
    current = 1
    route.append(1)
    for i in range(2, N+1):
        nextPoint = findnext(current)
        route.append(nextPoint)
        current = nextPoint
    return route
#objective function

objective = solver.Objective()
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            objective.SetCoefficient(X[i][j], d[i][j])

#solver.SetMinimization()
result_status = solver.Solve()
# if result_status != pywraplp.Solver.OPTIMAL:
#     print('cannot find optimal solution')
# else:
#     print('optimal objective value = ', solver.Objective().Value())

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if X[i][j].solution_value()>0:
#             print('(',i,',',j,')')
route = extractSolutionRoute()
print('THe number of cities:',N)
print('The optimal route:')
route.append(1)
cost = 0
for i in route:
    print(i, end = ' ')
for i in range(N):
    cost += d[route[i]][route[i+1]]
print('\nOptimal cost:',cost)


'''
6
0 31 15 23 10 17
16 0 24 7 12 12
34 3 0 25 54 25
15 20 33 0 50 40
16 10 32 3 0 23
18 20 13 28 21 0


4 
0 3 2 4
1 0 5 3
2 3 0 7
1 1 3 0
'''

'''
import itertools

def subtourelim(model, where):
    if where == 'all':
        # Subtour elimination for all arcs
        arcs = [(i,j) for i in model.nodes for j in model.nodes if i != j]
    elif where == 'intra':
        # Subtour elimination for intra-route arcs only 
        arcs = [(i,j) for i in model.nodes for j in model.nodes if i != j and model.x[i,j] > 0.5]

    while True:

        # find an elementary subtour 
        tour = subtour(model) 

        if len(tour) < len(model.nodes):

            # add constraint : sum of arcs in subtour <= len(subtour)-1 
            expr = 0 
            for i,j in itertools.combinations(tour, 2): 
                expr += model.x[i,j] 

            model.cbLazy(expr <= len(tour)-1)

        else: 

            break 

    return model  

def subtour(model):  

     unvisited = list(model.nodes)  

     tour = [unvisited[0]]  

     while unvisited:  

         last = tour[-1]  

         neighbors = [i for i in unvisited if model.x[last,i] > 0.5 ]  

         if neighbors:  
             tour.append(neighbors[0])  
             unvisited.remove(neighbors[0])  
         else:  
             break  

     return tour
'''