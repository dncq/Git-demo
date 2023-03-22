from py2opt.routefinder import RouteFinder
import sys
filename = r'C:\python code\Optimization\1.txt'
def INP(filename):
    with open(filename) as f:
        T = []
        for eachline in f:
            # line = map(int, eachline)
            T.append(eachline.split())
        N = int(T[0][0])
        K = int(T[0][1])
        M = [int(x) for x in T[1]]
        S = []
        for line in T[2:]:
            eachline = map(int, line)
            S.append(list(eachline))
        return N,K,M,S
N,K,d,S = INP(filename)
# print(S)
#     return N,K,M,S
# N,K,M,S = INP(filename)
        
# def inp():
#     # N: Sô khách hàng cần bảo trì
#     # K: Số nhân viên bảo trì
#     # M: Thời gian bảo trì của các khách hàng
#     # S: Thời gian di chuyển giữa hai địa điểm
#     [N,K] = [int(x) for x in sys.stdin.readline().split()]
#     M = [int(x) for x in sys.stdin.readline().split()]
#     S = []
#     for i in range(N+1):
#         rows = [int(x) for x in sys.stdin.readline().split()]
#         S.append(rows)
#     return N,K,M,S

cities_names = [str(i) for i in range(N+1)]
route_finder = RouteFinder(S, cities_names, iterations=N+1)
best_distance, best_route = route_finder.solve()
print('%.0f'%best_distance)
print(best_route)




'''
6 2
15 30 20 30 60 45
0 30 54 39 48 43 20
48 0 23 40 32 44 60
20 20 0 30 40 30 45
30 35 40 0 20 30 60
20 20 30 40 0 50 10
10 10 20 30 50 0 20
50 50 10 20 30 40 0
'''
