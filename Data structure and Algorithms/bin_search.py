# Binary search for non-decreasing array 

# def bin_search(a,start,end,y):
#     if start == end:
#         if a[start] == y:
#             return start
#         return -1

#     mid = (start + end) // 2
#     if a[mid] == y: return mid
#     elif a[mid] > y: return bin_search(a,start, mid-1,y)
#     elif a[mid] < y: return bin_search(a,mid+1,end,y)


# a = [1,2,3,4,5,6,7,8,9]
# print('Index of y:',bin_search(a,6,8,2))

# Binary search for non-increasing array

# def bin_search(a,start,end,y):
#     if start == end:
#         if a[start] == y:
#             return start
#         return -1
#     mid = (start + end) // 2
#     if a[mid] == y: return mid
#     elif a[mid] < y: return bin_search(a,start, mid-1, y)
#     elif a[mid] > y: return bin_search(a,mid + 1,end,y)

# a = [9,8,7,6,5,4,3,2,1]
# print(bin_search(a,2,5,5))


class Node:
    def __init__(self,data):
        self.LeftMostChild = None
        self.RightSibling = None
        self.data = data
    
def Find(r,k):
    if r == None:
        return None
    if r.data == k:
        return r
    p = Find(k,r.LeftMostChild)
    if p != None:
        return p
    return Find(k,r.RightSibling)

def AddLeft(u,r):
    p = Find(u,r)
    if p == None:
        return
    q = Find(u,r)
    if q != None:
        return
    q = Node(u)
    if p.LeftMostChild != None:
        return
    p.LeftMostChild = q

def AddRight(u,r):
    p = Find(u,r)
    if p == None:
        return
    q = Find(u,r)
    if q != None:
        return
    q = Node(u)
    if p.LeftMostChild != None:
        return
    p.LeftMostChild = q    

A = []
while True:
    inp = input()
    if inp == '*':
        break
    else:
        A.append(inp)

print(A)