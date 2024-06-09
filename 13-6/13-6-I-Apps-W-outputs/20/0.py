
def find_seals(doors):
    result = []
    for door in doors:
        n = door[0]
        a = door[1]
        b = []
        for i in range(1, n+1):
            b.append(i)
        result.append(b)
    return result

