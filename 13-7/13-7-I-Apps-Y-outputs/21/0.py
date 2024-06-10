
def get_min_snack_pieces(A, B):
    # Find the greatest common divisor (GCD) of A and B
    gcd = get_gcd(A, B)
    
    # Divide A and B by the GCD
    A_new = A // gcd
    B_new = B // gcd
    
    # Calculate the minimum number of snack pieces needed for both cases
    min_pieces = A_new * B_new
    
    return min_pieces

def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(get_min_snack_pieces(A, B))

