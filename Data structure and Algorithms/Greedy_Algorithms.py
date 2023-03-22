#Pseudo code
"""
Greedy(){
    S = {};
    while C != (empty set) and not solution(5){
        x = select(C);
        C = C/{x};
        if feasible(S union {x}}{
            S = S union {x}
        }
    }
    return S;
}
"""
#Time complexity
"""
for C = {1,2,...,n}
S = {}
for i = 2 --> n do:
    x = select(e) belongs to C s.t d[cur,x] is minimal
    C = C / {x};
    S = S ::x; // add x to the cost of S
    cur = x;
Time Complexity: O(n^2)
"""

#Code'
# import sys
# # L =[(0,10), (3,7), (6,14), (9,11) , (12,15), (17,19)]
# # # print('before sorting L =',L)

# # # print('after sorting L =', L)

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

'''
6
0 10
3 7
6 14
9 11
12 15
17 19
'''
