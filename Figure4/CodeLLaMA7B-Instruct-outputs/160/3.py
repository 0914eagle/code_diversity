

def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list must be one less than the length of operand list")
    if not all(isinstance(x, int) and x >= 0 for x in operand):
        raise ValueError("Operand list must contain only non-negative integers")
    if len(operator) == 0:
        raise ValueError("Operator list must have at least one operator")

    result = operand[0]
    for i in range(len(operator)):
        result = result + operator[i] * operand[i + 1]

    return result


