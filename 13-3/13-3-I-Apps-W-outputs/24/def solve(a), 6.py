
def solve(a):
    n = len(a)
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] * a[j] * a[k] == min(a[i] * a[j] * a[k], a[i] * a[k] * a[j], a[j] * a[k] * a[i]):
                    count += 1
    return count

