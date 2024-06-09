
def solve(x1, x2, x3, x4):
    # Find the sum of all three numbers
    sum_abc = x1 + x2 + x3

    # Find the pairwise sums
    a_b = x1 - x2
    a_c = x1 - x3
    b_c = x2 - x3

    # Find the greatest common divisor (gcd) of the pairwise sums
    gcd_ab = gcd(a_b, b_c)

    # Find the least common multiple (lcm) of the pairwise sums
    lcm_ab = lcm(a_b, b_c)

    # Find the three numbers
    a = lcm_ab // gcd_ab
    b = (sum_abc - a) // 2
    c = sum_abc - a - b

    return a, b, c

