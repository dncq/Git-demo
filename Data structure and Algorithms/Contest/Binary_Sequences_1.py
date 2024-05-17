n = int(input())
x = [0 for j in range(n)]
count = 0
def check(v,k):
    if k == 0:
        return 1
    return v + x[k-1] <= 1
def Try(k):
    for v in range(0,2):
        if check(v,k):
            x[k] = v
            if k == n-1: 
                solution()
            else:
                Try(k+1)

def solution():
    global count
    for i in range(n):
        print(x[i], end = '')
    count += 1
    print()
Try(0)
print(count)

# n = int(input())
# def f(n):
#     if n == 1:
#         return 3
#     if n == 2:
#         return 7
#     return 2*f(n-1) + f(n-2)

# print('Number of solutions:',f(n))