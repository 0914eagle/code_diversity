
def solve(l1, r1, l2, r2):
    # Find the largest integer that is less than or equal to the average of l1 and r1
    a = int(l1 + (r1 - l1) / 2)
    # Find the smallest integer that is greater than or equal to the average of l2 and r2
    b = int(r2 - (r2 - l2) / 2)
    # Make sure a and b are different
    if a == b:
        if a == l1:
            a += 1
        else:
            b -= 1
    return a, b

