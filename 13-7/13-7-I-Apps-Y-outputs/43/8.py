
def solve(x1, x2, x3, x4):
    # Find the sum of all three numbers
    sum_abc = x1 + x2 + x3

    # Find the pairwise sums
    a_plus_b = x1
    a_plus_c = x2
    b_plus_c = x3

    # Find the difference between the sum of all three numbers and the pairwise sums
    diff = sum_abc - a_plus_b - a_plus_c - b_plus_c

    # Find the value of the missing number
    missing_number = diff // 2

    # Find the values of a, b, and c
    a = a_plus_b - missing_number
    b = a_plus_c - missing_number
    c = b_plus_c - missing_number

    return a, b, c

