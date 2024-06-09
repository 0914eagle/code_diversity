
def solve(l1, r1, l2, r2):
    a = (l1 + r1) // 2
    b = (l2 + r2) // 2
    if a == b:
        if a == l1:
            a += 1
        else:
            a -= 1
    return a, b

