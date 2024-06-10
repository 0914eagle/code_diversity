
def get_perimeter(a, b):
    # Find the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    
    # Calculate the number of red tiles needed to form a rectangle
    red_tiles = a // gcd
    
    # Calculate the number of blue tiles needed to form a rectangle
    blue_tiles = b // gcd
    
    # Calculate the perimeter of the rectangle
    perimeter = 2 * (red_tiles + blue_tiles)
    
    return perimeter

def _get_gcd(a, b):
    if b == 0:
        return a
    else:
        return _get_gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_perimeter(a, b))

