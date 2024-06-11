def selectionsort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start, len(l)):
            if l[minpos] > l[i]:
                minpos = i
        (l[start], l[minpos]) = (l[minpos], l[start])


list1 = list(range(100000,0,-1))
selectionsort(list1)
print(list1)
