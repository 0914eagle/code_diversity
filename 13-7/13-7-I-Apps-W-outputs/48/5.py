
def solve(a1, b1, a2, b2, L, R):
    # Find the greatest common divisor of a1 and a2
    gcd = find_gcd(a1, a2)

    # Divide a1 and a2 by their GCD
    a1 //= gcd
    a2 //= gcd

    # Find the least common multiple of a1 and a2
    lcm = a1 * a2 // gcd

    # Find the number of integers x such that L ≤ x ≤ R and x = a1k + b1 = a2l + b2, for some integers k, l ≥ 0
    count = 0
    for k in range(L // lcm, R // lcm + 1):
        for l in range(L // lcm, R // lcm + 1):
            x = a1 * k + b1
            y = a2 * l + b2
            if x == y:
                count += 1

    return count

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

