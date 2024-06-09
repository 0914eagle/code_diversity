
import math

def solve(a, b):
    real_a, imag_a = map(float, a.split())
    real_b, imag_b = map(float, b.split())
    c = complex(real_a, imag_a)
    d = complex(real_b, imag_b)
    print(f"{c+d:.2f} {c-d:.2f} {c*d:.2f} {c/d:.2f} {math.fmod(c, d):.2f} {math.fmod(d, c):.2f}")

