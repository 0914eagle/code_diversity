
def get_minimum_pieces(a, b):
    # Find the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    # Return the least common multiple of a and b divided by the gcd
    return (a * b) // gcd

def _get_gcd(a, b):
    if b == 0:
        return a
    else:
        return _get_gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_minimum_pieces(a, b))

