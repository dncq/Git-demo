def Try(k,last):
    global s
    global c
    for v in range(last+1,m+1):
        s += v
        if k == n:
            if s == m:
                c += 1
        else:
            Try(k+1,v)
        s -= v
s = 0
c = 0
n = 3
m = 11
Try(1,0)
print(c)
