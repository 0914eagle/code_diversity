
def solve(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    if a == b:
        return a
    if a % 2 == 0 and b % 2 == 0:
        return solve(a // 2, b // 2) * 4
    if a % 2 == 0 and b % 2 == 1:
        return solve(a // 2, b // 2) * 2 * b
    if a % 2 == 1 and b % 2 == 0:
        return solve(a // 2, b // 2) * 2 * a
    if a % 2 == 1 and b % 2 == 1:
        return solve(a // 2, b // 2) * 2 * a * b
    return -1

