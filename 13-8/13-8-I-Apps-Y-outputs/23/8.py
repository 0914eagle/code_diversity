
def solve(a):
    n = len(a)
    increasing = []
    decreasing = []
    for i in range(n):
        if a[i] not in increasing and a[i] not in decreasing:
            increasing.append(a[i])
        elif a[i] in increasing:
            increasing.remove(a[i])
            decreasing.append(a[i])
        elif a[i] in decreasing:
            decreasing.remove(a[i])
            increasing.append(a[i])
    if len(increasing) + len(decreasing) == n:
        return "YES"
    else:
        return "NO"

