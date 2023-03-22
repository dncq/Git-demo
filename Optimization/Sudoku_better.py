from VarIntLS import VarIntLS
from LocalSearchManager import LocalSearchManager
from NotEqual import NotEqual
from ConstraintSystem import ConstraintSystem
import random as rd

def printSolution():
 for i in range(9):
  for j in range(9):
   print(x[i][j].getValue(), end = ' ')
  print('')
  
mgr = LocalSearchManager()
# define decision variables
x = [[VarIntLS(mgr,1,9,i+1,'x[' + str(i) + ',' + str(j) + ']') for i in range(9)] for j in range(9)]

#state constraints
constraints = []
# contraint on rows
for i in range(9):
 for j1 in range(8):
  for j2 in range(j1+1,9):
   c = NotEqual(x[i][j1],x[i][j2],'NotEqual')
   constraints.append(c)
            
# contraint on columns
for j in range(9):
 for i1 in range(8):
  for i2 in range(i1+1,9):
   c = NotEqual(x[i1][j],x[i2][j],'NotEqual')
   constraints.append(c)

# constraint on sub-squares
for I in range(3):
 for J in range(3):
  for i1 in range(3):
   for j1 in range(3):
    for i2 in range(3):
     for j2 in range(3):
      if i1 < i2 or i1 == i2 and j1 < j2:
       c = NotEqual(x[3*I+i1][3*J+j1], x[3*I+i2][3*J+j2],'NotEqual')
       constraints.append(c)

C = ConstraintSystem(constraints)

mgr.close() # close the model, init data structures representing relation between components of the model

# perform local search (hill climbing)
# make use of C.getAssignDelta, C.getSwapDelta for neighborhood query
def simpleHillClimbing(maxIters):
 
 
 # explore all possible assignment (x[i][j] <- v)
 for it in range(maxIters):
  # explore neighborhood for finding the best neighboring solution
  minDelta = 1e9
  select_i = -1 
  select_j = -1 
  select_value = -1
  candidates = []
  for i in range(9):
   for j in range(9):
    for v in range(1,10):
     delta = C.getAssignDelta(x[i][j],v)
     if delta < minDelta:
      minDelta = delta
      candidates = []
      candidates.append([i,j,v])
     elif delta == minDelta:
      candidates.append([i,j,v])
      
  # select randomly an element from candidates    
  idx = rd.randint(0,len(candidates)-1)
  select_i = candidates[idx][0]
  select_j = candidates[idx][1]
  select_value = candidates[idx][2]
  
  #  perform the selected local move 
  x[select_i][select_j].setValuePropagate(select_value)
  print('step ',it,' x[',select_i,',',select_j,'] = ',select_value,' violations = ',C.violations())
  
def improvedHillClimbing(maxIters):
 # explore neighborhood by swapping 2 variables on the same row
 for it in range(maxIters):
  candidates = [] 
  minDelta = 1e9
  for i in range(9):
   for j1 in range(8):
    for j2 in range(j1+1,9):
      delta = C.getSwapDelta(x[i][j1],x[i][j2])
      if delta < minDelta:
       minDelta = delta
       candidates = []
       candidates.append([i,j1,j2])
      elif delta == minDelta:
       candidates.append([i,j1,j2])      
  
  # select randomly an elment from candidates
  idx = rd.randint(0,len(candidates)-1)
  i = candidates[idx][0]
  j1 = candidates[idx][1]
  j2 = candidates[idx][2]
  x[i][j1].swapValuePropagate(x[i][j2]) # perform local move by swapping 2 selected variables 
  print('Step',it,' candidates = ',len(candidates),': swap x[',i,',',j1,'] and x[',i,',',j2,'] violations = ',C.violations())
  if C.violations() == 0:
   break
  #printSolution()
  
print('Init, C = ',C.violations())
printSolution()   
#simpleHillClimbing(1000)    
improvedHillClimbing(2000)     
printSolution()  