
def solve(f, b):
    n = len(f)
    m = len(b)
    if n != m:
        return "Impossible"
    count = [0] * (n + 1)
    for i in range(m):
        count[b[i]] += 1
    for i in range(1, n + 1):
        if count[i] != 1:
            return "Ambiguity"
    a = [0] * m
    for i in range(m):
        a[i] = f.index(b[i]) + 1
    return "Possible\n" + " ".join(str(x) for x in a)

