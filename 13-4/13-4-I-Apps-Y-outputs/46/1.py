
import math

def solve(numbers):
    num1, num2 = numbers.split()
    num1_real, num1_img = num1.split('+')
    num2_real, num2_img = num2.split('+')
    num1_real, num1_img, num2_real, num2_img = float(num1_real), float(num1_img), float(num2_real), float(num2_img)
    add = complex(num1_real + num2_real, num1_img + num2_img)
    sub = complex(num1_real - num2_real, num1_img - num2_img)
    mul = complex(num1_real * num2_real - num1_img * num2_img, num1_real * num2_img + num1_img * num2_real)
    div = complex(num1_real * num2_real + num1_img * num2_img, num1_img * num2_real - num1_real * num2_img) / (num2_real ** 2 + num2_img ** 2)
    mod_num1 = math.sqrt(num1_real ** 2 + num1_img ** 2)
    mod_num2 = math.sqrt(num2_real ** 2 + num2_img ** 2)
    return f"{add.real:.2f}+{add.imag:.2f}i\n{sub.real:.2f}+{sub.imag:.2f}i\n{mul.real:.2f}+{mul.imag:.2f}i\n{div.real:.2f}+{div.imag:.2f}i\n{mod_num1:.2f}\n{mod_num2:.2f}"

