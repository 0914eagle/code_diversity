
def get_perimeter(a, b):
    # Find the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    
    # Divide a and b by their gcd
    a //= gcd
    b //= gcd
    
    # Find the least common multiple of a and b
    lcm = a * b // _get_gcd(a, b)
    
    # Return the perimeter of the rectangle with sides a and b
    return 2 * (a + b + lcm)

def _get_gcd(a, b):
    if b == 0:
        return a
    else:
        return _get_gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_perimeter(a, b))

