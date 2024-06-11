def do_algebra(operator, operand):
    
    # Your code here
    # print(operator)
    # print(operand)
    # print(len(operator))
    # print(len(operand))
    # print(len(operator) == len(operand) - 1)
    # print(len(operand) > 1)
    # print(all(isinstance(x, int) for x in operand))
    # print(all(x >= 0 for x in operand))
    # print(all(isinstance(x, str) for x in operator))
    # print(all(x in ['+', '-', '*', '//', '**'] for x in operator))
    if len(operator) == len(operand) - 1 and len(operand) > 1 and all(isinstance(x, int) for x in operand) and all(x >= 0 for x in operand) and all(isinstance(x, str) for x in operator) and all(x in ['+', '-', '*', '//', '**'] for x in operator):
        # print("ok")
        result = operand[0]
        for i in range(len(operator)):
            if operator[i] == '+':
                result += operand[i+1]
            elif operator[i] == '-':
                result -= operand[i+1]
            elif operator[i] == '*':
                result *= operand[i+1]
            elif operator[i] == '//':
                result //= operand[i+1]
            elif operator[i] == '**':
                result **= operand[i+1]
        return result
    else:
        return None


if