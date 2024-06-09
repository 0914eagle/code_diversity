
def solve(a, b, c, d):
    count = 0
    for i in range(a, b+1):
        if i % c != 0 and i % d != 0:
            count += 1
    return count

