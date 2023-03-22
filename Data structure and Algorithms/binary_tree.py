class Node:
    def __init__(self,id):
        self.id = id
        self.leftchild = None
        self.rightchild = None
def find(u,r):
    # return a pointer to a node having id = u on the tree rooted at r
    if r == None:
        return None
    if r.id == u:
        return r
    p = find(u,r.leftchild) # explore the left sub_tree
    if p != None: # found a node having id = u
        return p

    return find(u,r.rightchild)
    
# def preOrder(r):
#     if r == None:
#         return 
#     print(r.id, end = ' ') # visit the root
#     preOrder(r.leftchild) # traverse the left sub_tree in a pre-order principle
#     preOrder(r.rightchild) # traverse the right sub_tree in a pre-order principle

# def inOrder(r):
#     if r == None:
#         return 
#     inOrder(r.leftchild) # traverse the left sub_tree in an in-order principle
#     print(r.id, end = ' ') # visit the root
#     inOrder(r.rightchild)# traverse the right sub_tree in an in-order principle

# def postOrder(r):
#     if r == None:
#         return 
#     postOrder(r.leftchild) # traverse the left sub_tree in a post-order principle
#     postOrder(r.rightchild) # traverse the right sub_tree in a post-order principle
#     print(r.id, end = ' ') # visit the root

def addleftchild(v,u):
    # create a new node having id = v 
    # make this new node as the left child of the node having id = u
    p = find(u,r)
    if p == None: # the node having id = u doea not exist
        return
    q = find(v,r)
    if q != None: # the node having id = v already exists
        return
    if p.leftchild != None:
        return
    k = Node(v)
    p.leftchild = k
    
    
def addrightchild(v,u):
    # create a new node having id = v
    # make this new node as the right child of the node having id = u
    p = find(u,r)
    if p == None: # the node having id = u does not exist
        return
    q = find(v,r)
    if q != None: # the node having id = v already exist
        return
    if p.rightchild != None: # the right child of p already exists
        return
    k = Node(v)
    p.rightchild = k
    # crate a new node having id = v
    # make this new node as the right child of the node having id = u
        
def cal(k,r,d):
    if r == None:
        return 0
    if r.id == k:
        return d
    d1 = cal(k,r.leftchild,d+1)
    if d1 > 0:
        return d1
    return cal(k,r.rightchild,d+1)

# def height(r):
#     # h = 0
#     # p = r.leftchild
#     # while p != None:
#     #     hp = height(p)
#     #     if h < hp:
#     #         h = hp
#     #     p = p.rightchild
    
#     # return h + 1
#     if r == None:
#         return 0
#     hl = height(r.leftchild)
#     hr = height(r.rightchild)
#     return max(hl,hr) + 1

# def countleaves(r):
#     if r == None:
#         return 0
#     if r.leftchild == None and r.rightchild == None:
#         return 1
#     return countleaves(r.leftchild) + countleaves(r.rightchild)
r = Node(6)
addleftchild(1,6)
addrightchild(9,6)

# addleftchild(4,5)
addrightchild(4,1)

addleftchild(7,9)
addrightchild(8,9)

addleftchild(2,4)
addrightchild(5,4)

addleftchild(3,8)
addrightchild(10,8)

# inOrder(r)
print()
# print('The number of leaf nodes = ',countleaves(r))
print(cal(5,r,1))