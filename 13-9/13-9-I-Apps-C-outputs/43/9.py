
def solve(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    positions = []
    for i in range(n - m + 1):
        window = a[i:i+m]
        if window == b:
            count += 1
            positions.append(i + 1)
    return count, positions

