def remdup(l):
    newl = []
    for i in l:
        if i not in newl:
            newl.append(i)
    return newl


def sumsquare(l):
    odd, even = 0, 0
    for i in l:
        if i % 2 == 0:
            even += i * i
        else:
            odd += i * i
    return [odd, even]


def transpose(l):
    transposematrix = [list(x) for x in zip(*l)]
    return transposematrix
print(transpose([[5,6,7],[0,0,0]]))