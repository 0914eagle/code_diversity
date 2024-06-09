
def solve(n):
    return str(sum(i**n for i in range(1, 5)) % 5)

