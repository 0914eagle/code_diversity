
def solve(n, m, a):
    result = 1
    for i in range(n):
        for j in range(i+1, n):
            result = result * abs(a[i] - a[j]) % m
    return result

