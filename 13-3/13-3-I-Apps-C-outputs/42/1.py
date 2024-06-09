
def solve(X):
    # Find the prime factors of X
    prime_factors = []
    i = 2
    while i * i <= X:
        if X % i:
            i += 1
        else:
            X //= i
            prime_factors.append(i)
    if X > 1:
        prime_factors.append(X)
    # Calculate the number of points obtained by the second player
    points = 0
    for i in range(len(prime_factors)):
        points += prime_factors[i] + 1
    return points

