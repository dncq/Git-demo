class Node:
    def __init__(self,id):
        self.id = id
        self.next = None #reference to the subsequent element is initialized by None

# nod = Node(10) # mod is the pointer to the block allocated
# print(nod.id) 

#--------------------------------------------------------------

def insertlast(v,f):
    # create a new node having identifier f
    # insert this node at the end of the linked list pointer by f
    # return the pointer to the resulting linked list 
    if f == None:
        f = Node(v)
        return f

    last = f
    while last.next != None:
        last = last.next
    # last points to the last element of the linked list
    q = Node(v) # allocate memory for the new node (element) 
    last.next = q
    return f # the first node (element) is not changed

# --------------------------------------------------------------

def insertRecursive(v,f):
    # use recursive way
    if f == None:
        f = Node(v)
        return f
# def insertBefore(v,u,f):
#     # f: the pointer to the first node of the linked list
#     # v: the value id of a new node
#     # g: the id a node before which the new node is inserted
      # special case 1: if the list is empty, then do nothing, return None  
#     if f == None:
#         return f
      # special case 2: the first node has id = u
#     
#     q = Node(v)
#     q.next = f
#     return q
      # general case: find a pointer (reference) to the node, such that p..next.id = u
#     p = f
#     while p.next != None:
#         if p.next.id == u:
#             break
#         p = p.next
#     if p.next != None:
#         q = Node(v)
#         q.next = p.next
#         p.next = q
#         return f
#     else:
#         return f

# --------------------------------------------------------------------

def insertBeforeRecursive(v,u,f):
    if f == None: # base case 1: the list is empty
        return None
    if f.id == u: # base case 2: the first node as id = u
        q = Node(v)
        q.next = f
        return q
    #recursive case: node has id = u is in the sub-list (or not exist)
    f.next = insertBeforeRecursive(v,u,f.next)
    return f

# --------------------------------------------------------------------

def remove(v, f):
    # f: pointer to the first node of the list
    # remove the element having the id = v from the list
    if f == None:
        return None
    if f.id == v:
        return f.next
    p = f
    while p.next != None:
        if p.next.id == v:
            break
        p = p.next
    if p.next != None: # found a node having id = v
        p.next = p.next.next
        return f
    else: # node having id = v does not exist in the given list        
        return f

# ---------------------------------------------------------------------

def removeRecursive(v, f):
    if f == None: # base case 1::empty list
        return None
    if f.id == v: # base case 2: remove the first node of the listt
        return f.next
    
    # Recursive case: the node having id = v is (if any) in the sub-list
    f.next = removeRecursive(v, f.next)
    return f

# -------------------------------------------------------------------
def find(u,f):
    # return the pointer to a node having id = u
    p = f
    while p != None:
        if p.id == u:
            return p
        # p = p.next
    return None

# -------------------------------------------------------------------

def insertAfter(v,u,f):
    # create a new node having id = v, insert this node after the node having id = u
    # f: the pointer (reference) to the first node of the list
    p = find(u,f) # find a pinter to a node having id = u
    if p == None:
        return 
    q = find(v,f) #find a node having id = v
    if q != None: #the node having id = v exists -> do not insert here
        return
    q = Node(v)
    q.next = p.next
    p.next = q
    return f

# ---------------------------------------------------------------------

def reverse(f):
    #reverse the list, return the pointer to the first node of the resulting list
    pp = None # previous node of p
    p = f
    np = None # next node of p
    while p != None:
        np = p.next 
        p.next = pp
        pp = p
        p = np
    return pp # point to the first element of the linked list

# ---------------------------------------------------------------------

def CountNode(f):
    # return the number of nodes of the list
    count = 1
    p = f #iterate over the elements of the list
    while p != None:
        count += 1
        p = p.next
    return count

#----------------------------------------------------------------------

def CountNodeRecursive(f):
    if f == None:
        return 0
    return 1 + CountNodeRecursive(f.next)

# ----------------------------------------------------------------------

def sum(f):
    # return the sum of ids of nodes of the list
    sum = 0
    p = f
    while p!= None:
        sum = sum + p.id
    return sum

# ----------------------------------------------------------------------

def sumRecursive(f):
    if f == None: #base case
        return 0
    return f.id  + sumRecursive(f.next)

# ----------------------------------------------------------------------

def printlist(f): # print the ids of all nodes (elements) of the list
                # f: pointer (reference) to the first element of the list
    
    p = f
    while p != None:
        print(p.id, end = " ")
        p = p.next
    print()


#MAIN   
first = None # pointer/reference to the first element of the linked list
             # first = insertlast(1, first)
             # first = insertlast(2, first)
             # first = insertlast(3, first)
             # first = insertlast(4, first)
for i in range(1,11):
    first = insertRecursive(i, first)
for i in range(4,100):
    first= insertlast(i, first)

printlist(first) 
# first = insertBefore(11,1000,first)
first = insertBeforeRecursive(11,1000,first)
first = remove(10, first)
first = removeRecursive(10, first)
printlist(first)
print('sum id =', sum(first))
first = insertAfter(8, 10, first)
printlist(first)

first = reverse(first)
printlist(first)
