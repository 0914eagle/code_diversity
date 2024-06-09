
def possible_matches(N, a, b):
    total_matches = 0
    for i in range(N):
        for j in range(i+1, N):
            total_matches += a[i] * a[j] * b[i] * b[j]
    return total_matches

