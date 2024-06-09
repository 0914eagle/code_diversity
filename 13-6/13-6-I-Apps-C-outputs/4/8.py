
def solve(n):
    if n == 1:
        return "YES"
    else:
        pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
        for pair in pairs:
            if pair[0] != pair[1] - 1:
                return "NO"
        return "YES"

