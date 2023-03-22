import sys
class Node:
    def __init__(self, id):
        self.id = id
        self.next = None

def find(v,f):
    if f == None:
        return False
    if f.id == v:
        return True

    p = f
    while p.id != v:
        if p.next == None:
            break
        p = p.next

    if p.id != v:
        return False
    return True

def addlast(v,f):
    if f == None:
        f = Node(v)
        return f
    if find(v,f):
        return f
    p = f
    while p.next != None:
        p = p.next
    
    k = Node(v)
    p.next = k
    
    return f


def addfirst(v,f):
    if f == None:
        return None
    if find(v,f):
        return f
    k = Node(v)
    k.next = f
    return k

def addafter(u,v,f):
    if f == None:
        return None
    if find(u,f):
        return f
    p = f
    while p.id != v:
        if p.next == None:
            break
        p = p.next
    
    if p.id != v:
        return f
    k = Node(u)
    k.next = p.next
    p.next = k

    return f

def addbefore(u,v,f):
    if f == None:
        return None
    if find(u,f):
        return f
    p = f # p is the pointer to the node before the node have id = v
    while p.next.id != v:
        if p.next == None:
            break
        p = p.next

    if p.next.id != v:
        return f
    k = Node(u)
    k.next = p.next
    p.next = k
    
    return f
def countNode(f):
    p = f
    count = 0
    while p != None:
        count += 1
        p = p.next
    return count
def sumNode(f):
    p = f
    sum = 0
    while p!= None:
        sum += p.id
        p = p.next
    return sum
def sumRecursive(f):
    if f == None:
        return 0
    return f.id + sumRecursive(f.next)

def remove(v,f):
    if f == None:
        return None
    if not find(v,f):
        return f
    if f.id == v:
        f = f.next

    p = f # p is the pointer to the node before the node having id = v
    while p.next != None:
        if p.next.id == v:
            break
        p = p.next
    if p.next != None:
        p.next = p.next.next
    return f

def reverse(f):
    np = None
    p = f
    pp = None
    while p != None:
        np = p.next
        p.next = pp
        
        pp = p
        p = np
    return pp

def printlist(f):
    p = f
    while p != None:
        print(p.id, end = ' ')
        p = p.next

# MAIN
first = None

def Input():
    n = int(input())
    s = [int(x) for x in sys.stdin.readline().split()]
    return [n, s]

[n, s] = Input()
for i in range(n):
    first = addlast(s[i], first)
while True:
    command = input().split()
    if '#' in command: break
    if 'addlast' in command:
        first = addlast(int(command[1]), first)
    if 'addfirst' in command:
        first = addfirst(int(command[1]), first)
    if 'addbefore' in command:
        first = addbefore(int(command[1]),int(command[2]), first)
    if 'addafter' in command:
        first = addafter(int(command[1]),int(command[2]), first)
    if 'remove' in command:
        first = remove(int(command[1]), first)
    if 'reverse' in command:
        first = reverse(first)
printlist(first)
print()





