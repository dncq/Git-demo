# n = 6
# a = [0,2,5,3,1,9,8]
# x = [0,0,0,0,0,0,0]
# m = 0
# def Try(k):
#     global m
#     for v in range(x[k-1] +1,n+1):
#         if a[v] > a[x[k-1]]:
#             x[k] = v
#             # print('value=',v)
#             if m < k: 
#                 m = k
#             if k < n: 
#                 Try(k+1)
# Try(1)
# print(m)


# def f(a,i,j):
#     if i > j:
#         return 0
#     if i == j:
#         return a[i]
#     m = (i+j)//2
#     t1 = f(a,i,m)
#     t2 = f(a,m+1,j)
#     if t1>t2:
#         return t1
#     else:
#         return t2
# a = [2,4,7,9,5]
# print(f(a,0,4))

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
    # if(Find(v, f)): 
    #     return f
    p = f
    while(p.next != None):
        p = p.next
    u = Node(v)
    p.next = u

    return f

def proc(v,f):
    if f == None:
        return None
    if f.val == v:
        tm = f
        f = f.next
        return f
    f.next = proc(v,f.next)
    return f

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
    X = [int (x) for x in sys.stdin.readline().split()]

    return  X

Linked_list = None

X= INP()

for i in X:
    Linked_list = addlast(i, Linked_list)

printlist(Linked_list)

proc(2,Linked_list)

printlist(Linked_list)
