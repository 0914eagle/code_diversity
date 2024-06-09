
def get_gcd(a, b):
    if a == 0:
        return b
    return get_gcd(b % a, a)

def solve(n):
    max_gcd = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            gcd = get_gcd(i, j)
            if gcd > max_gcd:
                max_gcd = gcd
    return max_gcd

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))

