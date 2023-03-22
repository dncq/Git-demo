# class Node:
#     def __init__(self,inputkey) -> None:
#         self.key = inputkey
#         self.leftchild = None
#         self.rightchild = None

# def insert(r,k):
#     if r == None:
#         return Node(k)
#     if r.key == k:
#         return r
#     if r.key < k:
#         r.rightchild = insert(r.rightchild, k)
#     else:
#         r.leftchild = insert(r.leftchild, k)
#     return r

# def search(r,k):
#     #find and return a node having key = k
#     if r == None:
#         return None
#     if r.key == k:
#         return r
#     if r.key > k:
#         return search(r.leftchild, k)
#     else:
#         return search(r.rightchild, k)

#     # search all:
#     '''
#     # p = r.leftchild
#     # while p!= None:
#     #     q = search(p, k)
#     #     if q != None:
#     #         return q
#     #     p = p.rightchild
#     # return None
#     '''

# def inOrder(r):
#     if r == None:
#         return None
#     inOrder(r.leftchild)
#     print(r.key, end = ' ')
#     inOrder(r.rightchild)
# r = Node(20)
# r = insert(r, 10)
# r = insert(r, 25)
# r = insert(r, 15)
# r = insert(r, 22)
# r = insert(r, 5)

# print()
# print('In-order trafersal: ')
# inOrder(r)
# print()
# p = search(r,10)
# if p != None:
#     print('FOUND')
# else:
#     print('NOT FOUND')
# # print(search(r,100))
