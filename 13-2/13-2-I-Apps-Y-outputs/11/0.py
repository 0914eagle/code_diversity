
def solve(A, B):
    # Find the greatest common divisor of A and B
    gcd = find_gcd(A, B)
    # Return the minimum number of pieces that can be evenly distributed to the guests
    return A * B // gcd

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

