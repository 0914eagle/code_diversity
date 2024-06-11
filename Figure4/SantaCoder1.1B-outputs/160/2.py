def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise ValueError("The length of operator list is not equal to the length of operand list minus one.")

    # Build the expression
    expression = ''
    for i in range(len(operator)):
        if operator[i] == '+':
            expression += str(operand[i] + operand[i + 1])
        elif operator[i] == '-':
            expression += str(operand[i] - operand[i + 1])
        elif operator[i] == '*':
            expression += str(operand[i] * operand[i + 1])
        elif operator[i] == '//':
            expression += str(operand[i] // operand[i + 1])
        elif operator[i] == '**':
            expression += str(operand[i] ** operand[i + 1])

    return eval(expression)


