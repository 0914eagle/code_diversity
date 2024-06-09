
def solve(n, x, ls):
    count = 0
    for i in range(n):
        if ls[i] + i <= x:
            count += 1
    return count

