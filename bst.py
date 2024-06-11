def bst(seq, target, f, l):  # f and l are indices
    if f <= l:
        mid = (f + l) // 2  #singleslash gives point
        if seq[mid] == target:
            return True
        elif seq[mid] > target:
            return bst(seq, target, f, mid-1)
        elif seq[mid] < target:
            return bst(seq, target, mid + 1, l)
    return False



seq1 = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 89]

print(bst(seq1, 80, 0, 10))

