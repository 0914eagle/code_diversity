
def f1(h1, a1, x1, y1, h2, a2, x2, y2):
    # find the gcd of x1, y1, x2, and y2
    gcd = find_gcd(x1, y1, x2, y2)
    # divide x1, y1, x2, and y2 by their gcd
    x1 //= gcd
    y1 //= gcd
    x2 //= gcd
    y2 //= gcd
    # find the least common multiple of x1, y1, x2, and y2
    lcm = find_lcm(x1, y1, x2, y2)
    # calculate the minimum time it takes for Xaniar to reach a1
    t1 = (a1 - h1) * lcm // gcd
    # calculate the minimum time it takes for Abol to reach a2
    t2 = (a2 - h2) * lcm // gcd
    # return the minimum of t1 and t2
    return min(t1, t2)

def f2(h1, a1, x1, y1, h2, a2, x2, y2):
    # find the gcd of x1, y1, x2, and y2
    gcd = find_gcd(x1, y1, x2, y2)
    # divide x1, y1, x2, and y2 by their gcd
    x1 //= gcd
    y1 //= gcd
    x2 //= gcd
    y2 //= gcd
    # find the least common multiple of x1, y1, x2, and y2
    lcm = find_lcm(x1, y1, x2, y2)
    # calculate the minimum time it takes for Xaniar to reach a1
    t1 = (a1 - h1) * lcm // gcd
    # calculate the minimum time it takes for Abol to reach a2
    t2 = (a2 - h2) * lcm // gcd
    # return the minimum of t1 and t2
    return min(t1, t2)

def find_gcd(x1, y1, x2, y2):
    # find the gcd of x1 and y1
    gcd = gcd_euclid(x1, y1)
    # find the gcd of x2 and y2
    gcd2 = gcd_euclid(x2, y2)
    # return the lcm of gcd and gcd2
    return lcm_euclid(gcd, gcd2)

def find_lcm(x1, y1, x2, y2):
    # find the lcm of x1 and y1
    lcm = lcm_euclid(x1, y1)
    # find the lcm of x2 and y2
    lcm2 = lcm_euclid(x2, y2)
    # return the lcm of lcm and lcm2
    return lcm_euclid(lcm, lcm2)

def gcd_euclid(a, b):
    # find the gcd of a and b using the Euclidean algorithm
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)

def lcm_euclid(a, b):
    # find the lcm of a and b using the Euclidean algorithm
    return a * b // gcd_euclid(a, b)

if __name__ == '__main__':
    h1, a1, x1, y1, h2, a2, x2, y2 = map(int, input().split())
    print(f1(h1, a1, x1, y1, h2, a2, x2, y2))

