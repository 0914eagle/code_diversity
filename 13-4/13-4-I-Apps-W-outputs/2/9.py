
def solve(a, x):
    # Calculate the greatest common divisor (gcd) of the sequence
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd_recursive(gcd, a[i])

    # Initialize the result
    result = 0

    # Iterate through the queries and calculate the number of pairs (l, r) such that gcd(a_l, a_l + 1, ..., a_r) = x_i
    for i in range(len(x)):
        for l in range(len(a)):
            for r in range(l, len(a)):
                if gcd_recursive(gcd, a[l], a[l + 1], ..., a[r]) == x[i]:
                    result += 1

    return result

def gcd_recursive(a, b, *args):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b, *args)

