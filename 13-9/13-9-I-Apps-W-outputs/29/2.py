
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_greatest_common_divisor(a, b):
    gcd = get_gcd(a, b)
    for i in range(a, b+1):
        if i % gcd != 0:
            return gcd
    return gcd

def input_numbers():
    a, b = map(int, input().split())
    return a, b

def main():
    a, b = input_numbers()
    print(get_greatest_common_divisor(a, b))

if __name__ == '__main__':
    main()

