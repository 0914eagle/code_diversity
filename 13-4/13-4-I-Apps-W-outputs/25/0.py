
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_max_gcd(a):
    max_gcd = 0
    for b in range(1, a):
        gcd = get_gcd(a ^ b, a & b)
        if gcd > max_gcd:
            max_gcd = gcd
    return max_gcd

def main():
    q = int(input())
    for _ in range(q):
        a = int(input())
        print(get_max_gcd(a))

if __name__ == '__main__':
    main()

