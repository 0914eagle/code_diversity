
def catch_x_mouse(m, x):
    # Find the prime factors of m
    prime_factors = []
    i = 2
    while i * i <= m:
        if m % i:
            i += 1
        else:
            m //= i
            prime_factors.append(i)
    prime_factors.append(m)

    # Find the minimum number of traps needed
    traps = 0
    for p in prime_factors:
        if x % p == 0:
            traps += 1

    return traps

