
def solve(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    c = (s * (1 + 1 / c) / v) ** (1 / n)
    time_algorithm = n * (log2(n) ** (c * sqrt(2))) / (p * 10 ** 9)
    
    # Calculate the total time it takes to run the algorithm and distribute the keys
    time_total = time_algorithm + s / v
    
    # Return the optimal parameter c and the total time
    return c, time_total

