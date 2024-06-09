
def reconstruct_equation(numbers):
    for operation in ['+', '-', '*', '/']:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    num1 = numbers[i]
                    num2 = numbers[j]
                    result = numbers[(i+j)%2]
                    if str(eval(str(num1) + operation + str(num2))) == str(result):
                        return str(num1) + operation + str(num2) + '=' + str(result)
    return -1

