import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def Find(v, f):
    if(f == None):
        return 0
    
    if(f.val == v): 
        return 1

    p = f
    while(p.val != v):
        if(p.next == None): 
            break
        p = p.next
    
    if(p.val != v): 
        return 0
    return 1
def addlast(v, f):
    if(f == None):
        f = Node(v)
        return f
    if(Find(v, f)): 
        return f
    p = f
    while(p.next != None):
        p = p.next
    u = Node(v)
    p.next = u

    return f

def addfirst(v, f):
    if(f == None):
        return None
    if (Find(v,f)):
        return f
    u = Node(v)

    u.next = f

    return u

def addafter(u, v, f):
    if(f == None):
        return None
    
    if(Find(u, f)): 
        return f
    if not (Find(v, f)): 
        return f
    # while(p.val != v):
    #     if(p.next == None): 
    #         break
    #     p = p.next
    

    # if(p.val != v): 
    #     return f
    p = f
    k = Node(u)

    k.next = p.next
    p.next = k

    return f

def addbefore(u, v, f):
    if(f == None):
        return None
    
    if(Find(u, f)): return f

    p = f

    while(p.next.val != v):
        if(p.next == None):
            break
        p = p.next
    
    if(p.next.val != v): 
        return f
    
    k = Node(u)

    k.next = p.next
    p.next = k

    return f

def remove(v, f):
    if(f == None):
        return None
    
    if(Find(v, f) == 0): 
        return f

    if(f.val == v):
        f = f.next

    p = f

    while(p.next != None):
        if(p.next.val == v): 
            break
        p = p.next

    if(p.next != None):
        p.next = p.next.next
        
    return f

def reverse(f):
    np = None
    p = f
    pp = None

    while(p != None):
        np = p.next
        p.next = pp
        pp = p
        p = np
    
    return pp

def printlist(f):

    if(f == None):
        return None

    p = f

    while(p != None): 
        print(p.val, end = " ")
        p = p.next
    print()

# MAIN
def INP():
    N = int(input())
    X = [int (x) for x in sys.stdin.readline().split()]

    return [N, X]

Linked_list = None

[N, X] = INP()

for i in range(N):
    Linked_list = addlast(X[i], Linked_list)


while(True):
    Ts = input().split()
    if( '#' in Ts): break
    if('addlast' in Ts): 
        Linked_list = addlast(int(Ts[1]), Linked_list)
    if( 'addfirst' in Ts): 
        Linked_list = addfirst(int(Ts[1]), Linked_list)
    if( 'addafter' in Ts): 
        Linked_list = addafter(int(Ts[1]), int(Ts[2]), Linked_list)
    if('addbefore' in Ts): 
        Linked_list = addbefore(int(Ts[1]), int(Ts[2]), Linked_list)
    if('remove' in Ts): 
        Linked_list = remove(int(Ts[1]), Linked_list)
    if('reverse' in Ts): 
        Linked_list = reverse(Linked_list)
printlist(Linked_list)