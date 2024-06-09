
def solve(x1, x2, x3, x4):
    # Find the sum of all three numbers
    sum_of_three = x1 + x2 + x3

    # Find the two pairs that add up to the sum of all three numbers
    pair1 = (sum_of_three - x1, sum_of_three - x2)
    pair2 = (sum_of_three - x1, sum_of_three - x3)

    # Find the number that is not part of either pair
    num = x4 - (pair1[0] + pair1[1])

    return num, pair1[0], pair1[1]

