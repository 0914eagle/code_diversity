def do_algebra(operator, operand):
    
    if len(operator) == 1:
        return operator[0]
    elif len(operator) == 2:
        if operator[0] == '+':
            return operand[0] + operand[1]
        elif operator[0] == '-':
            return operand[0] - operand[1]
        elif operator[0] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '//':
            return operand[0] // operand[1]
        elif operator[0] == '**':
            return operand[0] ** operand[1]
    else:
        raise Exception('Invalid operator list')


