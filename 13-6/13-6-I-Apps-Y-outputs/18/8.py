
def solve(l1, r1, l2, r2):
    # Find the largest integer that is less than or equal to the ratio of the lengths of the two segments
    a = int((l1 + r1) / 2)
    b = int((l2 + r2) / 2)
    # Make sure that a and b are within the respective ranges
    a = max(a, l1)
    a = min(a, r1)
    b = max(b, l2)
    b = min(b, r2)
    # Make sure that a and b are not equal
    if a == b:
        if a == l1:
            b += 1
        else:
            a += 1
    return [a, b]

