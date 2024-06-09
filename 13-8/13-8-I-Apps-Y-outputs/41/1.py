
def reconstruct_equation(numbers):
    num1, num2, num3 = map(int, numbers.split())
    for operation in ["+", "-", "*", "/"]:
        for i in range(1, 10):
            if eval(f"{num1} {operation} {i} {operation} {num2} {operation} {num3}"):
                return f"{num1} {operation} {i} = {num2} {operation} {num3}"

