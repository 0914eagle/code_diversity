def do_algebra(operator, operand):
    
    # If operand is empty, return 0
    if not operand:
        return 0

    # If operator is empty, return 1
    if not operator:
        return 1

    # If operand is a single integer, return it
    if len(operand) == 1:
        return operand[0]

    # If operator is a single integer, return it
    if len(operator) == 1:
        return operator[0]

    # If operand is a list of integers, operator is a list of strings, and operand is a list of strings,
    # return the evaluation of the expression
    if len(operand) == 2 and len(operator) == 2 and isinstance(operand[0], int) and isinstance(operator[0], str):
        return eval(operand[0] + operator[0] + operand[1])

    # If operand is a list of strings, operator is a list of integers, and operand is a list of strings,
    # return the evaluation of the expression
    if len(operand) == 2 and len(operator) == 2 and isinstance(operand[0], str) and isinstance(operator[0], int):
        return eval(operand[0] + operator[0] + operand[1])

    # If operand is a list of strings, operator is a list of strings, and operand is a list of integers,
    # return the evaluation of the expression
    if len(operand) == 2 and len(operator) == 2 and isinstance(operand[0], str) and isinstance(operator[0], str):
        return eval(operand[0] + operator[0] + operand[1])

    # If operand is a list of integers, operator is a list of strings, and operand is a list of integers,
    # return the evaluation of the expression
    if len(operand) == 2 and len(operator) == 2 and isinstance(operand[0], int) and isinstance(operator[0], int):
        return eval(operand[0] + operator[0] + operand[1])

    # If operand is a list of integers, operator is a list of integers, and operand is a list of strings,
    # return the evaluation of the expression
    if len(operand) == 2 and len(operator) == 2 and isinstance(operand[0], int) and isinstance(operator[0], str):
        return eval(operand[0]