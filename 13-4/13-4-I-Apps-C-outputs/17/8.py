
def get_points(X):
    # Find the prime factors of X
    prime_factors = []
    while X % 2 == 0:
        prime_factors.append(2)
        X //= 2
    for i in range(3, int(X**0.5) + 1, 2):
        while X % i == 0:
            prime_factors.append(i)
            X //= i
    if X > 1:
        prime_factors.append(X)

    # Calculate the number of points
    points = 0
    for prime in prime_factors:
        points += 1

    return points

