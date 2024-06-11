import random
import sys
sys.setrecursionlimit(100000000)

def randomize(l):
    for i in range(len(l)//2):
        j = random.randrange(0,len(l))
        k = random.randrange(0,len(l))
        (l[j],l[k]) = (l[k],l[j])

def quicksort(L,l,r):
    if r-l <=1:
        return ()
    left = l+1
    for i in range(l+1,r):
        if L[i] <= L[l]:
            (L[left],L[i]) = (L[i],L[left])
            left += 1
    (L[l],L[left-1]) = (L[left-1],L[l])
    quicksort(L,l,left-1) #after pivot interchanged, left decreases which means left sublist's length is left-1 only
    quicksort(L,left,r)

a = list(range(750000,0,-1))
randomize(a)
quicksort(a,0,len(a))
print(a)