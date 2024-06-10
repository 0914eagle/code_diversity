
def min_snacks(A, B):
    # Find the greatest common divisor (gcd) of A and B
    gcd = _gcd(A, B)
    # The minimum number of snacks is the product of gcd and the sum of A and B divided by 2
    return (gcd * (A + B)) // 2

def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(min_snacks(A, B))

