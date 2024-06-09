
def solve(a, b, s):
    n = len(a)
    m = len(b)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            for k in range(m):
                for l in range(k+1, m+1):
                    if a[i:j] + b[k:l] == s:
                        count += 1
    return count

