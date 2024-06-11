def do_algebra(operator, operand):
    
    if len(operator) == 0:
        return operand[0]
    elif len(operator) == 1:
        return operator[0] * operand[0]
    else:
        return operator[0] * do_algebra(operator[1:], operand[1:])

