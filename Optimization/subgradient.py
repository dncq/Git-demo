import numpy as np
def solve(A,b,x0,alpha):
    f = lambda x: np.max(A.dot(x) + b)
    g = lambda x: A[np.argmax(A.dot(x) + b)]
    x = x0
    f_best = f(x)
    for i in range(10000):
        x = x - alpha*g(x)
        if f(x) < f_best:
            f_best = f(x)
        print('Step ',i, ': x = ',x, 'f(x) = ',f(x),'f_best = ',f_best)
    return f_best
A = np.array([[2,-3],[5,1],[-3,1]])
b = np.array([4,-3,2]).T
x0 = np.array([0,0]).T
alpha = 0.005
solve(A,b,x0,alpha)

# j = np.argmax(x0)
