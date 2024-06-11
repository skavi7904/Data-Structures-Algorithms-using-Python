#
#
# table = {}
#
# def fib(n):
#     if n in table:
#         return table[n]
#     if n == 0 or n == 1:
#         value = n
#     else:
#         value = fib(n-1) + fib(n-2)
#     table[n] = value
#     return value
#
# print(fib(9))

#DYNAMIC PROGRAMMING - NOT COMPUTING ANYTHING TWICE

tabe = {}
def fib(n):
    tabe[0] = 0
    tabe[1] = 1
    for i in range(2,n+1):
        tabe[i] = tabe[i-1] + tabe[i-2]
    return tabe[n]

print(fib(0))