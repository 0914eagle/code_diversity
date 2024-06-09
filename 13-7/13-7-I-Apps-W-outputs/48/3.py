
def solve(a1, b1, a2, b2, L, R):
    # Find the greatest common divisor of a1 and a2
    gcd = find_gcd(a1, a2)

    # Divide a1 and a2 by their GCD
    a1 //= gcd
    a2 //= gcd

    # Find the least common multiple of a1 and a2
    lcm = a1 * a2 // find_gcd(a1, a2)

    # Find the number of integers x such that L ≤ x ≤ R and x = a1k' + b1 = a2l' + b2, for some integers k', l' ≥ 0
    count = 0
    for k in range(L // a1, R // a1 + 1):
        for l in range(L // a2, R // a2 + 1):
            if a1 * k + b1 == a2 * l + b2:
                count += 1

    return count

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

