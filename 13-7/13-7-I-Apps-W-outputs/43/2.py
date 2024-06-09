
def solve(n, m, a, b, s):
    count = 0
    for i in range(n - m + 1):
        for j in range(i, n - m + 1):
            if a[i:j + 1] + b[i:j + 1] == s:
                count += 1
    return count

