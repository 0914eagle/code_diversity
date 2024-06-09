
def solve(a, x):
    # Calculate the greatest common divisor (gcd) of the elements in a
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd(gcd, a[i])

    # Count the number of pairs (l, r) such that gcd(a_l, a_l + 1, ..., a_r) = x
    count = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if gcd(a[i], a[i+1], ..., a[j]) == x:
                count += 1

    return count

