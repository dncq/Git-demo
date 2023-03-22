import sys 
import time
class PriorityQueue:  
 def __init__(self,max_size): 
  self.sz = max_size # elements of priority queue have id from 1, 2, . . ., sz
  self.n = 0 # size of heap 
  self.keys = [0 for i in range(self.sz+1)]
  self.nodes = [0 for i in range(self.sz+1)]
  self.idx = [-1 for i in range(self.sz+1)]
 def Swap(self,i,j):
  tmp = self.nodes[i]
  self.nodes[i] = self.nodes[j]
  self.nodes[j] = tmp 
  self.idx[self.nodes[i]] = i
  self.idx[self.nodes[j]] = j 
  
 def Size(self):
  return self.n 
  
 def UpHeap(self,i):
  if i == 0:
   return 
  while i > 0:
   pi = (i-1)//2;  # parent of i 
   if self.keys[self.nodes[i]] < self.keys[self.nodes[pi]]:
    self.Swap(i,pi)  
   else:
    break 
   i = pi 
   
 def DownHeap(self,i):
  L = 2*i + 1 # index of the left-child 
  R = 2*i+2 # index of the right child
  minIdx = i
  if L < self.n and self.keys[self.nodes[L]] < self.keys[self.nodes[minIdx]]:
   minIdx = L
  if R < self.n and self.keys[self.nodes[R]] < self.keys[self.nodes[minIdx]]: 
   minIdx = R 
  if minIdx != i: 
   self.Swap(i,minIdx)
   self.DownHeap(minIdx) 
   
 def Insert(self, v, k):
  self.keys[v] = k 
  self.nodes[self.n] = v 
  self.idx[self.nodes[self.n]] = self.n 
  self.UpHeap(self.n) 
  self.n = self.n + 1
  
 def InHeap(self,v):
  return self.idx[v] >= 0 
 
 def UpdateKey(self, v, k):
  if self.keys[v] > k:
   self.keys[v] = k
   self.UpHeap(self.idx[v])  
  else:
   self.keys[v] = k
   self.DownHeap(self.idx[v])

 def DeleteMin(self):
  sel_node = self.nodes[0] # element at the root is the element having minimum key
  self.Swap(0,self.n-1)
  self.n = self.n - 1  
  self.DownHeap(0) # recover the min-heap property 
  self.idx[sel_node] = -1 # the sel_node is no longer belong to the prioriry queue (min-heap)
  return sel_node 
  
 def getKey(self,v):
  return self.keys[v]
  
 def Print(self): # print the information about the priority queue 
  for i in range(self.n):
   e = self.nodes[i]
   print('[',e,'idx',self.idx[e],',k',self.keys[e],'] ',end = ' ')
  print('') 
  
def Input():
 [n,m] = [int(x) for x in sys.stdin.readline().split()]
 A = [[] for v in range(n+1)]
 for i in range(m):
  [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
  A[u].append([v,w])
 
 [s,t] = [int(x) for x in sys.stdin.readline().split()] 
 
 return n,m,A,s,t 

def DijkstraPriorityQueue(n,m,A,s,t):
 pq = PriorityQueue(n)
 pq.Insert(s,0)
 while pq.Size() > 0:
  u = pq.DeleteMin()
  if u == t:
   break
  du = pq.getKey(u)
  #print('Pop u = ',u,' du = ',du)
  for [v,w] in A[u]: # explore the adjacent arcs of u -> update keys
   dv = du + w 
   if pq.InHeap(v) == False: # the node v is not in the priority queue (min-heap)
    #print('Insert(',v,dv,')')
    pq.Insert(v,dv) # insert node v and its key dv to priority queue 
    #print('After insert, Heap = ')
    #pq.Print()
   else:
    #print('from u = ',u,' consider v = ',v,' key = ',v,' dv = ',dv)
    if pq.getKey(v) > dv: # the current key d[v] is greater than new path length from s - t 
     pq.UpdateKey(v,dv)   # take the new path  
     #print('After Update(',v,dv,') Heap = ')
     #pq.Print()
 print(pq.getKey(t)) # print the length of the shortest path from s to t 
 
n,m,A,s,t = Input()
start_time = time.time()
#Dijkstra(n,m,A,s,t)
DijkstraPriorityQueue(n,m,A,s,t)
print('time = ',time.time() - start_time)
'''  
pq = PriorityQueue(10)
pq.Insert(9,90)
pq.Insert(1,10)
pq.Insert(2,20)
pq.Insert(5,50)
pq.Insert(4,40)  

while pq.Size() > 0:
 e = pq.DeleteMin()
 print('pop ',e,pq.getKey(e))

'''