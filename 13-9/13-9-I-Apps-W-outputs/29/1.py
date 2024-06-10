
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_gcd_range(a, b):
    gcd_value = gcd(a, b)
    return gcd_value

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_gcd_range(a, b))

