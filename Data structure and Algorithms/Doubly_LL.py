'''class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.prev = None
        self.next = None

# def remove(p,f,l):
#     if p == None:
#         return None
#     if f == l and p == f:
#         return None

#     if p == f:
#         f = p.next
#         f.prev = None 
    
#     if p == l:
#         l = p.prev
#         l.next = None
        
#     p.prev.next = p.next
#     p.next.prev = p.prev
class DLinked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def create(self,v):
        new_node = Node(v)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node
        

ddl = DLinked_List()
ddl.create([5,3,4])
print([node.val for node in ddl])'''

class Node(object):
    def __init__(self,value):
        self.prev = None
        self.next = None
        self.value = value

def findFromLeft(u,first,last):
    p = first
    while p != None:
        if p.value == u:
            return p
        p = p.next
    return None

def printLeft2Right(first,last):
    p = first
    while p != None:
        print(p.value,end=' ')
        p = p.next
    print()

def printRight2Left(first,last):
    p = last
    while p != None:
        print(p.value,end=' ')
        p = p.prev
    print()

def insertBefore(v,u,first,last):
    if first == None:
        return first,last
    q = Node(v)
    p = findFromLeft(u,first,last)
    pp = p.prev
    if pp == None:
        q.next = p
        first = q
        p.prev = q
        return first,last
    else:
        q.prev = pp
        q.next = p
        pp.next = q
        p.prev = q
        return first,last

def insert_first(u,first):
    p = first
    while p != None:
        if p.value == u:
            return p
        p = p.next
    return None
def insert_first(u,first,last):
    p = Node(u)
    if first == None and last == None:
        first = p
        last = p
        return first,last
    p.prev = last
    last.next = p
    last = p 
    return first,last
def remove_node(u,first,last):
    if first == None:
        return first,last
    p=first
    #p = findFromLeft(u,first,last)
    while p != None:
        if p.value == u:
            break
        p=p.next
    if p == None:
        return first,last
    pp=p.prev
    pn=p.next
    if pp == None:
        first =pn
    else:
        pp.next=pn
    if pn == None:
        last = pp
    else:
        pn.prev=pp
    return first,last
    # (5) 3 4 6 1
head=None
last=None
head,last = insert_first(1,head,last)
head,last = insert_first(3,head,last)
head,last = insert_first(5,head,last)
head,last = insertBefore(4,1,head,last)
head,last = insertBefore(6,1,head,last)
head,last = remove_node(5,head,last)
printLeft2Right(head,last)