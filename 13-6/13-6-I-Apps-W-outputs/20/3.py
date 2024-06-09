
def find_seals(doors):
    result = []
    for door in doors:
        n = door[0]
        a = door[1]
        b = [0] * n
        for i in range(n):
            b[i] = -a[i] // a[n-1]
        result.append(b)
    return result

