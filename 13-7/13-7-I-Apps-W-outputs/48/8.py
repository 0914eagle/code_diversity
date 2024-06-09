
def solve(a1, b1, a2, b2, L, R):
    # Find the greatest common divisor (gcd) of a1 and a2
    gcd = get_gcd(a1, a2)

    # Divide a1 and a2 by their gcd
    a1 //= gcd
    a2 //= gcd

    # Find the least common multiple (lcm) of a1 and a2
    lcm = get_lcm(a1, a2)

    # Divide L and R by the lcm
    L //= lcm
    R //= lcm

    # Initialize the count of integers x
    count = 0

    # Iterate over all possible values of k' and l'
    for k in range(L, R + 1):
        for l in range(L, R + 1):
            # Check if a1k' + b1 = a2l' + b2
            if a1 * k + b1 == a2 * l + b2:
                count += 1

    return count

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

def get_lcm(a, b):
    return a * b // get_gcd(a, b)

