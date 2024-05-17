class Node:
    def __init__(self, id):
        self.id = id
        self.leftmostchild = None
        self.rightsibling = None

def __InsertNode(r, v):
    if r == None:
        return None
    if r.leftmostchild == None:
        r.leftmostchild = Node(v)
        return r
    p = r.leftmostchild
    while p.rightsibling != None:
        p = p.rightsibling
    p.rightsibling = Node(v)

def find(u, r):
    if r == None:
        return None
    if r.id == u:
        return r
    p = r.leftmostchild
    while p != None:
        q = find(u, p)
        if q != None: 
            return q
        p = p.rightsibling
    return None 

def InsertNode(v, u):
    p = find(u,r)
    __InsertNode(p,v)

def get_generation(r):  
    h = 0
    p = r.leftmostchild
    while p!= None:
        hp = get_generation(p)
        if h < hp:
            h = hp
        p = p.rightsibling

    return h + 1

def get_descendants(r):
    if r == None:
        return 0
    res = 1
    p = r.leftmostchild
    while p != None:
        res += get_descendants(p)
        p = p.rightsibling
    
    return res

members = []
while True:
    line = input()
    if line == "***":
        break
    members.append(line.split())
query = []
while True:
    cmd = input()
    if cmd == "***":
        break
    query.append(cmd)

n = len(members)
sons = [members[i][0] for i in range(n)]
dads = [members[i][1] for i in range(n)]

r = None
for dad in dads:
    if dad not in sons:
        r = Node(dad)
for checktime in range(n):
    for member in members:
        if find(member[0],r) == None:
            InsertNode(member[0], member[1])

for cmd in query:
    if "descendants" in cmd:
        print(get_descendants(find(cmd.split()[1], r)) - 1)
    if "generation" in cmd:
        print(get_generation(find(cmd.split()[1], r)) - 1)
"""
7
Dung Quang
Tuan Quang
Hang Dung
Phong Tuan
An Tuan
Trang Dung
***
descendants Quang
descendants Dung
generation Tuan
generation Quang
***

"""




# h = dict()
# for dad in dads:
#     if dad not in sons:
#         h[dad] = 1

# for checktime in range(n):
#     for i in range(n):
#         son = sons[i]
#         dad = dads[i]
#         if (dad in h) and (son not in h):
#             h[son] = h[dad] + 1















#------------------------------------------------------------
# listh = [(name, h[name]) for name in h]
# listh.sort()
# for ele in listh:
#     print(*ele)

# # print(borns)
# print(sorted(list(h.items()), key= lambda x: x[1]))



"""
11
Peter Newman
Michael Thomas
John David
Paul Mark
Stephan Mark
Pierre Thomas
Mark Newman
Bill David
David Newman
Thomas Mark
"""