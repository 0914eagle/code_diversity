
def solve(a, b, s):
    n = len(a)
    m = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(n):
                for l in range(k+1, n):
                    if s == a[i:j] + b[k:l]:
                        count += 1
    return count
