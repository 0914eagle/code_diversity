
def solve(X):
    # Find the prime factors of X
    prime_factors = []
    i = 2
    while i * i <= X:
        while X % i == 0:
            prime_factors.append(i)
            X //= i
        i += 1
    if X > 1:
        prime_factors.append(X)
    
    # Calculate the number of points obtained by the second player
    points = 0
    for p in prime_factors:
        points += 1
    
    return points

