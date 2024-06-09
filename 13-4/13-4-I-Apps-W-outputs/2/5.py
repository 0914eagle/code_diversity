
def solve(a, x):
    # Calculate the greatest common divisor (gcd) of the sequence
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd(gcd, a[i])

    # Initialize the result
    result = 0

    # Iterate through the queries
    for x_i in x:
        # Calculate the number of pairs (l, r) such that gcd(a_l, a_l + 1, ..., a_r) = x_i
        for l in range(len(a)):
            for r in range(l, len(a)):
                if gcd(a[l], a[l + 1], ..., a[r]) == x_i:
                    result += 1

        # Print the result
        print(result)


