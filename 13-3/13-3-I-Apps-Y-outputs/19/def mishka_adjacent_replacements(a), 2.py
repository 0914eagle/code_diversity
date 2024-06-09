
def mishka_adjacent_replacements(a):
    n = len(a)
    for i in range(1, 500000001):
        for j in range(1, n):
            if a[j] == 2*i-1:
                a[j] = 2*i
            elif a[j] == 2*i:
                a[j] = 2*i-1
    return a

