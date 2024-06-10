
def get_min_pieces(A, B):
    # Find the greatest common divisor of A and B
    gcd = get_gcd(A, B)
    # Return the minimum number of pieces that can be divided evenly between A and B
    return (A // gcd) * (B // gcd)

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(get_min_pieces(A, B))

