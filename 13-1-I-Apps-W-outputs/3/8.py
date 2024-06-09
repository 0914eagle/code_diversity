
def solve(n, bumpers):
    count = 0
    for i in range(n):
        if bumpers[i] == '<':
            if i - 1 < 0:
                count += 1
        else:
            if i + 1 > n - 1:
                count += 1
    return count

