
def solve(p):
    n = len(p)
    m = 0
    while not is_sorted(p):
        i, j = find_swap(p)
        p[i], p[j] = p[j], p[i]
        m += 1
    return m

def is_sorted(p):
    return p == list(range(1, len(p) + 1))

def find_swap(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) >= n//2:
                return i, j
    return -1, -1

