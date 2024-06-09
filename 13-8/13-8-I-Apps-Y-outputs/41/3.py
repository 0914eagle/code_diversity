
def reconstruct_equation(numbers):
    for operation in ["+", "-", "*", "/"]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    result = str(numbers[i]) + operation + str(numbers[j])
                    if eval(result) == numbers[2]:
                        return result + "=" + str(numbers[2])

