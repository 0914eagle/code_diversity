
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def f1(a1, b1, a2, b2, L, R):
    lcm_ab = lcm(a1, a2)
    gcd_ab = gcd(a1, a2)
    count = 0
    for x in range(L, R + 1):
        if x % gcd_ab == 0 and (x - b1) % a1 == 0 and (x - b2) % a2 == 0:
            count += 1
    return count

def f2(a1, b1, a2, b2, L, R):
    lcm_ab = lcm(a1, a2)
    gcd_ab = gcd(a1, a2)
    count = 0
    for x in range(L, R + 1):
        if x % gcd_ab == 0 and (x - b1) % a1 == 0 and (x - b2) % a2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    a1, b1, a2, b2, L, R = map(int, input().split())
    print(f1(a1, b1, a2, b2, L, R))

