
def solve(n, m):
    result = 0
    for i in range(n, m+1):
        result += i % 1000000007
    return result % 1000000007

