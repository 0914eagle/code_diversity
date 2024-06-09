
def solve(a, b, x):
    n = len(a)
    m = len(b)
    c = [[a[i] * b[j] for j in range(m)] for i in range(n)]
    max_area = 0
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    area = (k - i + 1) * (l - j + 1)
                    if area > max_area and sum(sum(c[i:k+1], [])) <= x:
                        max_area = area
    return max_area

