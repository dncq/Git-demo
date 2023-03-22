# Dm cuoc doi
'''
6 9
1 3 7
1 6 3
2 4 9
2 5 6
2 6 4
3 4 8
3 6 5
4 5 2
4 6 1
'''

# CODE
import sys
def inp():
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for v in range(n+1)]
    # A[v] in the list of adjacent edges of v
    for i in range(m):
        [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append([v,w])
        A[v].append([u,w])
    return n,m,A

def delete(S):
    # select and delete the node u having minimum value d[u] from S
    minD = INF
    u = -1
    for x in S:
        if minD > d[x]:
            minD = d[x]
            u = x
    # if u != -1:
    S.remove(u)
    return u

def Tracepath(s,t):
    path = []
    v = t
    while v!= s:
        path.append(v)
        v = p[v] 
    path.append(s)
    path.reverse()
    return path

def dijkstra(s):
    # INitialize
    for [v,w] in A[s]:
        d[v] = w
        p[v] = s
    d[s] = 0
    S = set() # Set of nodes such that the shortest path from s to v is not found
    for v in range(1,n+1):
        if v!=s:
            S.add(v)
    while(len(S)) > 0:
        u = delete(S)
        # explore 
        if u == -1:
            break
        for [v,w] in A[u]:
            if v in S:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    p[v] = u
    for v in range(1,n+1):
        print('d[',str(v),'] =',str(d[v]),'path = ',Tracepath(s,v))
n,m,A = inp()
INF = 1e9
d = [INF for v in range(n+1)]
p = [0 for i in range(n+1)]
dijkstra(1)
# print(A)

'''
#import libraries 
import numpy as np 
import pandas as pd 
from pulp import * 

#define the data 
locations = ["A", "B", "C", "D"] 
distance_matrix = np.array([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])  
num_salesmen = 2 
depot = 0 #starting point for all salesmen is same 

#create the problem object in PuLP 
prob = LpProblem("Min-Max Multiple Traveling Salesman Problem", LpMinimize)  

 #create decision variables for each salesman and each location  
salesman_vars = LpVariable.dicts("Salesman", [(i, j) for i in range(num_salesmen) for j in locations], cat='Binary')  

 #create objective function to minimize the max distance traveled by any salesman   
prob += lpSum([distance_matrix[i][j]*salesman_vars[(i, j)] for i in range(num_salesmen) for j in locations])  

 #constraint: each location must be visited by exactly one salesman   
for j in locations:  
    prob += lpSum([salesman_vars[(i, j)] for i in range(num_salesmen)]) == 1  

 #constraint: each salesman starts and ends at the depot   
for i in range(num_salesmen):  
    prob += lpSum([salesman_vars[(i ,j)] for j in locations]) == 2  

 #constraint: no subtours (each salesman must visit all locations before returning to depot)   
for i in range(num_salesmen):  
    for subset in itertools.combinations(locations, 2):  														     prob += lpSum([salesman_vars[(i ,j)] for j in subset]) <= 1    

 #run optimization engine on problem object     prob.solve()     
'''

'''
import numpy as np 

def cross_exchange(dist_matrix, m): 
    # Initialize the path 
    path = np.arange(m) 

    # Calculate the initial cost of the path 
    cost = 0
    for i in range(m-1): 
        cost += dist_matrix[path[i]][path[i+1]] 

    # Initialize best cost and best path to current values  
    best_cost = cost  
    best_path = np.copy(path)  

    # Loop until no improvement is made  
    while True:  

        # Flag to indicate if any improvement is made or not  
        improved = False

        # Consider all possible cross-exchanges  
        for i in range(m-2): 

            for j in range(i+2, m): 

                # Store current nodes at i and j positions in path[]  
                a = path[i]  
                b = path[i+1]  
                c = path[j]  
                d = path[j+1]  

                # Calculate new cost if we make a cross exchange between (a,b) and (c,d) edges. 
                new_cost = cost - dist_matrix[a][b] - dist_matrix[c][d] + dist_matrix[a][c] + dist_matrix[b][d] 

                # If new cost is better than current cost then we make this exchange and update the variables accordingly. 
                if new_cost < cost: 

                    improved = True

                    # Update the paths with cross exchange of edges. 														                            tempPath=np.copy(path)                           tempPath[i+1]=c                           tempPath[j]=b                           path=np.copy(tempPath)                           

                    # Update the costs with new cost value.                  cost=newCost                       if (cost<bestCost):                          bestCost=cost                         bestPath=np.copy(path)               if (improved==False):                       break              return [bestCost,bestPath]
'''