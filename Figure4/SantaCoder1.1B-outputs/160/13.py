def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise Exception("The length of operator list is not equal to the length of operand list minus one.")

    # Initialize the result
    result = 0

    # Iterate through the operator list
    for i in range(len(operator)):
        # Get the operator
        op = operator[i]

        # Get the operand
        operand_i = operand[i]

        # If the operator is addition, subtract, multiply, or divide
        if op in ['+', '-', '*', '/']:
            # Get the first operand
            operand_i_1 = operand[i + 1]

            # Get the second operand
            operand_i_2 = operand[i + 2]

            # If the operator is addition, subtract, multiply, or divide
            if op == '+':
                result += operand_i + operand_i_1
            elif op == '-':
                result -= operand_i - operand_i_1
            elif op == '*':
                result *= operand_i * operand_i_1
            elif op == '/':
                result /= operand_i / operand_i_1

        # If the operator is exponentiation
        elif op == '**':
            # Get the base
            base = operand_i

            # Get the exponent
            exponent = operand_i_1

            # Raise the base to the exponent
            result = base ** exponent

    return result

if