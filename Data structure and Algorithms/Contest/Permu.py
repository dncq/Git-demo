
# def permutation(lst):

#     if len(lst) == 0:
#         return []

#     if len(lst) == 1:
#         return [lst]

 
#     l = [] 
 
#     for i in range(len(lst)):
#        m = lst[i]
 

#        remLst = lst[:i] + lst[i+1:]
 

#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l
 
 

# n = int(input())
# data = []
# for i in range(1,n+1):
#     data.append(i)
# for p in permutation(data):
#     print(*p)


n = int(input())
x = [0 for i in range(n)]
def solution():
    for i in range(n):
        print(x[i], end = ' ')
    print()

def check(v,k):
    for i in range(k):
        if v == x[i]:
            return False
    return True

def Try(k):
    for v in range(1,n+1):
        if check(v,k):
            x[k] = v
            if k == n-1:
                solution()
            else:
                Try(k+1)
Try(0)