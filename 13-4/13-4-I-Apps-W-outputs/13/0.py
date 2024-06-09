
def restore_sequence(f, b):
    n = len(f)
    m = len(b)
    if n != m:
        return "Impossible"
    count = [0] * (n + 1)
    for i in range(m):
        count[f[i]] += 1
        if count[f[i]] > 1:
            return "Ambiguity"
    for i in range(m):
        if count[b[i]] != 1:
            return "Impossible"
    a = [0] * m
    for i in range(m):
        a[i] = b.index(f[i]) + 1
    return "Possible\n" + " ".join(str(x) for x in a)

