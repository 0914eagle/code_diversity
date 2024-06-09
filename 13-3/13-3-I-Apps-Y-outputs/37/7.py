
def get_perimeter(a, b):
    # Find the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    # Return the perimeter of the rectangle with sides a/gcd and b/gcd
    return (a//gcd) + (b//gcd)

def _get_gcd(a, b):
    if b == 0:
        return a
    else:
        return _get_gcd(b, a%b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_perimeter(a, b))

