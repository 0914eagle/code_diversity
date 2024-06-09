
def find_minimum_pieces(a, b):
    lcm = a * b // gcd(a, b)
    return lcm

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = find_minimum_pieces(a, b)
    print(result)
