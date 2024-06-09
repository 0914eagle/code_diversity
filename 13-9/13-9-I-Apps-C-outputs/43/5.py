
def get_valid_positions(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    positions = []
    for i in range(n - m + 1):
        matched = True
        for j in range(m):
            if a[i + j] != b[j]:
                matched = False
                break
        if matched:
            count += 1
            positions.append(i + 1)
    return count, positions

