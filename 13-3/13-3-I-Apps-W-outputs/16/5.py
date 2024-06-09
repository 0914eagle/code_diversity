
def f(p, a):
    # Initialize the coefficients of the polynomial
    b = [0] * (p - 1)

    # Iterate through each coefficient
    for i in range(p - 1):
        # Calculate the value of the polynomial at i
        val = 0
        for j in range(p - 1):
            val += a[j] * b[p - 2 - j]
        val = val % p

        # Update the coefficient
        b[i] = (val - a[i]) % p

    return b

