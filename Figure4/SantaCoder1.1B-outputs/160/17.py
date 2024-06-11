def do_algebra(operator, operand):
    
    # Check if operand is empty
    if len(operand) == 0:
        return 0

    # Check if operator is empty
    if len(operator) == 0:
        return 0

    # Check if operator is a single element
    if len(operator) == 1:
        return operand[0]

    # Check if operator is a single element
    if len(operand) == 1:
        return operator[0]

    # Check if operator is a single element
    if len(operator) == 2:
        if operator[0] == '+' and operator[1] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '+' and operator[1] == '/':
            return operand[0] // operand[1]
        elif operator[0] == '+' and operator[1] == '**':
            return operand[0] ** operand[1]
        elif operator[0] == '-' and operator[1] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '-' and operator[1] == '/':
            return operand[0] // operand[1]
        elif operator[0] == '-' and operator[1] == '**':
            return operand[0] ** operand[1]
        elif operator[0] == '*' and operator[1] == '/':
            return operand[0] // operand[1]
        elif operator[0] == '*' and operator[1] == '**':
            return operand[0] ** operand[1]
        elif operator[0] == '/' and operator[1] == '**':
            return operand[0] ** operand[1]
        else:
            return 0

    # Check if operator is a single element
    if len(operand) == 2:
        if operator[0] == '+' and operator[1] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '+' and operator[1] == '/':
            return operand[0] // operand[1]
        elif operator[0] == '+' and operator[1] == '**':
            return operand[0] ** operand[1]
        elif operator[0] == '-' and operator[1] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '-' and operator[1] == '/':
            return operand[0] // operand[1]
        elif operator[0]