
def solve(s):
    n = len(s)
    counts = [0] * n
    counts[0] = 1
    counts[n-1] = 1
    for i in range(1, n-1):
        if s[i] == "L":
            counts[i] = counts[i-1]
        else:
            counts[i] = counts[i+1]
    return counts

