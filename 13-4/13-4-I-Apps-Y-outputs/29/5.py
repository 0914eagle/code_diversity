
def get_constants(n, *coefficients):
    constants = [0] * (n+1)
    constants[0] = coefficients[n]
    for i in range(1, n+1):
        constants[i] = constants[i-1] + coefficients[n-i]
    return constants

