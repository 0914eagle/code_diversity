
def restore_sequence(f, b):
    n = len(f)
    m = len(b)
    if n != m:
        return "Impossible"
    count = [0] * (n + 1)
    for i in range(m):
        count[b[i]] += 1
    for i in range(n):
        if count[i] != 1:
            return "Ambiguity"
    a = [""] * m
    for i in range(m):
        a[i] = str(f.index(b[i]) + 1)
    return "Possible\n" + " ".join(a)

