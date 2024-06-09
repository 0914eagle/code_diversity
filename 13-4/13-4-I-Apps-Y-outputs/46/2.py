
import math

def solve(numbers):
    C, D = numbers
    C = C.split()
    D = D.split()
    A, B = C
    a, b = D
    addition = str(float(A) + float(a)) + "+" + str(float(B) + float(b)) + "i"
    subtraction = str(float(A) - float(a)) + "+" + str(float(B) - float(b)) + "i"
    multiplication = str(float(A) * float(a) - float(B) * float(b)) + "+" + str(float(A) * float(b) + float(B) * float(a)) + "i"
    division = str(float(A) * float(a) + float(B) * float(b)) + "/" + str(float(a) ** 2 + float(b) ** 2)
    modulus_C = str(math.sqrt(float(A) ** 2 + float(B) ** 2))
    modulus_D = str(math.sqrt(float(a) ** 2 + float(b) ** 2))
    return [addition, subtraction, multiplication, division, modulus_C, modulus_D]

