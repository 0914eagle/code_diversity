
def find_minimum_pieces(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return a * b // gcd(a, b)

# Read input
a, b = map(int, input().split())

# Find and print the minimum number of pieces
print(find_minimum_pieces(a, b))
