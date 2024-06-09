
def find_teammates(strengths):
    n = len(strengths)
    teammates = [0] * n
    for i in range(n):
        max_strength = 0
        for j in range(i+1, n):
            if strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j
                teammates[j] = i
    return teammates

