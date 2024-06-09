
def polynomial_plotting(n, *coefficients):
    coefficients = list(coefficients)
    constants = [0] * (n+1)
    constants[0] = coefficients[0]
    for i in range(1, n+1):
        constants[i] = constants[i-1] + coefficients[i]
    return " ".join(str(c) for c in constants)

