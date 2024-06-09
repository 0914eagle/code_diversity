
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

def solve(arr):
    C = Complex(arr[0], arr[1])
    D = Complex(arr[2], arr[3])
    print(f"{C+D}")
    print(f"{C-D}")
    print(f"{C*D}")
    print(f"{C/D}")
    print(f"{C.mod()}")
    print(f"{D.mod()}")

arr = list(map(float, input().split()))
solve(arr)

