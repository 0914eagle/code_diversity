
import math

def solve(numbers):
    # Split the input into two complex numbers
    num1, num2 = numbers.split(" ")

    # Convert the input to complex numbers
    num1 = complex(num1)
    num2 = complex(num2)

    # Perform the operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    modulus_num1 = math.fabs(num1)
    modulus_num2 = math.fabs(num2)

    # Format the output
    output = ""
    output += "{:.2f} {:+.2f}i\n".format(addition.real, addition.imag)
    output += "{:.2f} {:+.2f}i\n".format(subtraction.real, subtraction.imag)
    output += "{:.2f} {:+.2f}i\n".format(multiplication.real, multiplication.imag)
    output += "{:.2f} {:+.2f}i\n".format(division.real, division.imag)
    output += "{:.2f}\n".format(modulus_num1)
    output += "{:.2f}\n".format(modulus_num2)

    return output

