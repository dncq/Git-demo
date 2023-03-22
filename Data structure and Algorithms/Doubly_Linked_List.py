class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None # pointer to the previous node of the current node
        self.next = None # pointer to the next node of the current node

def findFromLeft(u, first, last):
    p = first
    while p != None:
        if p.value == u:
            return p
        p = p.next
    return None
def printLeft2Right(first, last):
    p = first
    while p != None:
        print(p.value, end = ' ')
        p = p.next
    print()
def printRight2Left(first, last):
    p = last
    while p != None:
        print(p.value, end = ' ')
        p = p.prev
    print()
def insertBefore(v,u, first, last):
    # first and last are pointers to the fitst and last nodes of the current list
    # create a new node having value = v, insert this node before the node having value = u (first found when go from left to right)
    # return two pointers to the first and last nodes of the resulting list
    if first == None: #special case: the list is empty
        return first, last
    
    q = Node(v)
    p = findFromLeft(u, first, last)
    if p == None: # the node having the value u does not exist
        return first, last
    pp = p.prev
    if pp == None: #the node having value u is the first node of the list
        q.next = p
        first = q # the first node of the resulting list is the newly created node (node )
        return first, last
    q.prev = pp
    q.next = p
    pp.next = q
    p.prev = q
    return first, last # general case: node having the value u is located in the middle
                       # after the insertion, first and last do not change

first = Node(1)
last = first

first, last = insertBefore(2, 1, first, last)
first, last = insertBefore(3, 2, first, last)
first, last = insertBefore(4, 3, first, last)
printLeft2Right(first, last)
printRight2Left(first, last)