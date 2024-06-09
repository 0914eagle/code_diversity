
def reconstruct_equation(numbers):
    for operation in ["+", "-", "*", "/"]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    eq = str(numbers[i]) + operation + str(numbers[j]) + "=" + str(numbers[i+j])
                    if eval(eq):
                        return eq
    return "No solution found."

