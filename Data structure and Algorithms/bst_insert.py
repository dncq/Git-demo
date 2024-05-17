class Node:
    def __init__(self,inputkey) -> None:
        self.key = inputkey
        self.leftchild = None
        self.rightchild = None
def preOrder(r):
    if r == None:
        return 
    print(r.key, end = " ")
    preOrder(r.leftchild)
    preOrder(r.rightchild)

def insert(r,k):
    if r == None:
        return Node(k)
    if r.key == k:
        return r
    if r.key < k:
        r.rightchild = insert(r.rightchild, k)
    else:
        r.leftchild = insert(r.leftchild, k)
    return r

keys = []
while True:
    cmd = input()
    if cmd == "#":
        break
    keys.append(int(cmd.split()[1]))
r = Node(keys[0])
for key in keys[1:]:
    r = insert(r,key)
preOrder(r)