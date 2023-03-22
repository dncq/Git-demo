class Node:
    def __init__(self, id):
        self.id = id
        self.leftmostchild = None
        self.rightsibling = None

def __InsertNode(r, v):
    '''
    r is a pointer (reference) to some node of the tree
    create a node having id = v
    insert this newly created node at the end of the children list of r
    '''
    if r == None:
        return None
    # r.leftmostchild is the pointer reference to the first element of the linked
    # list of children of r
    if r.leftmostchild == None:
        r.leftmostchild = Node(v)
        return r
    p = r.leftmostchild
    while p.rightsibling != None:
        p = p.rightsibling
    p.rightsibling = Node(v)

def find(u, r):
    #find and return a node having id = u on the tree rooted at r
    # E.g. apply pre-order traversal on the tree for searching
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
    ''' u is the id of some node of the tree 
    create a new node having id = v
    insert this node at the end of the node having id = u '''
    p = find(u,r)
    __InsertNode(p,v)

def printTree(r):
    if r == None:
        return
    #print the id of f, follows by the list of children of r
    print(r.id, end = ': ')
    p = r.leftmostchild
    while p != None:
        print(p.id, end = " ")
        p = p.rightsibling
    print('')
    #call recursive for printing the sub
    p = r.leftmostchild
    while p != None:
        printTree(p)
        p = p.rightsibling
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

def height(r):
    # r: the pointer to the root of the tree
    # compute the height of a node in the tree
    # height of a node is defined to be the length of the longest path from that node to some key node + 1
    ''' height(r)
            rs = max(height (r1),height(r2),...,height(rn) + 1)
            h = 0
            p = r.leftMostSibling
            while p != NULL do:
                hp = height(p)
                k = max(k,hp)
                p = p.rightSibling
    
            '''
    h = 0
    p = r.leftmostchild
    while p!= None:
        hp = height(p)
        if h < hp:
            h = hp
        p = p.rightsibling

    return h + 1

def countNode(r):
    # r is the pointer to the root of the tree
    # compute and return the number of nodes of the tree
    if r == None:
        return 0
    res = 1
    p = r.leftmostchild
    while p != None:
        res += countNode(p)
        p = p.rightsibling
    
    return res

def countleaves(r):
    # r is the pointer to the root node
    # compute and return the number of leaf nodes of the tree
    
    if r == None:
        return 0
    res = 0
    p = r.leftmostchild
    if p == None: # r does not have any children, it is a leaf node
        return 1
    while p != None:
        res += countleaves(p)
        p = p.rightsibling
    return res
def sub_depth(v,p,d):
    # p is a pointer to the root of the tree
    # d: the depth of p on the original tree
    # return the depth of v in the tree rooted at p
    # return -1 if the node having id = v isn't in the tree
    if p == None:
        return -1
    if p.id == v:
        return 0
    q = p.leftmostchild
    while q != None:
        if q.id == v:
            # print('from', p.id,' reach q = ',q.id,'return 1')
            return 1
        a = sub_depth(v,q,d+1) # compute the depth of v on the sub_tree rooted at q
        if a > -1: # find a node having id = v on the tree rooted at q
            # print('from', p.id,'found on tree rooted at', q.id,'')
            return a + 1
        q = q.rightsibling # continue the search on the next child
    return -1
    
def depth(v):
    # compute the depth of the node having id = v
    ''' depth(v,p,d):
            if p == NULL then:
                return -1; // v does not belong to tree rooted at p
            for q in children(p) do:
                if q.id == v then:
                    return d + 1
                a = depth(v,q,d+1)
                if a != -1 then
                    return a + d
                return -1 // not found'''
    return sub_depth(v,r,1) + 1
r = Node(10)
InsertNode(11,10)
InsertNode(1,10)
InsertNode(3, 10)

InsertNode(5,11)
InsertNode(4,11)

InsertNode(8,3)
InsertNode(2,3)
InsertNode(7,3)

InsertNode(6,4)
InsertNode(9,4)
print('Each sub-tree is: ')
printTree(r)
print('Pre-order traversak: ')
preordertraversal(r)
print()
print('In-order traversak: ')
inorder(r)
print()
print('Post-order traversak: ')
postorder(r)
print()
print('Height of the root node:', height(r))
print('Number of nodes in the tree:', countNode(r))
print('Number of leaf node in the tree:', countleaves(r))
v= 10
print('Depth of the node:', depth(v))