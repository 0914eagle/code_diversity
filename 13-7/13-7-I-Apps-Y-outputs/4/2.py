
def solve(a, b):
    if a == b:
        return 0
    if a > b:
        return a - b
    if a % 2 == 0:
        return 1 + solve(a + 1, b)
    else:
        return 1 + solve(a - 1, b)

