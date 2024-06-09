
def reconstruct_equation(numbers):
    num1, num2, num3 = map(int, numbers.split())
    for operation in "+-*/":
        for result in (num1, num2, num3):
            for num in (num1, num2, num3):
                if operation == "+":
                    if num1 + num2 == result and num3 == num1 + num2:
                        return f"{num1} {operation} {num2} = {result}"
                elif operation == "-":
                    if num1 - num2 == result and num3 == num1 - num2:
                        return f"{num1} {operation} {num2} = {result}"
                elif operation == "*":
                    if num1 * num2 == result and num3 == num1 * num2:
                        return f"{num1} {operation} {num2} = {result}"
                elif operation == "/":
                    if num1 / num2 == result and num3 == num1 / num2:
                        return f"{num1} {operation} {num2} = {result}"
    return "Impossible"

