def power(x, n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * x
    return ans


print(power(4, 3))
