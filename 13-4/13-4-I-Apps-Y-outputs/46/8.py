
import math

def solve(C, D):
    C_real, C_imag = map(float, input().split())
    D_real, D_imag = map(float, input().split())
    
    C = C_real + C_imag * 1j
    D = D_real + D_imag * 1j
    
    print(f"{C+D:.2f}{C.imag>0 and '+' or '-'}{D.imag:.2f}i")
    print(f"{C-D:.2f}{C.imag>0 and '+' or '-'}{D.imag:.2f}i")
    print(f"{C*D:.2f}{C.imag>0 and '+' or '-'}{D.imag:.2f}i")
    print(f"{C/D:.2f}{C.imag>0 and '+' or '-'}{D.imag:.2f}i")
    print(f"{math.fmod(C, D):.2f}{C.imag>0 and '+' or '-'}{D.imag:.2f}i")
    print(f"{math.fmod(D, C):.2f}{D.imag>0 and '+' or '-'}{C.imag:.2f}i")

solve(C, D)

