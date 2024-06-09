
def solve(p):
    n = len(p)
    m = 0
    while not is_sorted(p):
        i, j = find_farthest_indices(p)
        p[i], p[j] = p[j], p[i]
        m += 1
    return m

def is_sorted(p):
    return p == list(range(1, len(p) + 1))

def find_farthest_indices(p):
    n = len(p)
    max_diff = -1
    i, j = -1, -1
    for k in range(n):
        for l in range(k+1, n):
            diff = abs(p[k] - p[l])
            if diff > max_diff:
                max_diff = diff
                i, j = k, l
    return i, j

