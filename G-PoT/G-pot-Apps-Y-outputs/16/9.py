
def find_min_pieces(A, B):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    return lcm(A, B)

# Read input
A, B = map(int, input().split())

# Find and print the minimum number of pieces
print(find_min_pieces(A, B))
