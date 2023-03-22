# Dynamic programming

# def max_sub(s):
#     smax = s[0]
#     ei = s[0]
#     for k in range(1,len(s)):
#         ei = max(s[k], ei + s[k])
#         smax = max(ei, smax)
#     return smax
# print(max_sub([-2, 11, -4, 13,-5,2]))

def solve(a):
    s = a[0]
    ans = a[0]
    for i in range(1,len(a)):
        if s > 0:
            s += a[i]
        else:
            s = a[i]
        ans = max(ans,s)
    return ans
a = [-2, 11, -4, 13,-5,2]
print(solve(a))
# import sys

# def input():
#     [n] = [int(x) for x in sys.stdin.readline().split()]
#     a  = [int(x) for x in sys.stdin.readline().split()]
#     return n, a

# def maxSeq():
#     s[0] = a[0]
#     res = s[0]

# n,a = input()
# s = [0 for i in range(n)]
