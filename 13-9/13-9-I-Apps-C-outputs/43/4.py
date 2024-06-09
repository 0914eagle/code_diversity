
def solve(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    positions = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if a[i + j] != b[j]:
                match = False
                break
        if match:
            count += 1
            positions.append(i + 1)
    return count, positions

