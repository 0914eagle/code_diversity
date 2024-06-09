
def get_teammates(n, strengths):
    teammates = [0] * (2 * n)
    for i in range(1, 2 * n):
        max_strength = 0
        for j in range(1, 2 * n):
            if i != j and strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j
    return teammates

