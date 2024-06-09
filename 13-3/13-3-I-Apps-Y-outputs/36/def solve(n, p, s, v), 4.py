
def solve(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    c = (s * (1 + 1 / c) / v) ** (1 / n)
    t = s * (1 + 1 / c) / v
    
    # Return the time and parameter c
    return t, c

