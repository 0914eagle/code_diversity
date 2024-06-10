
def get_minimum_pieces(a, b):
    # Find the smallest number that is a common multiple of a and b
    lcm = a * b // gcd(a, b)
    return lcm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_minimum_pieces(a, b))

