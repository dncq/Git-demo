# Queue Simulation
'''class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def isempty(self):
        if self.head == None and self.tail == None:
            return 1
        return 0

    def push(self,s):
        p = Node(s)
        if self.tail == None:
            self.head = p
            self.tail = p
            return
        self.tail.next = p
        self.tail = p
        
    def pop(self):
        if self.isempty():
            return 'NULL'
        poppedvalue = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        poppedvalue.next = None
        return poppedvalue.val

    def printqueue(self):
        curr = self.head
        while curr != None:
            print(curr.val, end = ' ')
            curr = curr.next
q = Queue()
res = []
while True:
    cmd = input().split()
    if '#' in cmd: break
    if 'PUSH' in cmd:
        q.push(int(cmd[1]))
    if 'POP' in cmd:
        res.append(q.pop())
for i in res:
    print(i)'''

# -------------------------------------------------------
# WATER JUGS
'''import sys
class State:
    def __init__(self,x,y,step) -> None:
        self.x = x # amount in Jug 1
        self.y = y # amount in Jug 2
        self.step = step # number of steps for obtaining the current state from the initial state
def finalState(s):
    return s.x == c or s.y == c or s.x + s.y == c
def solve():
    Q = [] # initialize an empty queue
    s0 = State(0,0,0)
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
def Input():
    [a,b,c] = [int(x) for x in sys.stdin.readline().split()]
    return a,b,c
a, b, c = Input()
s = solve()
if s == None:
    print('-1')
else:
    print(s.step)'''

