# import sys
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.poly = [0] * 10000
#         self.next = None

# def Create(poly_id,coef, expo, f):
#     if f == None:
#         f = Node(poly_id)
#         f.poly[expo] = coef
#         return f
    
#     p = f
#     while p.next != None:
#         if p == poly_id:
#             break
#         p = p.next 
    
class Node:
    def __init__(self,c,p) -> None:
        self.coeff = c
        self.pow= p
        self.next = None

def append(head, c, e):
    new_node = Node(c,e)

    while head.next != None:
        head = head.next
    head.next = new_node

def addPolynomial(p1, p2):
    res = Node(0, 0)  # dummy node ...head of resultant list
    prev = res  # pointer to last node of resultant list
 
    while p1 != None and p2 != None:
        if p1.pow < p2.pow:
            prev.next = p2
            prev = p2
            p2 = p2.next
        elif p1.pow > p2.pow:
            prev.next = p1
            prev = p1
            p1 = p1.next
        else:
            p1.coeff += p2.coeff
            prev.next = p1
            prev = p1
            p1 = p1.next
            p2 = p2.next
 
    if (p1 != None):
        prev.next = p1
 
    if (p2 != None):
        prev.next = p2
 
    return res.next

if __name__ == '__main__':
 
    # 1st Number: 5x^2+4x^1+2x^0
    poly1 = Node(5, 2)
    append(poly1, 4, 1)
    append(poly1, 2, 0)
 
    # 2nd Number: -5x^1-5x^0
    poly2 = Node(-5, 1)
    append(poly2, -5, 0)
 
    sum = addPolynomial(poly1, poly2)
 
    ptr = sum
    while ptr != None:
        # printing polynomial
        print(str(ptr.coeff) + 'x^' + str(ptr.pow), end="")
        if ptr.next != None:
            print(" + ", end="")
        ptr = ptr.next
    print()