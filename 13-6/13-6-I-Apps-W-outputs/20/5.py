
def find_seals(doors):
    solutions = []
    for door in doors:
        n = door[0]
        a = door[1]
        b = [0] * n
        for i in range(n):
            b[i] = -a[i]
        solutions.append(b)
    return solutions

