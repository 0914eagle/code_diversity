
def solve(x1, x2, x3, x4):
    # Find the sum of all three numbers
    sum_abc = x1 + x2 + x3

    # Find the two pairs that add up to the sum of all three numbers
    pair1 = (sum_abc - x1, sum_abc - x2)
    pair2 = (sum_abc - x1, sum_abc - x3)

    # Find the number that is not part of either pair
    num = [x for x in [x1, x2, x3] if x not in pair1 and x not in pair2][0]

    # Return the numbers in any order
    return num, pair1[0], pair1[1]

