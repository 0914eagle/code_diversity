
def get_perimeter(a, b):
    # Find the greatest common divisor of a and b
    gcd = get_gcd(a, b)
    # Return the perimeter as the product of a and b divided by their gcd
    return a * b // gcd

def get_gcd(a, b):
    # Base case: if b is 0, the gcd is a
    if b == 0:
        return a
    # Recursive case: divide a and b by their gcd and find the gcd of the results
    return get_gcd(b, a % b)

def main():
    a, b = map(int, input().split())
    print(get_perimeter(a, b))

if __name__ == '__main__':
    main()

