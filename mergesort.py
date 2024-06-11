def merge(A: list, B: list) -> list:
    (C, m, n, i, j) = ([], len(A), len(B), 0, 0)
    while i + j < m + n:
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    return C


def mergesort(L, left, right):
    if right - left <= 1:
        return (L[left:right])
    if right - left > 1:
        mid = (left + right) // 2
        leftlist = mergesort(L, left, mid)
        rightlist = mergesort(L, mid, right)
        return (merge(leftlist, rightlist))


x = list(range(1, 5, 2)) + list(range(0, 5, 2))
print(x)
print(mergesort(x, 0, len(x)))
