def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise Exception('operator and operand lists should have the same length')

    result = 0
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i]
        elif operator[i] == '-':
            result -= operand[i]
        elif operator[i] == '*':
            result *= operand[i]
        elif operator[i] == '/':
            result //= operand[i]
        elif operator[i] == '**':
            result **= operand[i]

    return result

