def do_algebra(operator, operand):
    
    if len(operator) == 0:
        return operand[0]
    elif len(operator) == 1:
        return operator[0] * operand[0]
    elif len(operator) == 2:
        return operator[0] * operand[0] + operator[1] * operand[1]
    else:
        return operator[0] * operand[0] + operator[1] * operand[1] + operator[2] * operand[2]


