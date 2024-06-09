
def f(p, a):
    # Initialize the coefficients of the polynomial
    b = [0] * (p - 1)

    # Iterate through each coefficient
    for i in range(p - 1):
        # Find the value of the polynomial at position i
        val = 0
        for j in range(p - 1):
            val += a[j] * b[p - 2 - j]
        val = val % p

        # Set the coefficient of the polynomial at position i
        b[i] = (val + p - a[i]) % p

    return b

