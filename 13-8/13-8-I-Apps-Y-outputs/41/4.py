
def reconstruct_equation(numbers):
    num1, num2, num3 = map(int, numbers.split())
    for operation in "+-*/":
        for eq in (f"{num1}{operation}{num2}={num3}", f"{num2}{operation}{num1}={num3}", f"{num1}{operation}{num3}={num2}"):
            if eval(eq) == True:
                return eq
    return "No solution"

