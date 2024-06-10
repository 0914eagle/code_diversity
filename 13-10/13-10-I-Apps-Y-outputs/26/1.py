
def get_rectangle_perimeter(a, b):
    # Find the greatest common divisor of a and b
    gcd = _get_gcd(a, b)
    
    # Divide a and b by their GCD
    a //= gcd
    b //= gcd
    
    # Check if a and b are both odd or both even
    if a % 2 == b % 2:
        # If they are both odd or both even, return their sum
        return a + b
    else:
        # If one is odd and the other is even, return their sum plus the smaller number
        return a + b + min(a, b)

def _get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a, b = map(int, input().split())
    print(get_rectangle_perimeter(a, b))

if __name__ == '__main__':
    main()

