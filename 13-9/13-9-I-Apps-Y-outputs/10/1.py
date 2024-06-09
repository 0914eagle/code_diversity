
def solve(q, l1, r1, l2, r2):
    a = (l1 + r1) // 2
    b = (l2 + r2) // 2
    while a == b:
        if a == r1:
            a = l1
        else:
            a += 1
        if b == r2:
            b = l2
        else:
            b += 1
    return [a, b]

