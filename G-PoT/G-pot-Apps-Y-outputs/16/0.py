
def find_minimum_pieces(A, B):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    return lcm(A, B)

# Input
A, B = map(int, input().split())

# Output
print(find_minimum_pieces(A, B))
