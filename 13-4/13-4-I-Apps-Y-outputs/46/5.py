
import math

def solve(numbers):
    num1, num2 = numbers.split()
    num1_real, num1_imag = num1.split('+')
    num2_real, num2_imag = num2.split('+')
    num1_real, num1_imag, num2_real, num2_imag = float(num1_real), float(num1_imag), float(num2_real), float(num2_imag)
    addition = complex(num1_real + num2_real, num1_imag + num2_imag)
    subtraction = complex(num1_real - num2_real, num1_imag - num2_imag)
    multiplication = complex(num1_real * num2_real - num1_imag * num2_imag, num1_real * num2_imag + num1_imag * num2_real)
    division = complex((num1_real * num2_real + num1_imag * num2_imag) / (num2_real ** 2 + num2_imag ** 2), (num1_imag * num2_real - num1_real * num2_imag) / (num2_real ** 2 + num2_imag ** 2))
    modulus_num1 = math.sqrt(num1_real ** 2 + num1_imag ** 2)
    modulus_num2 = math.sqrt(num2_real ** 2 + num2_imag ** 2)
    return f"{addition.real:.2f}{'+' if addition.imag >= 0 else '-'}{abs(addition.imag):.2f}i\n{subtraction.real:.2f}{'+' if subtraction.imag >= 0 else '-'}{abs(subtraction.imag):.2f}i\n{multiplication.real:.2f}{'+' if multiplication.imag >= 0 else '-'}{abs(multiplication.imag):.2f}i\n{division.real:.2f}{'+' if division.imag >= 0 else '-'}{abs(division.imag):.2f}i\n{modulus_num1:.2f}\n{modulus_num2:.2f}"

