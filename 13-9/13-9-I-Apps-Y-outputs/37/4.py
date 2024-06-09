
def solve(a, k):
    n = len(a)
    x = 0
    count = 0
    while True:
        changed = False
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                changed = True
        if not changed:
            return count
        count += 1
        x += 1

