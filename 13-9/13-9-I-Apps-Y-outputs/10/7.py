
def solve(l1, r1, l2, r2):
    a = (l1 + r1) // 2
    b = (l2 + r2) // 2
    if a == b:
        if a == l1:
            b = r1
        else:
            a = l1
    return a, b

