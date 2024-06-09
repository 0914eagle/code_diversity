
def polynomial_plotting(n, *coefficients):
    # Initialize the constants C_0, C_1, ..., C_n
    C = [0] * (n+1)
    C[0] = coefficients[n]
    for i in range(1, n+1):
        C[i] = C[i-1] + coefficients[n-i]
    return C

