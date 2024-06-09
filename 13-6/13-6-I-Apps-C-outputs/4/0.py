
def solve(n):
    if n == 1:
        return "YES"
    else:
        swaps = []
        for i in range(n-1):
            for j in range(i+1, n):
                swaps.append([i, j])
        if len(swaps) % 2 == 0:
            return "YES"
        else:
            return "NO"

