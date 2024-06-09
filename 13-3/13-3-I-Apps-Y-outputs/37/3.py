
def solve(a, k):
    n = len(a)
    x = 0
    count = 0
    while True:
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                count += 1
        x += 1
        if all(a[i] % k == 0 for i in range(n)):
            break
    return count

