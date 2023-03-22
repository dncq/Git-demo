import random
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import copy

N = 10
V = set(range(N+1))
location = [(np.random.uniform(0,50), np.random.uniform(0,50))]
plt.plot(location[-1][0], location[-1][1],'rs')

d = [0]
for i in V - {0}:
    location.append((np.random.uniform(0,50),np.random.uniform(0,50)))
    d.append(random.randint(1,3))
    plt.scatter(location[-1][0],location[-1][1],d[-1]*20,'b')
    plt.text(location[-1][0],location[-1][1],str(i))

plt.show()

def distance(a,b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

c = [[0 if i == j 
      else round(distance(location[i], location[j])) 
      for j in V] for i in V]

print(c)

# np.random.seed(0)
# y0 = list(np.random.permutation(N))
# y = [y0[i] for i in range(N)]
# print(y)

def TSP_tour_cost(y,c,N):
    y.append(y[0])
    cost = 0
    for i in range(N):
        cost += c[y[i]][y[i+1]]
    y.pop(-1)
    return cost


def TSP_tour_plot(y,location,N):
    y.append(y[0])
    for i in range(N):
        plt.plot([location[y[i]][0], location[y[i+1]][0]],[location[y[i]][1], location[y[i+1]][1]],'r')
    # plt.show()
    y.pop(-1)

# print(TSP_tour_cost(y,c,N))
# TSP_tour_plot(y,location,N)

def TSP_onestep_opt2(y,c,N):
    y.append(y[0])
    for i in range(N-2):
        for j in range(i+2,N):
            total_distance_pre = c[y[i]][y[i+1]] + c[y[j]][y[j+1]]
            total_distance_post = c[y[i]][y[j]] + c[y[i+1]][y[j+1]]
            # print(y[i],y[i+1],y[j],y[j+1],total_distance_pre-total_distance_post)
            if total_distance_post < total_distance_pre:
                for k in range(math.ceil(((j-i-1)/2))):
                    temp = y[i+k+1]
                    y[i+k+1] = y[j-k]
                    y[j-k] = temp
                y.pop(-1)
                return (1,y)
    y.pop(-1)
    return (0,y)

def TSP_opt2(y,c,N,max_iter):
    cost_record = []
    for i in range(max_iter):
        (label,y) = TSP_onestep_opt2(y,c,N)
        cost_record.append(TSP_tour_cost(y,c,N))
        if label == 0:
            break
    return (cost_record, y)

def partition (list_in, n):
    lst = list_in[:]
    random.shuffle(lst)
    return [lst[i::n] for i in range(n)]
[K] = [int(x) for x in sys.stdin.readline().split()]
# N: số thành phố
# K: số nhân viên
group = []
cities = np.random.permutation([i for i in range(1,N+1)])
u = partition(cities, K)
for i in u:
    group.append(list(i))
for u in group:
    u.insert(0,0)
#print(group)

c_group = []
location_group = []
for subgroup in group:
    c_group.append([[c[i][j] for j in subgroup] for i in subgroup])
    location_group.append([location[i] for i in subgroup])
# print(c_group)
# print(location_group)
# (label,y) = TSP_onestep_opt2(y,c,N)
# cost = TSP_tour_cost(y,c,N)
# (cost_record,y) = TSP_opt2(y,c,N,1000)
# print(cost_record[-1])
# TSP_tour_plot(y,location,N)
# plt.plot(cost_record)
# plt.show()
# print(label,cost,y)

max_iter = 100000
total_cost = []
order_y = []

for m in range(K):
    sub_node = group[m]
    sub_N = len(sub_node)
    sub_c = c_group[m]
    sub_y = list(range(sub_N))
    sub_location = location_group[m]
    cost_record, sub_y = TSP_opt2(sub_y, sub_c,sub_N, max_iter)
    TSP_tour_plot(sub_y,sub_location,sub_N)
    order_y.append(sub_y)
    total_cost.append(cost_record[-1])

for i in V-{0}:
    plt.scatter(location[i][0],location[i][1],d[i]*20,'b')
plt.show()
print(total_cost)

replace_y = []
y_cities = []
Route_y = []

def Allocating(route_y, Time): #Tinh tong chi phi can thiet
    for i in (route_y):
        Time += d[i]

    return Time

#Chuyen nen ve tp thuc su:
for m in range(K):
    y = group[m]
    index_y = order_y[m]
    replace_y = [0 for x in range (len(y))]
    for x in range(len(y)):
        replace_y[index_y[x]] = y[x]
    Route_y.append(replace_y)

print(Route_y)

def Swap_Node(i, price1, route1, j, price2, route2): #Dao 2 thanh pho index i, j tren 2 route1 va route2
    route1_copy = copy.deepcopy(route1)
    route2_copy = copy.deepcopy(route2)

    tmp = route1_copy[i]
    route1_copy[i] = route2_copy[j]
    route2_copy[j] = tmp

    route1_index = list(range(len(route1_copy)))
    c_new1 = [[c[i][j] for j in route1_copy] for i in route1_copy]
    cost_record, sub_y1 = TSP_opt2(route1_index, c_new1, len(route1_copy), max_iter)
    route1_cost = cost_record[-1]
    All_Cost_1 = Allocating(route1_copy, route1_cost)

    route2_index = list(range(len(route2_copy)))
    c_new2 = [[c[i][j] for j in route2_copy] for i in route2]
    cost_record, sub_y2 = TSP_opt2(route2_index, c_new2, len(route2_copy), max_iter)
    route2_cost = cost_record[-1]
    All_Cost_2 = Allocating(route2_copy, route2_cost)

    if(All_Cost_1 < Lower_Bound or All_Cost_2 < Lower_Bound or abs(All_Cost_1 - All_Cost_2) > Max_ans): 
        return route1, price1, route2, price2
    
    else: return route2_copy, All_Cost_1, route2_copy, All_Cost_2


def Move_Node(i, price1, route1, price2, route2): # chuyen thanh pho co index i tu route1 sang route2
    route1_copy = copy.deepcopy(route1)
    route2_copy = copy.deepcopy(route2)

    tmp = route1_copy[i]
    route1_copy.remove(tmp)
    route2_copy.append(tmp)

    route1_index = list(range(len(route1_copy)))
    c_new1 = [[c[i][j] for j in route1_copy] for i in route1_copy]
    cost_record, sub_y1 = TSP_opt2(route1_index, c_new1, len(route1_copy), max_iter)
    route1_cost = cost_record[-1]
    All_Cost_1 = Allocating(route1_copy, route1_cost)

    route2_index = list(range(len(route2_copy)))
    c_new2 = [[c[i][j] for j in route2_copy] for i in route2_copy]
    cost_record, sub_y2 = TSP_opt2(route2_index, c_new2, len(route2_copy), max_iter)
    route2_cost = cost_record[-1]
    All_Cost_2 = Allocating(route2_copy, route2_cost)

    if(All_Cost_1 < Lower_Bound or All_Cost_2 < Lower_Bound or abs(All_Cost_1 - All_Cost_2) > Max_ans):
        return route1, price1, route2, price2
    
    return route1_copy, All_Cost_1, route2_copy, All_Cost_2

#Sap xep cac thanh pho theo cost

Cities_sorted = []

for i in range (len(Route_y)):
    Route_x = Allocating(Route_y[i], total_cost[i])
    Cities_sorted.append([Route_x, str(i)])

Cities_sorted.sort()

#Minimize (Routemax - Routemin)

#Consider Route Min 

#Cities_Sorted là các Route từ 1 đến K theo thứ tự tiền tăng dần 
#Route_y là tour của các nhân viên K
#Total_cost la gia tri di cua moi route

route_index = list(range(N))
cost_record, sub_y = TSP_opt2(route_index, c, N, max_iter)
route_cost = cost_record[-1]
All_Cost = Allocating(route_index, route_cost)

Lower_Bound = All_Cost / K

count = 0

#index_max dia chi 
#Price
#Route_max


while(1):
    index_max = int(Cities_sorted[-1][1])
    Price1 = Cities_sorted[-1][0]
    Price2 = Cities_sorted[0][0]
    
    route_max = Route_y[index_max]

    i = int(Cities_sorted[0][1])
    Select = Route_y[i]
    Max_ans = Cities_sorted[-1][0] - Cities_sorted[0][0]

    Cities_sorted.pop(0)
    Cities_sorted.pop(-1)
    index_1 = random.randint(1, len(route_max) - 1)
    index_2 = random.randint(1, len(Select) - 1)


    Route_max, Price1, Select, Price2 = Swap_Node(index_1, Price1, route_max, index_2, Price2, Select)
    Route_y[index_max] = Route_max
    Route_y[i] = Select
    Cities_sorted.append([Price1, str(index_max)])
    Cities_sorted.append([Price2, str(i)])
    Cities_sorted.sort()
    
    count += 1

    if(count > 2): break

count = 0

# while(1):
#     index_max = int(Cities_sorted[-1][1])
#     Price1 = Cities_sorted[-1][0]
#     Price2 = Cities_sorted[0][0]
#     route_max = Route_y[index_max]
#     Max_ans = Cities_sorted[-1][0] - Cities_sorted[0][0]
#     i = int(Cities_sorted[0][1])
#     Select = Route_y[i]

#     Cities_sorted.pop(0)
#     Cities_sorted.pop(-1)
#     index_1 = random.randint(1, len(route_max) - 1)

#     Route_max, Price1, Select, Price2 = Move_Node(index_1,Price1, route_max, Price2, Select)
#     Route_y[index_max] = Route_max
#     Route_y[i] = Select
#     Cities_sorted.append([Price1, str(index_max)])
#     Cities_sorted.append([Price2, str(i)])
#     Cities_sorted.sort()

#     count += 1

#     if(count > max_iter): break


print(Route_y)
print(Cities_sorted)