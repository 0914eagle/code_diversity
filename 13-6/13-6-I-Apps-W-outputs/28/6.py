
def get_gcd(a, b):
    if a == 0:
        return b
    return get_gcd(b % a, a)

def get_max_gcd(n):
    max_gcd = 1
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            gcd = get_gcd(i, j)
            if gcd > max_gcd:
                max_gcd = gcd
    return max_gcd

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_max_gcd(n))

if __name__ == '__main__':
    main()

