
def solve(a, k):
    n = len(a)
    x = 0
    count = 0
    while True:
        found = True
        for i in range(n):
            if a[i] % k != 0:
                found = False
                break
        if found:
            return count
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                count += 1
        x += 1

