
def spongebob_prank(f, b):
    n = len(f)
    m = len(b)
    if n != m:
        return "Impossible"
    a = [0] * m
    for i in range(m):
        a[i] = f.index(b[i]) + 1
    for i in range(m):
        if a[i] != i + 1:
            return "Ambiguity"
    return "Possible\n" + " ".join(str(x) for x in a)

