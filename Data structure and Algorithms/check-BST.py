import sys
class Node:
    def __init__(self, k):
        self.key = k
        self.leftChild = None
        self.rightChild = None
     
def find(k, r):
    # return the pointer/reference to the node having key k
    if r == None:
        return None
    if r.key == k:
        return r
    p = find(k, r.leftChild)
    if p != None:
        return p
    return find(k, r.rightChild)
    
        
def addLeft(u,v,r):
    # create a node having key is u, add to the left-child position of the node having key v
    p = find(v,r)
    if p == None: # the node having key v does not exist 
        #print('addLeft: find(',v,' return None -> return')
        return   
    #print('funtion addLeft(',u,',',v,' found a node p key = ',p.key)    
    q = find(u,r)
    if q != None: # the node having key u exists, do not insert more 
        #print('addLeft: find(',u,' not None -> return')
        return     
    q = Node(u)
    if p.leftChild != None: # p already has left-child
        #print('addLeft: node ',p.key,' already has left-child -> return')
        return     
    p.leftChild = q
    
def addRight(u,v,r):
    p = find(v,r)
    if p == None:
        #print('addRight: find(',v,') return None -> return')
        return 
    q = find(u,r)
    if q != None: # the node having key u already exists, do not insert more 
        print('addRight: find(',u,') return not None -> return')
        return     
    q = Node(u)    
    if p.rightChild != None: # the node p already has right-child 
        #print('addRight: node ',p.key,' already has right-child -> return')
        return 
    p.rightChild = q

def checkBST(r):
    if r == None:
        return True, -10000000, 100000000, 0
    ok1,minK1,maxK1,sumK1 = checkBST(r.leftChild)
    ok2,minK2,maxK2,sumK2 = checkBST(r.rightChild)
    
    #print('checkBST(',r.key,'), left, ok1 = ',ok1,'minK1 = ',minK1,'maxK1 = ',maxK1,' sumK1 = ',sumK1)
    if ok1 == False:
        return False,0,0,(sumK1 + sumK2 + r.key)   
    if r.leftChild != None:
        if maxK1 > r.key:
            return False,0,0,(sumK1 + sumK2 + r.key)   
    else:
        minK1 = r.key 
        
    
    #print('checkBST(',r.key,'), right ok2 = ',ok2,'minK2 = ',minK2,'maxK2 = ',maxK2,'sumK2 = ',sumK2)
    if ok2 == False:
        return False,0,0,(sumK1 + sumK2 + r.key)   
    if r.rightChild != None:
        if minK2 < r.key:
            return False,0,0,(sumK1 + sumK2 + r.key)   
    else:
        maxK2 = r.key 
        
    #print('checkBST(',r.key,') return True, minK1 = ',minK1,'maxK2 = ',maxK2,'sumK1 = ',sumK1,' sumK2 = ',sumK2)
    
    return True,minK1,maxK2,(sumK1 + sumK2 + r.key)         
    
def inOrder(r):
    if r == None:
        return
    inOrder(r.leftChild)
    print(r.key, end = ' ')
    inOrder(r.rightChild)
    
r = None 
while True:
    line = sys.stdin.readline().split()
    if line[0] == '*':
        break
    #print(line)
    if line[0] == 'MakeRoot':
        r = Node(int(line[1]))
    elif line[0] == 'AddLeft':
        u = int(line[1])
        v = int(line[2])        
        addLeft(u,v,r)    
        #print('after addLeft',u,v)
        #inOrder(r)
    elif line[0] == 'AddRight':
        u = int(line[1])
        v = int(line[2])
        addRight(u,v,r)
        #print('after AddRight',u,v)
        #inOrder(r)
        
#inOrder(r)        
ok,minK,maxK,SumK = checkBST(r)
res = 1
if ok == True:
    res = 1
else:
    res = 0    
    
print(str(res) + ' ' + str(SumK))    