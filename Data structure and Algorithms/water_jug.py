import sys
class State:
    def __init__(self,x,y,step, parent, action):
        self.x = x # amount in Jug 1
        self.y = y # amount in Jug 2
        self.step = step # number of steps for obtaining the current state from the initial state
        self.parent = parent
        self
def finalState(s):
    return s.x == c or s.y == c
def solve():
    Q = [] # initiate an empty queue
    s0 = State(0,0,0, None)
    Q.append(s0) # push the initial state into the queue Q
    visited = [[False for i in range(1000)] for j in range(1000)]
    # visited[x][y] = False means that state (x,y) is not visited
    # visited[x][y] = True measn that state (x,y) is visited
    visited[0][0] = True
    while len(Q) > 0:
        s = Q.pop(0) # pop an element out of the queue (in the front, index 0)
        # fill Jug 1
        ns = State(a, s.y, s.step + 1) # from current state s, generate the new state ns
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        # Fill Jug 2
        ns = State(s.x, b,s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        # Empty Jug 1
        ns = State(0, s.y, s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        # Empty Jug 2
        ns = State(s.x, 0 ,s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        # Pour Jug 1 to Jug 2
        if s.x + s.y <= b:
            ns = State(0, s.x + s.y, s.step + 1)
        else:
            ns = State(s.x + s.y - b, b, s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        # Pour Jug 2 to Jug 1
        if s.x + s.y <= a:
            ns = State( s.x + s.y, 0, s.step + 1)
        else:
            ns = State(a, s.x + s.y - a, s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
    return None # No solution found
def input():
    [a,b,c] = [int(x) for x in sys.stdin.readline().split()]
    return a,b,c
a, b, c = input()
s = solve()
if s == None:
    print('-1')
else:
    print(s.step)
    s = finalState()
    stack = []
    while s != None:
        stack.append(s)
        s = s.parent
    while len(stack) > 0:
        s = stack.pop()
        print(s.action, '{', s.x,',',s.y,']')