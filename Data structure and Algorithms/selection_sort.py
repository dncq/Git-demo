# def selection_sort(a):
#     return sorted(a, reverse= True)
# print(selection_sort([1,2,5,4,6,8,5,0]))

# def swap(a,b):
#     temp = a
#     a = b
#     b = temp

""" Using selection sort algorithm"""

""" Descending order """
# def selection_sort(a): 
#     for i in range(len(a)):
#         index_max = i
#         for j in range(i+1,len(a)):
#             if a[j] > a[index_max]:
#                 index_max = j
#         (a[i], a[index_max]) = (a[index_max], a[i])
# a = [1,2,5,4,6,8,5,0]
# selection_sort(a)
# print(a)


""" Ascending order """
# def selection_sort(a): 
#     for i in range(len(a)):
#         index_min = i
#         for j in range(i+1,len(a)):
#             if a[j] < a[index_min]:
#                 index_min = j
#         (a[i], a[index_min]) = (a[index_min], a[i])
# a = [1,2,5,4,6,8,5,0]
# selection_sort(a)
# print(a)

def swap(a,b):
    tmp = a
    a = b
    b = tmp

def partition(L,R,indexPivot):
    pivot = a[indexPivot]
    swap(a[indexPivot],a[R])
    storeindex = L
    for i in range(L,R):
        if a[i] < pivot:
            swap(a[storeindex],a[i])
            storeindex += 1
    swap(a[storeindex],a[R])
    return storeindex


def quicksort(L,R):
    if L<R:
        index = (L+R) // 2
        index = partition(L,R,index)
        if L<index:
            quicksort(L,index-1)
        if index < R:
            quicksort(index+1,R)

a = [5,7,3,8,1,2,9,4,6]
quicksort(0,8)
print('sorted list: ', a)