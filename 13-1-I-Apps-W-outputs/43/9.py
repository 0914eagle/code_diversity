
def solve(p, a):
    # Initialize the coefficients of the polynomial
    b = [0] * (p-1)

    # Iterate over each coefficient
    for i in range(p-1):
        # Calculate the value of the polynomial at i
        val = 0
        for j in range(p-1):
            val += a[j] * b[i-j]
        val = val % p

        # Update the coefficient
        b[i] = (val + p) % p

    return b

