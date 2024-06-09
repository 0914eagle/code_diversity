
def solve(s, x):
    n = len(s)
    count = 0
    for i in range(n):
        balance = s[:i].count("0") - s[:i].count("1")
        if balance == x:
            count += 1
    return count

