
def possible_matches(n, a, b):
    total_matches = 0
    for i in range(n):
        for j in range(i+1, n):
            total_matches += a[i] * a[j] * b[i] * b[j]
    return total_matches

