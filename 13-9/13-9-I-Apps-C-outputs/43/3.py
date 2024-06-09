
def get_valid_positions(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    positions = []
    for i in range(n - m + 1):
        found = True
        for j in range(m):
            if a[i + j] != b[j]:
                found = False
                break
        if found:
            count += 1
            positions.append(i + 1)
    return count, positions

