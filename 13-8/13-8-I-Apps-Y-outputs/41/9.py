
def reconstruct_equation(numbers):
    num1, num2, num3 = map(int, numbers.split())
    for operation in "+-*/":
        for i in range(1, 4):
            if eval(f"{num1}{operation}{num2}{operation}{num3}"):
                return f"{num1}{operation}{num2}={num3}"

