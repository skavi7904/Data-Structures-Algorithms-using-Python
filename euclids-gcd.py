def gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n:
        (m, n) = (n, m % n)
    return n


print(gcd(96, 4))
