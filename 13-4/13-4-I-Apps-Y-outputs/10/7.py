
def solve(A, B, C, D):
    count = 0
    for i in range(A, B+1):
        if i % C != 0 and i % D != 0:
            count += 1
    return count

