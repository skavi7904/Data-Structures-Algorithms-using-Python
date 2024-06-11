# def threesquares(m):
#     return False
#     f
#     if m<0:
#     or p in range(int(m**0.5)+1):
#         for q in range(int(m ** 0.5) + 1):
#             for r in range(int(m ** 0.5) + 1):
#                 if (p**2 + q**2 + r**2) == m:
#                     return True
#     return False

def factors(n):
    if n == 0:
        return([0])
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist.append(i)
    return(factorlist)

def square(n):
    return(len(factors(n))%2 == 1)

def threesquares(n):
    for i in range(0,n+1):
        for j in range(i,n+1):
            if square(i) and square(j) and square(n-(i+j)):
                return(
                    True)
    return(False)