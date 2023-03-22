import sys 

class Node:
 def __init__(self, k):
  self.key = k
  self.leftChild = None 
  self.rightChild = None 

class BST:
 def __init__(self):
  self.root = None 
 
 #private function 
 def __Find__(self,k,r):
  if r == None:
   return None 
  if r.key == k:
   return r 
  if r.key < k:
   return self.__Find__(k,r.rightChild) 
  else:
   return self.__Find__(k,r.leftChild)
   
 #public function  
 def Find(self, k):
  return self.__Find__(k,self.root) 
   
 # private function  
 def __Insert__(self,k,r):
  if r == None:
   return Node(k) 
  if r.key < k:
   r.rightChild = self.__Insert__(k,r.rightChild)
  else:
   r.leftChild = self.__Insert__(k, r.leftChild) 
  return r
  
 def Insert(self, k):
  p = self.Find(k)
  if p != None:
   return 0 # key k exists, insert fail 
  self.root = self.__Insert__(k,self.root) 
  return 1
  
m = 100000
bst = [BST() for i in range(m)]

def h(k):
 # return the hashCode of the key k 
 code = 0
 for i in range(len(k)):
  code = code*256 + ord(k[i])
  code = code % m 
 return code 
 
 
def Find(k):
 idx = h(k) # hashCode -> specify the corresponding index 
 p = bst[idx].Find(k)
 if p != None:
  return 1 # FOUND
 return 0   #NOT FOUND 
 
def Insert(k):
 idx = h(k)
 res = bst[idx].Insert(k)
 return res 
 
def run(): 
 while True:
  line = [x for x in sys.stdin.readline().split()]
  if line[0] == '*':
   break
  Insert(line[0])
 
 while True:
  line = [x for x in sys.stdin.readline().split()]
  if line[0] == '***':
   break 
  if line[0] == 'find':
   res = Find(line[1])
   print(res)
  elif line[0] == 'insert':
   res = Insert(line[1])
   print(res)
   


run()
