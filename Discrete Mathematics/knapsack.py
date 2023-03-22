# # 0/1 Knapsack Problem
# # A Dynamic Programming based Python 
# # Program for 0-1 Knapsack problem
# # Returns the maximum value that can be put in a knapsack of capacity W
# # def knapSack(W, wt, val, n):
# #     K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
# #     # Build table K[][] in bottom up manner
# #     for i in range(n + 1):
# #         for w in range(W + 1):
# #             if i == 0 or w == 0:
# #                 K[i][w] = 0
# #             elif wt[i-1] <= w:
# #                 K[i][w] = maxe(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
# #             else:
# #                 K[i][w] = K[i-1][w]
  
# #     return K[n][W]
  
# # # Driver program to test above function
# # val = [60, 100, 120]
# # wt = [10, 20, 30]
# # W = 50
# # n = len(val)
# # print(knapSack(W, wt, val, n))
  
# # This code is contributed by Bhavya Jain

# '''
# # A naive recursive implementation of 0-1 Knapsack Problem
  
# # Returns the maximum value that can be put in a knapsack of
# # capacity W
# def knapSack(W, wt, val, n):
  
#     # Base Case
#     if n == 0 or W == 0 :
#         return 0
  
#     # If weight of the nth item is more than Knapsack of capacity
#     # W, then this item cannot be included in the optimal solution
#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)
  
#     # return the maximum of two cases:
#     # (1) nth item included
#     # (2) not included
#     else:
#         return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
#                    knapSack(W, wt, val, n-1))
  
# # end of function knapSack
  
# # To test above function
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print knapSack(W, wt, val, n)
  
# # This code is contributed by Nikhil Kumar Singh'''


# # class KnapsackPackage(object): 
# #     """ Knapsack Package Data Class """
# #     def __init__(self, weight, value): 
# #         self.weight = weight 
# #         self.value = value 
# #         self.cost = value / weight 
 
# #     def __lt__(self, other): 
# #         return self.cost < other.cost
 
# # class FractionalKnapsack(object):
# #     def __init__(self):
# #         pass
 
# #     def knapsackGreProc(self, W, V, M, n):
# #         packs = []
# #         for i in range(n): 
# #             packs.append(KnapsackPackage(W[i], V[i]))
# #         packs.sort(reverse = True)
# #         remain = M
# #         result = 0
# #         i = 0
# #         stopProc = False
# #         while (stopProc != True):
# #             if (packs[i].weight <= remain):
# #                 remain -= packs[i].weight;
# #                 result += packs[i].value;
# #             print("Pack ", i, " - Weight ", packs[i].weight, " - Value ", packs[i].value)
# #             if (packs[i].weight > remain):
# #                 i += 1
# #             if (i == n):
# #                 stopProc = True           
# #         print("Max Value:\t", result)
 
# # if __name__ == "__main__": 
# #     W = [15, 10, 2, 4] 
# #     V = [30, 25, 2, 6] 
# #     M = 37
# #     n = 4
# #     proc = FractionalKnapsack()
# #     proc.knapsackGreProc(W, V, M, n)'''

# count = 0
# A = [1, 3, 2, 7, 6, 8, 4, 2, 6, 7]
# s = 0
# for i in range(len(A)):
#     s = A[i]
#     if s % 2 == 0:
#         count += 1
#     for j in range(i+1,len(A)):
#         s += A[j]
#         if s % 2 == 0 :
#             count += 1
#         else:
#             continue
# print(count)

n = 6
def f(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return f(n-1) + f(n-2)
print(f(6))