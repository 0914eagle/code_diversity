
def get_probability(n, m):
    probability = 0
    for i in range(1, n+1):
        probability += (1/m) * (1/i)
    return probability

