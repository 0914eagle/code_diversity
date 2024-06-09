
def solve(s):
    a = [s]
    i = 1
    while True:
        if a[i] in a:
            return i
        if a[i] % 2 == 0:
            a.append(a[i] // 2)
        else:
            a.append(3 * a[i] + 1)
        i += 1

