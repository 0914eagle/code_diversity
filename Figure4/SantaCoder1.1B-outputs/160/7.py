def do_algebra(operator, operand):
    
    if len(operator) == 1:
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
            raise ValueError('Invalid operator')
    else:
        if operator[0] == '+':
            return do_algebra(operator[1:], operand) + do_algebra(operator[1:], operand)
        elif operator[0] == '-':
            return do_algebra(operator[1:], operand) - do_algebra(operator[1:], operand)
        elif operator[0] == '*':
            return do_algebra(operator[1:], operand) * do_algebra(operator[1:], operand)
        elif operator[0] == '//':
            return do_algebra(operator[1:], operand) // do_algebra(operator[1:], operand)
        elif operator[0] == '**':
            return do_algebra(operator[1:], operand) ** do_algebra(operator[1:], operand)
        else:
            raise ValueError('Invalid operator')


