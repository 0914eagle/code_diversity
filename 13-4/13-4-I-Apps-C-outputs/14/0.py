
def solve(a, s):
    n = len(s)
    b = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n):
            b[i][j + 1] = b[i][j] + int(s[j])
    rectangles = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n + 1):
                    if b[i][l] - b[i][j] == a and b[k][l] - b[k][j] == a:
                        rectangles += 1
    return rectangles

