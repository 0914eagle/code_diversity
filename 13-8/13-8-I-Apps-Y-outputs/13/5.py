
def solve(a):
    n = len(a)
    if n % 6 == 0:
        return 0
    else:
        count = 0
        for i in range(n):
            if a[i] != i % 6 + 1:
                count += 1
        return count

