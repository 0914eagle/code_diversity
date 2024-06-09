
def solve(k):
    a, b = 0, 0
    for i in range(k):
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    return a, b

