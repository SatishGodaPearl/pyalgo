"""
PSEUDO CODE:

function mergesort(m)
   var list left, right
   if length(m) ≤ 1
       return m
   else
       middle = length(m) / 2
       for each x in m up to middle
           add x to left
       for each x in m after middle
           add x to right
       left = mergesort(left)
       right = mergesort(right)
       result = merge(left, right)
       return result
"""

def mergeSort(alist):
    print("Splitting: ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
