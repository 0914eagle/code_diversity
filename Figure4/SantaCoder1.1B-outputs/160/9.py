def do_algebra(operator, operand):
    
    if len(operator) == 1:
        return operator[0]
    elif len(operator) == 2:
        return operator[0] + operator[1]
    else:
        if operator[0] == '+':
            return do_algebra(operator[1:], operand)
        elif operator[0] == '-':
            return do_algebra(operator[1:], operand)
        elif operator[0] == '*':
            return do_algebra(operator[1:], operand)
        elif operator[0] == '//':
            return do_algebra(operator[1:], operand)
        elif operator[0] == '**':
            return do_algebra(operator[1:], operand)
        else:
            return operator[0] + do_algebra(operator[1:], operand)


