
def reconstruct_equation(numbers):
    num1, num2, num3 = map(int, numbers.split())
    for operation in "+-*/":
        for x in (num1, num2, num3):
            for y in (num1, num2, num3):
                if x != y and eval(f"{x} {operation} {y} {operation} {num3}") == 0:
                    return f"{x} {operation} {y} = {num3}"

