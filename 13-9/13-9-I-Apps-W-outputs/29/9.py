
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_gcd_efficient(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return get_gcd_efficient(a - b, b)
    else:
        return get_gcd_efficient(a, b - a)

def main():
    a, b = map(int, input().split())
    print(get_gcd_efficient(a, b))

if __name__ == '__main__':
    main()

