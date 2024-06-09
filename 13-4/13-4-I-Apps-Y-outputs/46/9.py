
import math

def solve(a, b):
    # Convert the inputs to complex numbers
    c = complex(a[0], a[1])
    d = complex(b[0], b[1])
    
    # Calculate the results
    addition = c + d
    subtraction = c - d
    multiplication = c * d
    division = c / d
    modulus_c = math.fabs(c)
    modulus_d = math.fabs(d)
    
    # Format the output
    output = []
    output.append("{:.2f}+{:.2f}i".format(addition.real, addition.imag))
    output.append("{:.2f}-{:.2f}i".format(subtraction.real, subtraction.imag))
    output.append("{:.2f}+{:.2f}i".format(multiplication.real, multiplication.imag))
    output.append("{:.2f}+{:.2f}i".format(division.real, division.imag))
    output.append("{:.2f}".format(modulus_c))
    output.append("{:.2f}".format(modulus_d))
    
    return output

