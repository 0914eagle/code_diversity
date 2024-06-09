
def solve(p):
    n = len(p)
    m = 0
    swaps = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) >= n//2:
                swaps.append((i, j))
                m += 1
                if m == 5*n:
                    break
        if m == 5*n:
            break
    return m, swaps

