
def mishka_adjacent_replacements(a):
    n = len(a)
    for i in range(1, 500000001):
        for j in range(i, n, i):
            if a[j] == i:
                a[j] = i + 1
            if a[j] == i + 1:
                a[j] = i
    return a

