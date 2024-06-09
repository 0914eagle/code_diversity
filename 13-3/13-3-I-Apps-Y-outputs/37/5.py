
def solve(a, k):
    n = len(a)
    x = 0
    count = 0
    while True:
        done = True
        for i in range(n):
            if a[i] % k != 0:
                done = False
                break
        if done:
            return count
        for i in range(n):
            if a[i] % k != 0:
                a[i] += x
                count += 1
        x += 1

