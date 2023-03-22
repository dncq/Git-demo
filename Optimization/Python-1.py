from ortools.linear_solver import pywraplp
# Nhập dữ liệu
filename = r'C:\python code\Optimization\1.txt'
def INP(filename):
    with open(filename) as f:
        T = []
        for eachline in f:
            # line = map(int, eachline)
            T.append(eachline.split())
        N = int(T[0][0])
        K = int(T[0][1])
        d = [int(x) for x in T[1]]
        S = []
        for line in T[2:]:
            eachline = map(int, line)
            S.append(list(eachline))
        return N,K,d,S
# N: số lượng khách hàng
# K: số lượng nhân viên
# M: thời gian bảo trì
# S: thời gian di chuyển giữa 2 địa điểm
N,K,d,S = INP(filename)
# Tạo bài toán LP
prob = pywraplp.Solver.CreateSolver(pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
# Tạo các biến x[i,k], y[i,j,k] và c[k]
K = int(input("Số lượng công nhân: "))
d = []
N = int(input("Số lượng khách hàng: "))
for i in range(N):
    d.append(int(input("Thời gian bảo trì khách hàng thứ " + str(i+1) + ": ")))
x = {}
for i in range(N+1):
    for k in range(K+1):
        x[i, k] = prob.IntVar(0, 1, "x[%i,%i]" % (i, k))
y = {}
for i in range(N+1):
    for j in range(N+1):
        for k in range(K+1):
            y[i, j, k] = prob.IntVar(0, 1, "y[%i,%i,%i]" % (i, j, k))
c = [prob.IntVar(0, 100, "c[%i]" % i) for i in range(K+1)]
# Tạo hàm mục tiêu
prob.Minimize(sum(c[k] * x[i][k] for i in range(1, N+1) for k in range(1, K+1)))

# Thêm các ràng buộc
# Ràng buộc 1: Mỗi khách hàng chỉ được bảo trì bởi một nhân viên duy nhất
for i in range(1, N+1):
    prob.Add(sum(x[i][k] for k in range(1, K+1)) == 1)

# Ràng buộc 2: Mỗi nhân viên chỉ bảo trì tối đa một khách hàng trong một thời điểm
for k in range(1, K+1):
    prob.Add(sum(x[i][k] for i in range(1, N+1)) <= 1)

# Ràng buộc 3: Thời gian làm việc của mỗi nhân viên phải đủ để hoàn thành các công việc
for k in range(1, K+1):
    prob.Add(sum(d[i] * x[i][k] for i in range(1, N+1)) <= c[k])
# Ràng buộc 4: Mỗi nhân viên phải đi từ trụ sở đến điểm bắt đầu bảo trì và từ điểm bảo trì đến trụ sở
for k in range(K):
    # Add constraint for starting from headquarters
    prob.Add(sum(y[0, i, k] for i in range(N+1)) == 1)
    # Add constraint for returning to headquarters
    prob.Add(sum(y[i, 0, k] for i in range(N+1)) == 1)

# Ràng buộc 5: Mỗi nhân viên chỉ được di chuyển đến một khách hàng duy nhất trong một thời điểm
for i in range(1, N+1):
    for k in range(1, K+1):
        prob.Add(sum(y[i, j, k] for j in range(1, N+1)) <= 1)
        prob.Add(sum(y[j, i, k] for j in range(1, N+1)) <= 1)

# Ràng buộc 6: Mỗi khách hàng chỉ được bảo trì bởi một nhân viên duy nhất
for i in range(1, N+1):
    for k in range(1, K+1):
        prob.Add(sum(y[i, j, k] * x[j][k] for j in range(1, N+1)) == x[i][k])

# Ràng buộc 7: Mỗi nhân viên chỉ bảo trì tối đa một khách hàng trong một thời điểm
for j in range(1, N+1):
    for k in range(1, K+1):
        prob.Add(sum(y[i, j, k] * x[j][k] for i in range(1, N+1)) == 0)
# Giải bài toán
prob.solve()
# In kết quả
# print("Kết quả: ", value(prob.objective))
for i in range(1, N+1):
    for k in range(1, K+1):
        if x[i][k].value() == 1:
            print("Khách hàng", i, "được bảo trì bởi nhân viên", k)