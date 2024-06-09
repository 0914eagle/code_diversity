
def solve(n):
    if n % 2 == 0:
        return "a" * (n // 2) + "b" + "a" * (n // 2)
    else:
        return "a" * (n // 2) + "b" + "a" * (n // 2 + 1)

