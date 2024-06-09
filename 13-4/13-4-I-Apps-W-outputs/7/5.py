
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

    # Find the least common multiple of the prime factors
    lcm = 1
    for p in prime_factors:
        lcm *= p

    # Return the minimum number of traps needed
    return lcm // x

