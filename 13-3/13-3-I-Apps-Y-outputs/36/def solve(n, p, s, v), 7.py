
def solve(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    c = (n * (np.log2(n) ** (1 / 2)) / (p * 10 ** 9)) ** (1 / (s / v))
    
    # Calculate the total time it takes to run the algorithm and distribute the keys
    t = s / v + c * (n * (np.log2(n) ** (1 / 2)) / (p * 10 ** 9))
    
    return t, c

