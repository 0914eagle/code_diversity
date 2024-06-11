def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise ValueError('The length of operator list is not equal to the length of operand list minus one.')
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

