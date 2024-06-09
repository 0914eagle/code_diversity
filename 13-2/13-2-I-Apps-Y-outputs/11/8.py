
def solve(A, B):
    # Calculate the greatest common divisor (gcd) of A and B
    gcd = gcd_calc(A, B)
    # Return the minimum number of pieces that can be evenly distributed to the guests
    return A * B // gcd

def gcd_calc(a, b):
    if b == 0:
        return a
    else:
        return gcd_calc(b, a % b)

