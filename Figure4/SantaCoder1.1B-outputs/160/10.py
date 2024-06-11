def do_algebra(operator, operand):
    
    if len(operator) != len(operand) - 1:
        raise ValueError("operator and operand lists must have the same length")

    # Initialize the result to 0
    result = 0

    # Iterate through the operator list
    for i in range(len(operator)):
        # Get the operator
        op = operator[i]

        # Get the operand
        operand_i = operand[i]

        # Check if the operator is a basic algebra operation
        if op in basic_algebra_ops:
            # Get the function to call
            func = basic_algebra_ops[op]

            # Call the function
            result += func(operand_i)
        else:
            # Get the function to call
            func = operator_funcs[op]

            # Call the function
            result += func(operand_i)

    return result


