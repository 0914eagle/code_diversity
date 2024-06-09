
def solve(p, a):
    # Initialize the coefficients of the polynomial
    b = [0] * (p-1)

    # Iterate over each coefficient
    for i in range(p-1):
        # Find the value of the polynomial at i
        f_i = 0
        for j in range(p-1):
            f_i += b[j] * a[i-j]
        f_i %= p

        # Update the coefficient
        b[i] = (f_i - a[i]) % p

    return b

