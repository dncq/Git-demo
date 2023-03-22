def Hash_Code(s, start, end):
    c = 0

    for i in range (start, end + 1):
        c = c * 256 + ord(s[i])
        c = c % Mod
    
    return c


def Rabin_Karp_Algo(P, T):
    cnt = 0
    N = len(T)
    M = len(P)

    e = d ** (M - 1)

    Code_T = Hash_Code(T, 0, M - 1)
    Code_P = Hash_Code(P, 0, M - 1)

    for s in range(0, N - M  + 1):
        if(Code_P == Code_T):
            Check = 1
            for j in range(0, M):
                if(P[j] != T[j + s]):
                    Check = 0
                    break
            
            if(Check): cnt += 1
        else:
            U = ord(T[s]) * e
            U = U % Mod
            U = MinusMod(Code_T, U)
            Code_T = U * d + ord(T[s + M])
            Code_T = Code_T % Mod
        
    return cnt



def MinusMod(a, b):
    a = a % Mod
    b = b % Mod
    
    if(a >= b): return a - b
    else: return Mod + a - b

def exp(d, n):
    if(n == 0): return 1
    if(n == 1): return d % Mod

    n1 = n/2

    u = exp(d, n1)
    u = (u * u) % Mod

    if(n % 2 == 0): return u
    
    return (u * d) % Mod


d = 256
Mod =  1e9 + 7

T_real = []
P_real = []

P = input().split()
for x in P:
    for i in range (len(x)):
        P_real.append(x[i])

T = input().strip().split()
for x in T:
    for i in range (len(x)):
        T_real.append(x[i])
    
ans = Rabin_Karp_Algo(P_real, T_real)

print(ans)