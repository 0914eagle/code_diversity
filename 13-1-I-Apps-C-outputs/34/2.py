
def solve(n):
    if n == 1:
        return "YES"
    else:
        swaps = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                swaps.append([i, j])
        if len(swaps) % 2 == 0:
            return "YES"
        else:
            return "NO"

