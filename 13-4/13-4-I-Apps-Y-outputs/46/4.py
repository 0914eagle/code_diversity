
import math

def solve(C, D):
    C_real, C_imag = C
    D_real, D_imag = D
    C_plus_D = C_real + D_real, C_imag + D_imag
    C_minus_D = C_real - D_real, C_imag - D_imag
    C_times_D = (C_real * D_real - C_imag * D_imag, C_real * D_imag + C_imag * D_real)
    C_div_D = (C_real * D_real + C_imag * D_imag) / (D_real ** 2 + D_imag ** 2), (C_imag * D_real - C_real * D_imag) / (D_real ** 2 + D_imag ** 2)
    C_mod = math.sqrt(C_real ** 2 + C_imag ** 2)
    D_mod = math.sqrt(D_real ** 2 + D_imag ** 2)
    return C_plus_D, C_minus_D, C_times_D, C_div_D, C_mod, D_mod

