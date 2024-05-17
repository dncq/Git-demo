'''
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class Stack():
    def __init__(self) -> None:
        self.top = None
    def isempty(self):
        if self.top == None:
            return True
        return False

    def push(self,data):
        p = Node(data)
        p.next = self.top
        self.top = p
    
    def pop(self):
        if self.isempty():
            return 
        poppednode = self.top
        self.top = self.top.next
        poppednode.next = None
        return poppednode.val

def match(o,c):
    if (o == '(' and c == ')'): 
        return 1
    if (o == '[' and c == ']'): 
        return 1
    if (o == '{' and c == '}'): 
        return 1
    return 0
def check(s,f):
    for i in s:
        if i == '(' or i == '[' or i == '{':
            f.push(i)
        else:
            if f.isempty(): 
                return 0
            else:
                c = f.pop()
                if match(c,i) == 0: 
                    return 0
    if f.isempty():
        return 1
    else:
        return 0
# MAIN
f = Stack()
s = input()
print(check(s,f))
'''

#-------------------------------------
# Using list

def pop_stack(arr):
    return arr[-1]

def check_match(s):
    stack = []
    for par in s:
        if par == "(" or par == "[" or par == "{":
            stack.append(par)
        else:
            if len(stack) == 0:
                return 0
            else:
                if (par == ")" and pop_stack(stack) == "(") or \
                    (par == "]" and pop_stack(stack) == "[") or \
                    (par == "}" and pop_stack(stack) == "{"):
                    stack.pop()
                else:
                    return 0
    if len(stack) == 0:
        return 1
    return 0

s = input()
print(check_match(s))