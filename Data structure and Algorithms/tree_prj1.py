class Node:
    def __init__(self, id):
        self.id = id
        self.leftmostchild = None
        self.rightsibling = None

def __InsertNode(r, v):
    if r == None:
        return None
    if r.leftmostchild == None:
        r.leftmostchild = Node(v)
        return r
    p = r.leftmostchild
    while p.rightsibling != None:
        p = p.rightsibling
    p.rightsibling = Node(v)

def find(u, r):
    if r == None:
        return None
    if r.id == u:
        return r
    p = r.leftmostchild
    while p != None:
        q = find(u, p)
        if q != None: # the node is found
            return q
        p = p.rightsibling
    return None # not found

def InsertNode(v, u):
    p = find(u,r)
    __InsertNode(p,v)

def preordertraversal(r):
    if r == None:
        return
    print(r.id, end = ' ')
    p = r.leftmostchild 
    while p != None:
        preordertraversal(p)
        p = p.rightsibling

def inorder(r):
    if r == None:
        return None
    p = r.leftmostchild
    inorder(p)
    print(r.id, end = ' ')
    if p != None:
        p = p.rightsibling
    while p!= None:
        inorder(p)
        p = p.rightsibling

def postorder(r):
    if r == None:
        return None
    p = r.leftmostchild
    while p!= None:
        postorder(p)
        p = p.rightsibling

    print(r.id, end = ' ')

command = []
while True:
    cmd = input()
    if cmd == "*":
        break
    command.append(cmd)
r = None
for cmd in command:
    if "MakeRoot" in cmd.split(" "):
        r = Node(int(cmd.split(" ")[1]))
    if "Insert" in cmd.split(" "):
        InsertNode(int(cmd.split(" ")[1]), int(cmd.split(" ")[2]))
    if "PreOrder" in cmd:
        preordertraversal(r)
        print()
    if "InOrder" in cmd:
        inorder(r)
        print()
    if "PostOrder" in cmd:
        postorder(r)
        print()
    # print(cmd.split())







"""
MakeRoot 10
Insert 11 10
Insert 1 10
Insert 3 10
InOrder
Insert 5 11
Insert 4 11
Insert 8 3
PreOrder
Insert 2 3
Insert 7 3
Insert 6 4
Insert 9 4
InOrder
PostOrder
*
"""
"""
MakeRoot 10
Insert 11 10
Insert 1 10
Insert 3 10
InOrder
Insert 5 11
Insert 4 11
Insert 8 3
PreOrder
Insert 2 3
Insert 7 3
Insert 6 4
Insert 9 4
InOrder 
PostOrder
*
"""