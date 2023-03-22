import sys

def input():
    [n] = [int(x) for x in sys.stdin.readline().split()]
    a  = [int(x) for x in sys.stdin.readline().split()]
    return n, a

def maxLeft(L,R):
    # return the weight of the largest subsequence of a[L,R] terminating at a[R]
    res = a[R]
    s = 0
    i = R
    while i >= L:
        s = s + a[i]
        res = max(res,s)
        i = i-1

    return res


def maxRight(L,R):
    # return the weight of the largest subsequencr of a[L,R] staring at a[L]
    res = a[L]
    s = 0
    i = L
    while i <= R:
        s = s + a[i]
        res = max(res, s)
        i = i+1

    return res

def maxSeq(L,R):
    if L == R:
        return a[L]
    
    m = (L+R)//2 #index of the element in the middle
    mL = maxSeq(L, m) # the weight  of the largest subsequence of a[L,m]
    mR = maxSeq(m+1, R) # the weight  of the largest subsequence of a[m+1, R]
    mLR = maxLeft(L,m) + maxRight(m+1,R) #the weight of the largest subsequence covering both a[L..m] and a[m+1..R]
    # print('maxSeq(',L,',',R,'mL = ',mL,'mR = ',mR,'mLR = ',mLR)
    res = mL #res = MAX(mL, mR, MLR)
    if res < mR:
        res = mR
    if res < mLR:
        res = mLR
    return res


n,a = input()
res = maxSeq(0, n-1)
print(res)