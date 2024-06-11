def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise ValueError('operator and operand lists must have the same length')
    if len(operator) == 0:
        raise ValueError('operator list cannot be empty')
    if len(operator) == 1:
        return operand[0]
    if operator[0] == '+':
        return do_algebra(operator[1:], operand) + do_algebra(operator[1:], operand)
    if operator[0] == '-':
        return do_algebra(operator[1:], operand) - do_algebra(operator[1:], operand)
    if operator[0] == '*':
        return do_algebra(operator[1:], operand) * do_algebra(operator[1:], operand)
    if operator[0] == '/':
        return do_algebra(operator[1:], operand) // do_algebra(operator[1:], operand)
    if operator[0] == '**':
        return do_algebra(operator[1:], operand) ** do_algebra(operator[1:], operand)
    raise ValueError('unknown operator')


