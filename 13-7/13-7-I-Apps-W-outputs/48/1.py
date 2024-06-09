
def solve(a1, b1, a2, b2, L, R):
    count = 0
    for k in range(L//a1):
        for l in range(R//a2):
            if a1*k + b1 == a2*l + b2:
                count += 1
    return count

