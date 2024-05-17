# Code của cụ Quý
'''class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
    def isempty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self,data):
        p = Node(data)
        p.next = self.top
        self.top = p
    
    def pop(self):
        if self.isempty():
            return 'NULL'
        poppednode = self.top
        self.top = self.top.next
        poppednode.next = None
        return poppednode.val

# MAIN
mystack = Stack()
res = []
while True:
    cmd = input().split()
    if '#' in cmd: break
    if 'PUSH' in cmd:
        mystack.push(int(cmd[1]))
    if 'POP' in cmd:
        res.append(mystack.pop())
for i in res:
    print(i)'''



# Code của cháu Trường
"""
def stack(cmd):
    curr_stack = []
    pop = []
    for e in cmd:
        if e.split()[0] == "PUSH":
            curr_stack.append(e.split()[1])
        elif e == "POP":
            if len(curr_stack) == 0:
                pop.append("NULL")
            else:
                pop.append(curr_stack[-1])
                curr_stack.pop()
    return pop
command = []
while True:
    cmd = input()
    if cmd == "#":
        break
    command.append(cmd)
            
res = stack(command)
for i in res:
    print(i)
"""



''' myInput = []
while True:
    strg = input()
    if strg == '#':
        break
    myInput.append(strg)
# print(myInput)
def simutation(myInput):
    stack = []
    pop = []
    for e in myInput:
        ee = e.split()
        # print(ee)
        if ee[0] == 'PUSH':
            stack.append(int(ee[1]))
        elif ee[0] == 'POP':
            if len(stack) == 0:
                if e == myInput[0]:
                    return 'NULL'
                else:
                    return pop
            else:
                x = stack.pop()
                pop.append(x)
    return pop
S = simutation(myInput)
if S == 'NULL':
    print(S)
elif len(S) == 0:
    print()
else:
    for i in S:
        print(i)'''