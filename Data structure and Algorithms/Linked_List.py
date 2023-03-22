class Node:
    def __init__(self,id):
        self.id = id
        self.next = None #reference to the subsequent element is initialized by None


# nod = Node(10) # nod is the pointer to the block allocated
# print(nod.id) 

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
def insertRecursive(v,f):
    # use recursive way
    if f == None:
        f = Node(v)
        return f
 
def printlist(f): # print the ids of all nodes (elements) of the list
                # f: pointer (reference) to the first element of the list
    p = f
    while p != None:
        print(p.id, end = " ")
        p = p.next

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