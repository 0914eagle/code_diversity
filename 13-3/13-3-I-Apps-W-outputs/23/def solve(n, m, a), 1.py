
def solve(n, m, a):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                count += 1
    return count
