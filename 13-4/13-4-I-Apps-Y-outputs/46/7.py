
import math
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
        imag = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
        return Complex(real, imag)

    def mod(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

def print_complex(num):
    if num.real == 0 and num.imag == 0:
        return "0.00+0.00i"
    elif num.real == 0 and num.imag != 0:
        return "0.00+{:.2f}i".format(num.imag)
    elif num.real != 0 and num.imag == 0:
        return "{:.2f}+0.00i".format(num.real)
    else:
        if num.imag < 0:
            return "{:.2f}-{:.2f}i".format(num.real, abs(num.imag))
        else:
            return "{:.2f}+{:.2f}i".format(num.real, num.imag)

# Read input
line = input().split()
a, b = float(line[0]), float(line[1])
c, d = float(line[2]), float(line[3])

# Create complex numbers
num1 = Complex(a, b)
num2 = Complex(c, d)

# Perform operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod1 = num1.mod()
mod2 = num2.mod()

# Print output
print(print_complex(add))
print(print_complex(sub))
print(print_complex(mul))
print(print_complex(div))
print("{:.2f}".format(mod1))
print("{:.2f}".format(mod2))

