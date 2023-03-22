# import sys
# [n] = [int(x) for x in sys.stdin.readline().split()]
# L = []
# for i in range(n):
#     s = [int(x) for x in sys.stdin.readline().split()]
#     L.append(s)

# L.sort(key = lambda x: x[1])
# res = 0
# last = -1e9
# for seg in L:
#     if seg[0] > last:
#         res = res + 1
#         last = seg[1]

# print(res)


# Disjoint segment (premium version)
import sys
def INP():
    [n] = [int(x) for x in sys.stdin.readline().split()]
    L = []
    for i in range(n):
        rows = [int(x) for x in sys.stdin.readline().split()]
        L.append(rows)
    return n,L
n,L = INP()
L.sort(key = lambda x: x[1])

# print(L)
# [3,7],[0,10],[9,11],[6,14],[12,15],[17,19]

S = [L[0]]
res = 1
last = S[-1]
for segs in L[1:]:
    if segs[0] > last[1]:
        S.append(segs)
        res += 1
        last = segs 

print('Solution:',S)
print(res)

'''
6
0 10
3 7
6 14
9 11
12 15
17 19
'''