
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def f(a):
    max_gcd = 0
    for b in range(1, a):
        gcd_ab = gcd(a ^ b, a & b)
        if gcd_ab > max_gcd:
            max_gcd = gcd_ab
    return max_gcd

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a = int(input())
        print(f(a))

