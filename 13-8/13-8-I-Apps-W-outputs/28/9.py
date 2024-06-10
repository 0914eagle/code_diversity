
def get_interval(a, b):
    # Find the smallest number that is common to both a and b
    gcd = a * b // __gcd(a, b)
    # Check if the number is a power of 2
    if gcd & (gcd - 1) == 0:
        return "YES"
    else:
        return "NO"

def main():
    a, b = map(int, input().split())
    print(get_interval(a, b))

if __name__ == '__main__':
    main()

