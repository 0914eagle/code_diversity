
def reconstruct_equation(numbers):
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                for operation in ["+", "-", "*", "/"]:
                    if eval(str(num1) + operation + str(num2)) == num3:
                        return str(num1) + operation + str(num2) + "=" + str(num3)

