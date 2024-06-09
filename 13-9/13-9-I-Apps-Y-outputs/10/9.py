
def solve(l1, r1, l2, r2):
    # Find the smallest integer greater than or equal to the left endpoint of the first segment
    a = int(l1) + 1
    # Find the smallest integer greater than or equal to the left endpoint of the second segment
    b = int(l2) + 1
    # If the right endpoint of the first segment is less than or equal to the left endpoint of the second segment, then swap them
    if r1 <= l2:
        a, b = b, a
    return a, b

