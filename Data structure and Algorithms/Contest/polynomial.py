class Node:
    def __init__(self, val):
        self.val = val
        self.poly = [0] * 10005
        self.next = None


def Create(poly_id, coef, exp, f):
    if(f == None):
        f = Node(poly_id)
        f.poly[exp] = coef
        return f
    
    p = f
    while(p.next != None):
        if(p == poly_id): 
            break
        p = p.next
    
    if(p.val == poly_id):
        if(p.poly[exp] != 0): 
            p.poly[exp] += coef
        else: 
            p.poly[exp] = coef
    else:
        p.next = Node(poly_id)
        p.next.poly[exp] = coef
    
    return f

def PrintPoly(val, f):
    if(f == None):
        return
    
    p = f

    while(p.next != None):
        if(p.val == val): break
        p = p.next
    
    if(p.val == val):
        for i in range (10000, 0, -1):
            if(p.poly[i] != 0):
                print(p.poly[i], i - 1, end = " ")
        
        print()

def EvaluatePoly(Poly_id, x, f):
    if(f == None):
        return
    
    p = f
    Sum = 0
    while(p.next != None):
        if(p.val == Poly_id): break
        p = p.next
    
    if(p.val == Poly_id):
        for i in range (10001, 0, -1):
            Sum += p.poly[i] * ((x) ** (i - 1))
    
    print(Sum)

    return

def Destroy(Poly_id, f):
    if(f == None):
        return None
    
    p = f

    while(p.next != None):
        if(p.next == Poly_id): break
        p = p.next
    
    if(p.next != None):
        p.next = p.next.next
    
    return f

def AddPoly(Poly_1, Poly_2, Poly_F, f):
    if(f == None):
        return f
    
    u = f

    while(u.next != None):
        if(u.val == Poly_1): break
        u = u.next
    
    v = f
    while(v.next != None):
        if(v.val == Poly_2): break
        v = v.next
    
    if(u.val == Poly_1 and v.val == Poly_2):
        z = f
        while(z.next != None):
            if(z.val == Poly_F): break
            z = z.next
        
        if(z.val == Poly_F): 
            for i in range(10001, 0, -1):
                z.poly[i] = u.poly[i] + v.poly[i]
        else:
            k = Node(Poly_F)
            z.next = k
            z = z.next
            for i in range(10001, 0, -1):
                z.poly[i] = u.poly[i] + v.poly[i]
                
    return f


# MAIN
Poly = None

while(1):
    Ts = [input().split()]
    if(Ts[0][0] == '*'): break
    if(Ts[0][0] == 'AddTerm'): 
        x = int(Ts[0][1])
        y = int(Ts[0][2])
        z = int(Ts[0][3]) + 1
        Poly = Create(x, y, z, Poly)
    if(Ts[0][0] == 'EvaluatePoly'): EvaluatePoly(int(Ts[0][1]), int(Ts[0][2]), Poly)
    if(Ts[0][0] == 'AddPoly'): Poly = AddPoly(int(Ts[0][1]), int(Ts[0][2]), int(Ts[0][3]), Poly)
    if(Ts[0][0] == 'PrintPoly'): PrintPoly(int(Ts[0][1]), Poly)
    if(Ts[0][0] == 'Destroy'): Poly = Destroy(int(Ts[0][1]), Poly)