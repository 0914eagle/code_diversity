
def get_points(x):
    # Find all prime factors of x
    prime_factors = []
    i = 2
    while i * i <= x:
        if x % i:
            i += 1
        else:
            x //= i
            prime_factors.append(i)
    if x > 1:
        prime_factors.append(x)
    # Calculate the number of factors
    num_factors = 1
    for p in prime_factors:
        num_factors *= p + 1
    return num_factors

