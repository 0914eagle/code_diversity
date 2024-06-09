
def f1(p, k):
    if p == 0:
        return 1, [0]
    if k == 1:
        return -1
    for d in range(1, 1001):
        for coeffs in itertools.product(range(k), repeat=d):
            poly = [c % k for c in coeffs]
            if poly[-1] == 0:
                continue
            remainder = poly[-1]
            for i in range(d-1):
                remainder = (remainder * k + poly[i]) % k
            if remainder == p:
                return d, poly
    return -1, None

def f2(p, k):
    d, poly = f1(p, k)
    if d == -1:
        return -1
    return d, poly

if __name__ == '__main__':
    p, k = map(int, input().split())
    d, poly = f2(p, k)
    if d == -1:
        print(-1)
    else:
        print(d)
        print(*poly)

