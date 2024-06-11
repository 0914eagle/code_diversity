def do_algebra(operator, operand):
    
    if len(operator) == 0:
        return None
    if len(operand) < 2:
        return None
    if len(operator) != len(operand) - 1:
        return None
    if len(operator) == 1:
        return operand[0]
    if len(operator) == 2:
        return operand[0] + operand[1]
    if len(operator) == 3:
        return operand[0] + operand[1] * operand[2]
    if len(operator) == 4:
        return operand[0] + operand[1] * operand[2] - operand[3]
    if len(operator) == 5:
        return operand[0] + operand[1] * operand[2] - operand[3] // operand[4]
    if len(operator) == 6:
        return operand[0] + operand[1] * operand[2] - operand[3] // operand[4] ** operand[5]
    return None


