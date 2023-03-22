import sys
def Input():
    [N] = [int(x) for x in sys.stdin.readline().split()]
    A = [int(x) for x in sys.stdin.readline().split()]
    A.insert(0,0) # use the array from index 1 to index N
    return N,A

def swap(i,j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def heapify(i,N):
    # perform the heapify from index i until index n of the sequence A
    L = 2*i # index of the left child of A[i]
    R = 2*i + 1 # index of the right child of A[i]
    max_index = i # the index of the maximum elements among the children of A[i]
    if L <= N and A[L] > A[max_index]:
        max_index = L
    if R <= N and A[R] > A[max_index]:
        max_index = R
    if max_index != i:
        swap(i,max_index)
        heapify(max_index,N)

def BuildHeap():
    for i in range(N//2,0,-1):
        heapify(i,N)
def HeapSort():
    BuildHeap()
    for i in range(N, 1,-1):
        swap(1,i) # swap the biggest elements A[1] and the last elemnt of the remaing sequence A[i]
        heapify(1,i-1) # FIX the last element A[i], perform heapify so that the remaining sequence A[1,...i-1] becomes a max-heap

def Merge(L,M,R):
    # merge 2 sorted list: A[1,....,M] and A[(M+1)....R] into a unique sorted list
    i = L # index runs on the left sub-sequence A[1...M]
    j = M+1 # index runs on the right sub-sequence A[(M+1)....R]
    for k in range(L,R+1):
        if i > M: # i is out of the left sub-sequence
            TA[k] = A[j]
            j += 1
        elif j > R: # j is out of the right sub-sequence
            TA[k] = A[i]
            i += 1
        else:
            if A[i] < A[j]:
                TA[k] = A[i]
                i += 1
            else:
                TA[k] = A[j]
                j += 1
    # copy the suquence TA[L.....R] back to the original one
    for k in range(L,R+1):
        A[k] = TA[k]

def MergeSort(L,R):
    if L >= R:
        return
    M = (L+R) // 2
    MergeSort(L,M)
    MergeSort(M+1,R)
    Merge(L,M,R)

N,A = Input()
TA = [0 for i in range(N+1)] # temp array used in the merge sort algo
# HeapSort()
# print('Sorted list by HeapSort: ')
# print(*A[1:])
MergeSort(1,N-1)
print('Sorted list by MergeSort: ')
print(*A[1:])

'''
11
6 1 2 9 7 5 3 10 4 11 12
'''