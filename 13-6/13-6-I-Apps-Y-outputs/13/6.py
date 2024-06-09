
def reconstruct_equation(numbers):
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                for operation in ["+", "-", "*", "/"]:
                    equation = str(num1) + operation + str(num2) + "=" + str(num3)
                    if eval(equation) == num3:
                        return equation
    return "No solution found."

