f = lambda x1,x2,x3: x1**2 + x2**2 + x3**3 -x1*x2 - x2*x3 + x1 + x3
df = lambda x1,x2,x3: [2*x1 - x2 + 1, 2*x2 - x1 - x3, 2*x3 - x2 + 1]
[x1,x2,x3] = [0,0,0]
for i in range(1,1001):
    [D1,D2,D3] = df(x1,x2,x3)
    A = 2*x1*D1 + 2*x2*D2 + 2*x3*D3 - x2*D1 - x1*D2 - D2*x3 - D3*x2 + D1 + D3
    B = 2*D1*D1 + 2*D2*D2 + 2*D3*D3 - 2*(D1*D2 + D2*D3)
    if B == 0:
        break
    alpha = A/B
    x1 = x1 - alpha*D1
    x2 = x2 - alpha*D2
    x3 = x3 - alpha*D3
    print('f(x) at',i,'-th iteration: f(x) = ',f(x1,x2,x3))