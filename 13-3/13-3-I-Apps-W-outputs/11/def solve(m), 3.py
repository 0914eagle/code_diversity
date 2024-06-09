
def solve(m):
    count = 0
    for n in range(1, 100001):
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        if str(factorial).endswith(str(0) * m):
            count += 1
    return count

