
def get_points(x):
    # Find the prime factors of x
    prime_factors = []
    while x % 2 == 0:
        prime_factors.append(2)
        x //= 2
    for i in range(3, int(x**0.5) + 1, 2):
        while x % i == 0:
            prime_factors.append(i)
            x //= i
    if x > 1:
        prime_factors.append(x)

    # Calculate the number of points
    points = 1
    for p in prime_factors:
        points *= p + 1
    return points
