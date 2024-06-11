import sys
sys.setrecursionlimit(1000000)
def recursioninsertionsort(seq):
    l = len(seq)
    insertionsortrecursion(seq, l)


def insertionsortrecursion(seq, l):
    if l > 1:
        insertionsortrecursion(seq, l - 1)
        insertfunction(seq, l - 1)


def insertfunction(seq, k):
    while k > 0 and seq[k] < seq[k - 1]:
        (seq[k], seq[k - 1]) = (seq[k - 1], seq[k])
        k -= 1


a = list(range(10234, 0, -1))
recursioninsertionsort(a)
print(a)
