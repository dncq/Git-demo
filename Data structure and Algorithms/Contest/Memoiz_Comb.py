def C(k,n,mod = 1e9 + 7):
        if k==0 or k==n:
            memo[(k,n)] = 1
        if k == 1:
            memo[(k, n)] = n
        if (k,n) not in memo:
            memo[(k,n)] = (C(k,n-1)%mod + C(k-1,n-1)%mod) %mod
        return memo[(k,n)]

k,n = input().split()
memo = {}
print('%.0f' % C(int(k),int(n)))


